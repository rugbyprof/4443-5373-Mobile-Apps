"""
This file opens up the folder categoryJson and processes each json file
adding the category name to each candy document and posting it to mongodb
"""

from mongoManager import MongoManager
import json
import glob
from rich import print
import base64
from PIL import Image
import sys
import io


def convert_jpg_to_png_in_memory(jpg_path):
    # Open the JPG image
    with Image.open(jpg_path) as img:
        # Convert the image to PNG format in memory
        in_memory_file = io.BytesIO()
        img.save(in_memory_file, format='PNG')
        # Seek to the beginning of the stream
        in_memory_file.seek(0)
        return in_memory_file.getvalue()
    

def load():
    json_files = glob.glob("./categoryJson/*.json")

    db = MongoManager()

    db.setDb("candy_store_2")

    db.dropCollection('candies')

    db.dropCollection('categories')

    db.dropCollection('images')


    category_id = 0
    candy_id = 0
    candy_long_ids = []
    big_candy_dict = {}
    for file in json_files:
        print(file)
        parts = file.split("/")
        image_folder = parts[-1][:-5]
        category = parts[-1][:-5].replace("-", " ").title()

        print(category)

        summary = {}

        with open(file) as f:
            data = json.load(f)

            summary["count"] = len(data)
            summary["name"] = category
            summary["_id"] = category_id
            summary["candies"] = []
            category_id += 1

            # iterate over the candy items in each of the category files
            for id, item in data.items():
                if not 'categories' in item:
                    item["categorys"] = []

                # if first time seeing this candy add its id to a list
                if not id in candy_long_ids:
                    candy_long_ids.append(id)
                else:
                    # get the index location of the original candy id
                    print(f"id: {id} exists at {index}! "+"="*20)
                    

                index = candy_long_ids.index(id)

                if not index in big_candy_dict:
                    item["_id"] = index
                    big_candy_dict[index] = item
                    summary["candies"].append(index)
                    item['img_path'] = "./images/"+image_folder+"/"+id+'.jpg'
                    print(item['img_path'])
            
                big_candy_dict[index]["categorys"].append(category_id)

                #print(item)
                # db.setCollection("candies")
                # db.post(item)
        db.setCollection('categories')
        db.post(summary)
        candy_id += 1

    db.setCollection("candies")
    for id,item in big_candy_dict.items():
        db.post(item)

    db.setCollection("images")
    for id,item in big_candy_dict.items():
        
        png_data = convert_jpg_to_png_in_memory(item['img_path'])
        db.store_image_in_mongodb(id,png_data)

    
    print(len(big_candy_dict))
    with open("big_updated_candy.json","w") as f:
        json.dump(big_candy_dict,f)
    

if __name__ == "__main__":

    load()

