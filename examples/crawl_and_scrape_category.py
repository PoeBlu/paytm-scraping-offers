"""
This snippet only written so
that example scripts can be run standalone within their sub-directory: python examples/crawl_and_scrape_category.py
Don't do it this way when importing from outside the repository as you should.
Simply remove the passage from start to end tags

Start Snippet
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

"""
This snippet only written so 
that example scripts can be run standalone within their sub-directory: python examples/crawl_and_scrape_category.py
Don't do it this way when importing from outside the repository as you should.
Simply remove the passage from start to end tags

End Snippet
"""

from core.db_manager import DB_Manager
from core.scrape import Scrape
from time import sleep

s = Scrape()
categories = s.get_all_categories()
dbm = DB_Manager()

# print(categories) -> Will show you all the available categories in paytm mall.
# crawl and scrape category: Speakers -> existing at 3rd index position of categores list.

for i in range(30):
    print(f"Crawling and Scraping for Category: {categories[3]['name']}")
    data = s.scrape(categories[3]['url'], s.get_query_string(page_number=i + 1, sort_type="popular"))
    dbm.insert_data(data)
    sleep(5)
