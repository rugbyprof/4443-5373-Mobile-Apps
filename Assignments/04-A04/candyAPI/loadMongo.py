from mongoDBInterface import MongoDBInterface
import json
import glob
from rich import print
import sys

json_files = glob.glob("./categoryJson/*.json")

db = MongoDBInterface('candy_store','candies')


for file in json_files:
    print(file)
    parts = file.split('/')
    category = parts[-1][:-5]
    print(category)
    
    with open(file) as f:
        data = json.load(f)
        for id,item in data.items():
            item['category'] = category
            print(item)
            db.post(item)


