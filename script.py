#!/usr/bin/env python3

import requests

SITE_ID = str(input("SITE ID: "))
SELLER_ID = int(input("SELLER_ID: "))

#SITE_ID="MLA"
#SELLER_ID="179571326"

req = requests.get(f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={SELLER_ID}")

info = req.json()
items = info['results']

with open("LOG", 'w') as f:
    for item in items:
        itemID = item['id']
        title = item['title']
        category_id = item['category_id']

        req = requests.get(f"https://api.mercadolibre.com/categories/{category_id}")
        info = req.json()
        
        category_name = info['name']

        print(itemID, title, category_id, category_name, file=f)