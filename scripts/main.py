"""
Project : Price Scraper
Author : Tao Serveaux
Goal : Entry point of the application
"""

import scheduler

if __name__ == "__main__" :

    scheduler.runTask(5.5, "https://www.amazon.fr/dp/B01DN8TEA2")