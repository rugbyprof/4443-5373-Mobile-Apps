import glob
import json
from rich import print


files = glob.glob("categoryJson/*.json")

i = 0
for file in files:
    with open(file) as f:
        data = json.load(f)

    data["count"] = len(data)

    parts = file.split("/")
    cat = parts[-1][:-5].replace("-", " ").title()

    data["category_name"] = cat
    data["category_id"] = i
    i += 1

    
