from bs4 import BeautifulSoup
from rich import print
import json
import os
import random
import re
import requests
import sys
import time

candyDB = {}


def random_delay(min_delay, max_delay):
    """
    Sleeps for a random amount of time between min_delay and max_delay seconds.

    Parameters:
    - min_delay (float): Minimum amount of time to delay in seconds.
    - max_delay (float): Maximum amount of time to delay in seconds.
    """
    delay = random.uniform(min_delay, max_delay)
    print(f"Sleeping for: {round(delay,2)}")
    time.sleep(delay)


def download_image(image_url, filename):
    response = requests.get(image_url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.

    with open(filename, "wb") as f:
        f.write(response.content)


def ensure_folder_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def stageThree(category, id, image_url):
    global candyDB

    filename = f"./images/{category}/{id}.jpg"

    if os.path.exists(filename):
        return

    response = requests.get(image_url)
    response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.

    # Example usage:
    ensure_folder_exists(f"./images/{category}")

    with open(filename, "wb") as f:
        f.write(response.content)


def stageTwo(category, id, candy_url):
    global candyDB
    r = requests.get(f"{candy_url}")
    html_content = r.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    prod_desc = soup.find(
        "div", class_="product-description rte", itemprop="description"
    )
    desc = prod_desc.find("p").text

    candyDB[category][id]["desc"] = desc


def stageOne(collection_url):
    """Get some basic candy data from the first page of each candy collection."""
    global candyDB
    r = requests.get(f"{collection_url}")
    html_content = r.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all elements with class 'product-grid-item'
    product_grid_candyDB = soup.find_all(
        class_="grid-item small--one-half medium--one-third large--one-third xlarge--one-quarter"
    )

    collName = collection_url.split("/")
    collName = collName[-1]
    print(collName)

    candyDB[collName] = {}

    # Print or process the found elements
    for item in product_grid_candyDB:
        # pull necessary items out of grid element (candy data)
        image = item.find("img")
        price_tag = item.find_all(class_="visually-hidden")
        id = item.find(class_="cat-add-form addToCartForm").find(
            "input", {"name": "id"}
        )["value"]
        name = item.find("p")
        ahref = item.find("a")
        prod_url = f'https://www.candystore.com{ahref["href"]}'
        candyName = name.text
        img_widths = json.loads(image["data-widths"])
        img_url = image["data-src"]
        img_url = "https:" + img_url.replace("{width}", str(img_widths[-1]))
        price = None
        for pt in price_tag:
            if "$" in pt.text:
                price = float(pt.text.strip("$"))

        candyDB[collName][id] = {}

        candyDB[collName][id]["id"] = id
        candyDB[collName][id]["name"] = candyName
        candyDB[collName][id]["prod_url"] = prod_url
        candyDB[collName][id]["img_url"] = img_url
        candyDB[collName][id]["price"] = price


def getBrands():
    with open("candy_brands.html") as f:
        text = f.read()

    # Regular expression pattern
    pattern = r'/collections/([^"]+)'

    # Find all matches
    matches = re.findall(pattern, text)

    unique = {}

    # Print matches
    for match in matches:
        if not match in unique and not "v=" in match:
            unique[match] = 0

    names = list(unique.keys())
    return names


def usage():
    print("python generate_db.py ")
    print("   where n = the stage number (1-3)")
    sys.exit()


if __name__ == "__main__":
    stage = sys.argv[1]

    print(stage)

    """
    I could have made it so the script ran all at once, but that usually takes more time and 
    effort because 
    """

    if stage == "1":
        """
        Get the first page of candy data from each candy category which gives anywhere from 3-50+ candy items.
        In total, scraping only the first page, I still get 777 candies.
        """
        with open("candy_categories.txt") as f:
            urls = f.read().split("\n")

            for url in urls:
                url = url.replace(" ", "")
                print(url)
                stageOne(url)  # Run stage one

        with open("candyDB.json", "w") as f:
            json.dump(candyDB, f)
    elif stage == "2":
        """This opens the candy page for the single candy and grabs the description, if there is one."""
        with open("candyDB.json") as f:
            candyDB = json.load(f)

        tot_candys = 0
        for category, category_items in candyDB.items():
            print(category)
            for id, candy in category_items.items():
                tot_candys += 1
                print(f'{category} {tot_candys} {candy["prod_url"]}')
                stageTwo(category, id, candy["prod_url"])
                random_delay(
                    0.6, 1.3
                )  # This will pause the script for a random time between 1 and 3 seconds

            with open(f"./json/{category}.json", "w") as f:
                json.dump(candyDB[category], f)

    elif stage == "3":
        """
        Get the images associated with each candy item and save them using the name structure: candy_id.jpg
        """
        with open("candyDB.json") as f:
            candyDB = json.load(f)

        tot_candys = 0
        for category, category_items in candyDB.items():
            print(category)
            for id, candy in category_items.items():
                tot_candys += 1
                print(f'{category} {tot_candys} {candy["img_url"]}')
                stageThree(category, id, candy["img_url"])
                random_delay(
                    0.6, 1.3
                )  # This will pause the script for a random time between 1 and 3 seconds
