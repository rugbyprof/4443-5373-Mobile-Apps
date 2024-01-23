import re
from rich import print
import requests
from bs4 import BeautifulSoup
import bs4
import sys

candyDB = {}


def getElements(name):
    global candyDB
    print("=" * 80)
    print(name)
    print("=" * 80)
    r = requests.get(f"https://www.candystore.com/collections/{name}")
    html_content = r.text

    # Parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    # Find all elements with class 'product-grid-item'
    product_grid_candyDB = soup.find_all(class_="product-grid-item")

    candyDB[name] = []

    # Print or process the found elements
    for item in product_grid_candyDB:
        desc = None
        img = None
        price = None

        desc = item.find("p").get_text().strip()
        img = item.find("noscript").find("img")

        # img["src"] = f"https://{img.strip()}"
        print(img)

        price = item.find_all("span", {"class": "visually-hidden"})

        if len(price) > 0:
            price = float(price[-1].get_text().strip().strip("$"))

        candyDB[name].append(
            {"desc": desc, "img": "https:" + img["src"], "price": price}
        )

        # You can further process each item as needed


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


if __name__ == "__main__":
    names = getBrands()

    for name in names:
        print(f"https://www.candystore.com/collections/{name}")
        # class="grid-item small--one-half medium--one-third large--one-third xlarge--one-quarter sold-out"

        elements = getElements(name)
        print(candyDB)
        sys.exit()
