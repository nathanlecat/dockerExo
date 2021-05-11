#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask,render_template,request
import requests
import json
from random import randint

app = Flask(__name__)

data = {}



@app.route('/', methods=['get', 'post'])
def Home():
    r = JSON()
    if request.method == 'POST':
        reponse = request.form["prixObjet"]
        data['tentative'] = reponse
        data['reponse'] = reponse
        if int(reponse) > data['price']:
             data["resultat"] = "C'est plus ! Recommence !"
        elif int(reponse) < data["price"]:
            data["resultat"] = "C'est moins ! Recommence !"
        elif int(reponse) == data['price']:
            
            data["resultat"] = "Bravo c'est exatcement ça !!!"
    else:
        product = r['name']
        priceProduct = r['price']
        imgProduct = r['imgProduct']
        descProduct = r['Description']
        data['product']=product
        data['price']=priceProduct
        data['image']=imgProduct
        data['description']=descProduct
        data['reponse'] = 0
        data["resultat"]="A vous de jouer, trouver le prix de cette objet !"
        data["tentative"] = '0'
    return render_template('index.html', title="Le Juste Prix", data=data)
    

def JSON():
    api_token = '9fa0010adcmshe131dc1bfa56f2dp104431jsn2e6c85c945c1'
    URL = 'http://localhost:3000/api'
    headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}
    api_url = '{0}/products'.format(URL)
    response = requests.get(api_url, headers=headers)
    products = response.json()

    productObj = {}

    productNumberAleatoire = randint(1, 3)
    productFormated = {}
    for product in products['data']:
      if product['id'] == productNumberAleatoire:
          productFormated = product
      else:
        print('ERROR => ')
    ...
    return productFormated

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)