"""
Project : Price Scraper
Author : Tao Serveaux
Goal : Schedule and trigger price alerts when target price is reached
"""

import schedule
import time
import checker

def runTask(minPrice,url):
    """
    Schedule the price check task to run every day at 9:00.

    Args :
        - minPrice (float) : target price threshold
        - url (str) : URL of the Amazon product page

    Return :
        - None : runs indefinitely until interrupted
    """

    schedule.every().day.at("9:00").do(checker.checkPrice, minPrice, url)

    while True :

        schedule.run_pending()
        time.sleep(60)
