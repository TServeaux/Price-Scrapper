"""
Project : Price Scraper
Author : Tao Serveaux
Goal : Scrape a product on amazon
"""

import requests
from bs4 import BeautifulSoup

def getProduct(url) :
    """
    Fetch the HTML content of an Amazon product page.

    Arg :
        - url (str) : URL of the Amazon product page

    Return :
        - response.content (str) : raw HTML content of the page
    """

    response = requests.get(

        url,

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36",
            "Accept-Language": "fr-FR,fr;q=0.9",
            "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding" : "gzip, deflate, br"
        },

        verify = True,
        timeout = 10,
    )

    response.raise_for_status()

    return response.content

def getPrice(url) :
    """
    Extract the price of an Amazon product from its page.

    Arg :
        - url (str) : URL of the Amazon product page

    Return :
        - price (float) : current price of the product as a string
    """

    page = getProduct(url)
    soup = BeautifulSoup(page, "html.parser")
    price = soup.find("input", {"id": "twister-plus-price-data-price"})["value"]

    return price

