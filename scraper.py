'''
IMDb scraper
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
import json


DB_PATH = "MovieGenreIGC_v3.xlsx"
OUTPUT = "output.json"

# Define variable to load the dataframe
dataframe = openpyxl.load_workbook(DB_PATH)
 
# Define variable to read sheet
dataframe1 = dataframe.active
    





def getData_type1(url: str) -> dict:
    '''
    Returns a dictionary with title, director, description, year, and genres
    of the movie specified in the IMDb url.
    Returns an empty dictionary if the page doesn't exist.
    For pages without videos.
    '''

    if "http://www.imdb.com/title/tt" not in url:
        return {}

    r = requests.get(url)

    if r.status_code != 200:
        return {}


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
    genres = imdb.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-6.bunqBa > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-8.hOtbMQ > div.sc-16ede01-9.bbiYSi.sc-7643a8e3-11.efPxUc > div.ipc-chip-list--baseAlt.ipc-chip-list.sc-16ede01-5.ggbGKe > div.ipc-chip-list__scroller > a")
    parsed_genres = []

    for elem in genres:
        parsed_genres.append(elem.text)

    return {
        "title": title.text,
        "director": director.text,
        "year": year.text,
        "description": desc.text,
        "genres": parsed_genres
    }


def getData_type2(url: str) -> dict:
    '''
    Returns a dictionary with title, director, description, year, and genres
    of the movie specified in the IMDb url.
    Returns an empty dictionary if the page doesn't exist.
    For pages with videos.
    '''
    if "http://www.imdb.com/title/tt" not in url:
        return {}

    r = requests.get(url)

    if r.status_code != 200:
        return {}

    imdb = BeautifulSoup(r.text, "html.parser")

    # movie title
    title = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > h1")
    # director
    director = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-fa02f843-2.dwQKsL > div > div > ul > li:nth-child(1) > div > ul > li > a")
    # description
    desc = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-16ede01-8.hXeKyz.sc-7643a8e3-11.efPxUc > p > span.sc-16ede01-2.gXUyNh")
    # year
    year = imdb.select_one("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-80d4314-0.fjPRnj > div.sc-80d4314-1.fbQftq > div > ul > li:nth-child(1) > span")


    # genres
    genres = imdb.select("#__next > main > div > section.ipc-page-background.ipc-page-background--base.sc-9b716f3b-0.hWwhTB > section > div:nth-child(4) > section > section > div.sc-7643a8e3-2.ebKPVC > div.sc-7643a8e3-10.itwFpV > div.sc-7643a8e3-4.iAthmE > div.sc-16ede01-8.hXeKyz.sc-7643a8e3-11.efPxUc > div > div.ipc-chip-list__scroller > a")
    parsed_genres = []

    for elem in genres:
        parsed_genres.append(elem.text)

    return {
        "title": title.text,
        "director": director.text,
        "year": year.text,
        "description": desc.text,
        "genres": parsed_genres
    }

def main():
    '''
    Goes through the database on DB_PATH and gets the urls,
    using those to scrape the data of each movie, and saving it to OUTPUT
    '''
    data = {}
    data['movies'] = []

    result = dict()

    # Iterate the loop to read the cell values
    for row in range(1, dataframe1.max_row):
        for col in dataframe1.iter_cols(2, 2):
            #print(col[row].value)
            movieUrl =col[row].value
            result = getData_type1(movieUrl)
            data['movies'].append({
                'movie_title': result["title"],
                'movie_director': result["director"],
                'movie-year': result["year"],
                'movie-description': result["description"]})

            
    with open(OUTPUT, 'w') as file:
        json.dump(data, file, indent=4)

    pass


def test():
    # type 1
    print(getData_type1("http://www.imdb.com/title/tt0357608/"))  # one genre
    print(getData_type1("http://www.imdb.com/title/tt4991286/"))  # multiple genres
    print(getData_type1("http://www.imdb.com/title/tt0adfdf7608/"))  # fails

    # type 2
    print(getData_type2("http://www.imdb.com/title/tt0780504"))  # one genre
    print(getData_type2("http://www.imdb.com/title/tt0446029"))  # multiple genres
    print(getData_type1("http://www.imdb.com/title/tt0adfdf7608/"))  # fails


if __name__ == "__main__":
    # test()
    main()
