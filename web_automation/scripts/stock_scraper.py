#!/usr/bin/env python3

from datetime import datetime as dt
import requests
import time


def fetch_stock_csv(stock, start, end):
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) " +
               "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 " +
               "Safari/537.36"}

    url = "https://query1.finance.yahoo.com/v7/finance/download/{}" \
          "?period1={}&period2={}&interval=1d&events=" \
          "history&includeAdjustedClose=true".format(stock, start, end)
    fname = "files/{}_{}_{}.csv".format(stock, start, end)

    content = requests.get(url, headers=headers).content
    with open(fname, "wb") as file:
        file.write(content)


def fetch_start_date():
    start = input("Enter start date in yyyy/mm/dd: ")
    dt_obj = dt.strptime(start, "%Y/%m/%d")
    epoch = int(time.mktime(dt_obj.timetuple()))
    return epoch


def fetch_end_date():
    end = input("Enter end date in yyyy/mm/dd: ")
    dt_obj = dt.strptime(end, "%Y/%m/%d")
    epoch = int(time.mktime(dt_obj.timetuple()))
    return epoch


def main():
    stock = input("Enter stock symbol: ")
    start_epoch = fetch_start_date()
    end_epoch = fetch_end_date()
    fetch_stock_csv(stock, start_epoch, end_epoch)


if __name__ == "__main__":
    main()
