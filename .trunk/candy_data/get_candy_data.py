import requests
import bs4

with open("candy_categories.txt") as f:
    links = f.read().replace(" ", "").split("\n")

print(links)
