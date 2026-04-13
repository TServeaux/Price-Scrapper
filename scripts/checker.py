"""
Project : Price Scraper
Author : Tao Serveaux
Goal : Check product price and trigger notifications if below target
"""

import scrape
import notifier

def checkPrice(minimumPrice, url) :
    """
    Check if the Amazon product price is below the target price
    and send notifications if so.

    Args :
        - minimumPrice (float) : target price threshold
        - url (str) : URL of the Amazon product page

    Return :
        - None : sends email and Telegram alert if price is below threshold
    """

    price = scrape.getPrice(url)

    if price <= minimumPrice :

        notifier.sendAll(f"Product under {minimumPrice} \n\n This product {url} is under your target price.",
                         f"This product {url} is under {minimumPrice}.")