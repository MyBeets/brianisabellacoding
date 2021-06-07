from json import load, dump
import requests
import sqlite3
from datetime import datetime

def get_data(key: str) -> dict:
    return requests.get(
        url = 'https://api.hypixel.net/skyblock/bazaar',
        params = {'key': key}
    ).json()

def create_the_database() -> sqlite3.Connection:
    con = sqlite3.connect('sqdata.db')
#    cur = con.cursor()
#    cur.execute('CREATE TABLE bzdata (timestamp, item, instantBuy, instantSell)')
    return con



con = create_the_database()
cur = con.cursor()
data = get_data('9f2001ea-1048-4575-8ce0-e6d274d7d19d')['products']
for product, val in data.items():
    timestamp = datetime.now().isoformat()
    sell_summary_list = val['sell_summary']
    sell_price_per_unit = sell_summary_list[0]['pricePerUnit'] if len(sell_summary_list) > 0 else None
    buy_summary_list = val['buy_summary']
    buy_price_per_unit = buy_summary_list[0]['pricePerUnit'] if len(buy_summary_list) > 0 else None

    cur.execute(f"INSERT INTO bzdata VALUES ('{timestamp}','{product}','{sell_price_per_unit}', '{buy_price_per_unit}')")

con.commit()
