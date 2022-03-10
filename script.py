#!/usr/bin/env python3

import requests

'''
    Requiere como parametros de entrada el SITE_ID y el SELLER_ID

    SITE_ID es de tipo string
    SELLER_ID es de tipo entero
'''

SITE_ID = str(input("SITE ID: "))
SELLER_ID = int(input("SELLER_ID: "))

#SITE_ID="MLA"
#SELLER_ID="179571326"


'''
    Se hace una peticion a la API sites de ML utilizando los parametros de entrada

    Luego obtenemos los items del usuario
'''

req = requests.get(f"https://api.mercadolibre.com/sites/{SITE_ID}/search?seller_id={SELLER_ID}")

info = req.json()
items = info['results']


'''
    Por cada item del usuario, obtenemos los datos requeridos.

    Para obtener el nombre de la categoria utilizamos el valor de category_id, y una llama a la API de categories

    Luego guardamos en el archivo LOG todos los datos necesarios
'''
with open("LOG", 'w') as f:
    for item in items:
        itemID = item['id']
        title = item['title']
        category_id = item['category_id']

        req = requests.get(f"https://api.mercadolibre.com/categories/{category_id}")
        info = req.json()
        
        category_name = info['name']

        print(itemID, title, category_id, category_name, file=f)