"""
url à scrapper : http://books.toscrape.com/

Exercice : Choisissez n'importe quelle page Produit sur le site de Books to Scrape.
Écrivez un script Python qui visite cette page et en extrait les informations suivantes :

product_page_url
universal_ product_code (upc)
title
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url

Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.
"""

from bs4 import BeautifulSoup
import requests
import csv

#url de la page du livre à scrapper
url_livre = "http://books.toscrape.com/catalogue/i-know-what-im-doing-and-other-lies-i-tell-myself-dispatches-from-a-life-under-construction_704/index.html"
req = requests.get(url_livre)

if req.ok:
    soup = BeautifulSoup(req.text, features="html.parser")

    titre = soup.find("h1")

    liste_carac_livre = soup.findAll("td")

    description = soup.find("div", id="product_description")
    description = description.nextSibling.nextSibling.string # J'ai recherché le tag "div" avec l'id "product_description" et je me suis déplacé 2 fois pour trouver la description

    categorie = soup.find("li")
    categorie = categorie.nextSibling.nextSibling.nextSibling.nextSibling

    image_source = soup.find("img").get("src")

    with open("fiche_livre.csv", "w", encoding="utf-8") as livre_csv:
        livre_csv.write("product_page_url, universal_ product_code (upc), title, price_including_tax,"
                        "price_excluding_tax, number_available, product_description, category, review_rating, image_url" "\n\n")
        livre_csv.write(url_livre + "," + "\n" + liste_carac_livre[0].text + "," + "\n" + titre.string + "," + "\n" +
                        liste_carac_livre[3].text.replace("Â", "") + "," + "\n" + liste_carac_livre[2].text.replace("Â", "") +
                        "," + "\n" + liste_carac_livre[5].text + "," + "\n" + '"' + description + '"' + "," + "\n" + categorie.text.replace("\n","") +
                        "," + "\n" + liste_carac_livre[6].text + "," + "\n" + image_source.replace("../..", "http://books.toscrape.com"))