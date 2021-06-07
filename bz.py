from json import load, dump
import requests
import sqlite3

def get_data(key: str) -> dict:

    assert isinstance(key, str)

    return requests.get(
        url = 'https://api.hypixel.net/skyblock/bazaar',
        params = {'key': key}
    ).json()

def download_data(key: str) -> None:
    data = get_data(key)
    with open('data.json', 'w') as f:
        dump(data, f, indent=4)

    return data

def create_the_database() -> sqlite3.Connection:
    con = sqlite3.connect('sqdata.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE bzdata (timestamp, item, instantBuy, instantSell)')
    return con



data = get_data('9f2001ea-1048-4575-8ce0-e6d274d7d19d')['products']

x = 0
# for name, product in data.items():
#     print (name, product)
#     quit()
print('hi')
x = 0
for name, product in data.items():
    x += 1
    sell_summary_list = product['sell_summary']
    sell_summary = sell_summary_list[0] if len(sell_summary_list) > 0 else None
    buy_summary_list = product['buy_summary']
    buy_summary = buy_summary_list[0] if len(buy_summary_list) > 0 else None
    print(x, name, sell_summary, buy_summary)
