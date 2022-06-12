import os

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

RAW_DATA_PATH = "./data/raw"


def _get_contributor_name(contributor):
    try:
        contributor_name: str = (
            contributor.find("h4", class_="").contents[0].strip()
        )
        contributor_name_nospace = "".join(contributor_name.split())
    except IndexError as e:
        print(e)
        print("\nContributor name not found inside div")

    return contributor_name_nospace


def _get_contributor_img_url(contributor_name, contributor):
    try:
        contributor_img_url = contributor.findAll("img")[0]["src"]
    except IndexError as e:
        print(f"\n{e}\nCouldn't find {contributor_name}'s img file")
    except KeyError as e:
        print(f"\n{e}\nCouldn't find {contributor_name}'s image src url")

    return contributor_img_url


def _create_destiny_dir(contributor_name):
    image_destiny_path = f"{RAW_DATA_PATH}/{contributor_name}"
    try:
        os.mkdir(image_destiny_path)
    except FileExistsError as e:
        print(f"\n{e}\nPath already exists for: {contributor_name}")
    return image_destiny_path


def retrieve_contributors_data():
    """Retrieves the Contributors data from Poatek's Team web page that is
    available at https://poatek.com/our-team

    Raises:
        SystemExit: When the Poatek's Team Page in unreacheble
    """

    # Poatek team page
    URL = "https://poatek.com/our-team"

    # Retrieve Poatek Team page data using requests
    try:
        page = requests.get(URL)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    # Retrieve the page html data with Beautiful Soup
    soup = BeautifulSoup(page.content, "html.parser")

    # Get the Data from the div with all the contributors
    contributors_data = soup.find_all("div", {"class": "team team_vertical"})

    for contributor_data in tqdm(contributors_data, desc="Downloading data"):
        contributor_name = _get_contributor_name(contributor_data)
        contributor_img_url = _get_contributor_img_url(
            contributor_name, contributor_data
        )
        image_destiny_path = _create_destiny_dir(contributor_name)

        img_extension = contributor_img_url.split(".")[-1]
        img_data = requests.get(contributor_img_url).content
        with open(
            f"{image_destiny_path}/profile_pic.{img_extension}", "wb"
        ) as handler:
            handler.write(img_data)

        print(
            f"\n{contributor_name}: {contributor_img_url} | {image_destiny_path}"
        )


def main():

    retrieve_contributors_data()


if __name__ == "__main__":
    main()
