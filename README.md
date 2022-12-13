# Multimedia Classification System
By Ignacio Arnaiz Tierraseca & Luis Daniel Casais Mezquida  
Multimedia 22/23  
Bachelor's Degree in Computer Science and Engineering, grp. 89  
Universidad Carlos III de Madrid  

Creation of an Information Retrieval System based on [ElasticSearch](https://www.elastic.co/es/products/elasticsearch).


## Introduction and goals
The goal of the lab case is to build an Information Retrieval System based on ElasticSearch.  

During Block 1 of this course you have worked with a collection of images of film posters available in IMDB ([repo here](github.com/ldcas-uc3m/MM-Project1)). Those images have additional information of the given film such as director, actor, release date and so on. A short description of the film is also available as well as comments and reviews provided by web site users.  
The Information Retrieval (IR) system to be developed must allow searching on this textual content.

## Lab case development
The implementation of the IR system will follow the steps or phases described below:


### Step 1
Definition of ES index structure and mappings to store film data according to the queries described in Step 3.   
This can be found in `scripts/mappings.json`.

### Step 2
Using an ES instance, deploy the structures defined in step 1. Index HTML pages containing the data of each film. The Excel file provided (`data/MovieGenreIGC_v3.xlsx`) with the images of the posters also contains links to the HTML pages of the films.  

You must develop a web scraper (`scraper.py`) and use it to generate the bulk data (`data/bulk_data`).

### Step 3
Implement the queries needed to run the following searches on the films collection
built in steps 1 and 2:
1. World War II films produced from 1980 onwards.
2. Directors with the most action films.
3. LGBTQ-themed films available in the collection. In addition to the listing,
show the number of films by year.
4. Films dealing with corrupt politicians in Europe and the United States.

Use 50 results per query.


## Execution

### Scraper
First install python, pip and the requirements:
```
pip install -r requirements.txt
```

Then execute the script:
```
python3 scraper.py
```

### ElasticSearch and queries
Download, install and run [ElasticSearch](https://www.elastic.co/es/downloads/elasticsearch).  

You can run the whole script or step by step, as you prefer:
```
chmod +x run.sh
./run.sh
```