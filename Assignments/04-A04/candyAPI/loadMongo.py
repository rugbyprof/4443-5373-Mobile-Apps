"""
This file opens up the folder categoryJson and processes each json file
adding the category name to each candy document and posting it to mongodb
"""

from mongoManager import MongoManager
import json
import glob
from rich import print
import sys


def load(**kwargs):
    json_files = glob.glob("./categoryJson/*.json")

    # not used right now
    username = kwargs.get("username", None)
    password = kwargs.get("password", None)
    db = kwargs.get("db", None)

    collection1 = kwargs.get("collection1", None)
    collection2 = kwargs.get("collection2", None)

    print(collection1)
    print(collection2)

    # No auth right now
    # db1 = MongoManager(username=username, password=password, db=db)
    # db2 = MongoManager(username=username, password=password, db=db)

    db1 = MongoManager()
    db2 = MongoManager()

    db1.setDb("candy_store")
    db2.setDb("candy_store")

    db1.dropCollection(collection1)
    db2.dropCollection(collection2)

    db1.setDb("candy_store")
    db2.setDb("candy_store")

    db1.setCollection("candies")
    db2.setCollection("categories")

    i = 0
    for file in json_files:
        print(file)
        parts = file.split("/")
        category = parts[-1][:-5].replace("-", " ").title()

        print(category)

        summary = {}

        with open(file) as f:
            data = json.load(f)

            summary["count"] = len(data)
            summary["name"] = category
            summary["id"] = i

            for id, item in data.items():
                item["category"] = category
                item["category_id"] = i
                print(item)
                db1.post(item)
        db2.post(summary)
        i += 1


if __name__ == "__main__":

    kwargs = {
        "username": "griffin",
        "password": "HorseCatDonkeyBattery",
        "db": "candy_store",
        "collection1": "candies",
        "collection2": "categories",
    }

    load(**kwargs)
