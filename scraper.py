'''
IMDb scraper
'''

import requests
from bs4 import BeautifulSoup
# import panda as pd

def getData_type1(url: str):
    # pages w/out videos

    r = requests.get(url)

    # r.status_code
    # r.headers["Content-Type"]
    # r.text

    imdb = BeautifulSoup(r.text, "html.parser")

    # movie title
    title = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > h1")
    # director
    director = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-6.bunqBa > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-8.hOtbMQ > div.sc-fa02f843-2.dwQKsL > div > div > ul > li:nth-child(1) > div > ul > li > a")
    # description
    desc = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-6.bunqBa > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-8.hOtbMQ > div.sc-16ede01-9.bbiYSi.sc-7643a8e3-11.efPxUc > div.sc-16ede01-7.hrgVKw > span.sc-16ede01-1.kgphFu")
    # year
    year = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(1) > span")


    # genres
    genres = imdb.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-16ede01-8.hXeKyz.sc-7643a8e3-11.efPxUc > div > div.ipc-chip-list__scroller > a:nth-child(2)")

    print(title.text)
    print(director.text)
    print(desc.text)
    print(year.text)
    print(genres)


def getData_type2(url: str):
    # pages w/out videos
    
    r = requests.get(url)

    # r.status_code
    # r.headers["Content-Type"]
    # r.text

    imdb = BeautifulSoup(r.text, "html.parser")

    # TODO: Redo selectors

    # movie title
    title = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > h1")
    # director
    director = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-6.bunqBa > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-8.hOtbMQ > div.sc-fa02f843-2.dwQKsL > div > div > ul > li:nth-child(1) > div > ul > li > a")
    # description
    desc = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-16ede01-8.hXeKyz.sc-7643a8e3-11.efPxUc > p > span.sc-16ede01-1.kgphFu")
    # year
    year = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(1) > span")


    # genres
    genres = imdb.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-16ede01-8.hXeKyz.sc-7643a8e3-11.efPxUc > div > div.ipc-chip-list__scroller > a:nth-child(2)")



# type 1
getData_type1("http://www.imdb.com/title/tt0357608/")
# getData("https://www.imdb.com/title/tt4991286/")

# type 2
getData_type2("http://www.imdb.com/title/tt0780504")
