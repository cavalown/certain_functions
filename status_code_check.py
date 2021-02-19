import os

import requests


def get_status_code():
    url = str(os.environ.get("url"))
    # url = 'https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=html&date=20170401&stockNo=1101'
    res = requests.head(url)
    stat_code = res.status_code
    print(f'Status_code: {stat_code}')


if __name__ == '__main__':
    get_status_code()
    
