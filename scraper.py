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
    





def getData(url: str) -> dict:
    '''
    Returns a dictionary with title, director, description, year, and genres
    of the movie specified in the IMDb url.
    Returns an empty dictionary if the page doesn't exist.
    '''

    if "http://www.imdb.com/title/tt" not in url:
        return {}

    url += "/reference"

    r = requests.get(url)

    # print(r.status_code, url)

    if r.status_code != 200:
        return {}


    imdb = BeautifulSoup(r.text, "html.parser")

    # movie title
    title = imdb.select_one("#main > section > div > div > h3")
    # director
    director = imdb.select_one("#main > section > section.titlereference-section-overview > div:nth-child(3) > ul > li > a")
    # description
    desc = imdb.select_one("#main > section > section.titlereference-section-overview > div:nth-child(1)")
    # year
    year = imdb.select_one("#main > section > div > div > h3 > span > a")


    # genres
    # TODO: parsing of text (it's currently shit)
    # check if there is a category (stuff changes)
    category = imdb.select_one("#main > section > div > div > ul:nth-child(9) > li:nth-child(1)")
    if category == None:
        category = imdb.select_one("#main > section > div > div > ul:nth-child(8) > li:nth-child(1)")
        print(category.text)
        if category.text in ("G", "PG", "PG-13", "R", "NC-17"):
            genres = imdb.select("#main > section > div > div > ul:nth-child(8) > li:nth-child(3) > a")
    else:
        if category.text in ("G", "PG", "PG-13", "R", "NC-17"):
            genres = imdb.select("#main > section > div > div > ul:nth-child(9) > li:nth-child(3) > a")
        
    # print(category)
    genres = imdb.select("#main > section > div > div > ul:nth-child(8) > li:nth-child(2) > a")
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
    idCount = 0
    # Iterate the loop to read the excel cell values 
    # containing the url to acces each movie iMDB url

    for row in range(1, dataframe1.max_row):
        for col in dataframe1.iter_cols(2, 2):
            #print(col[row].value)
            movieUrl =col[row].value
            result = getData_type1(movieUrl)

            if result != []:
                data['movies'].append({
                    'index': '_id:'+ idCount})

                data['movies'].append({
                    'movie_title': result["title"],
                    'movie_director': result["director"],
                    'movie-year': result["year"],
                    'movie-description': result["description"]})
            else:
                result = getData_type2(movieUrl)
                
            idCount += 1

            
    with open(OUTPUT, 'w') as file:
        json.dump(data, file, indent=4)

    pass


def test():
    # type 1
    print(getData("http://www.imdb.com/title/tt0357608"))  # one genre
    print(getData("http://www.imdb.com/title/tt4991286"))  # multiple genres
    print(getData("http://www.imdb.com/title/tt0adfdf7608"))  # fails

    # type 2
    print(getData("http://www.imdb.com/title/tt0780504"))  # one genre
    print(getData("http://www.imdb.com/title/tt0446029"))  # multiple genres
    print(getData("http://www.imdb.com/title/tt0adfdf7608/"))  # fails


if __name__ == "__main__":
    test()
    # main()
