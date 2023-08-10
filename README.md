# Random Movie Generator from IMDB Data

Welcome to the Random Movie Generator Project! This project allows you to dynamically generate random movies based on
IMDB data. It involves web scraping, data manipulation, and a web server to present recommendations. 

## Table of Contents
- [Installation]
- [Usage]
- [Overview]

## Installation
1. Clone this repository
 git clone https://github.com/your-username/your-repo.git
2. Install the required dependencies
 pip install -r requirements.txt

## Usage
1. Run the `main.py` script to scrape IMDb's top-rated movies and save them to an Excel file:
2. Generate a random movie recommendation HTML page:
3. Start the web server to access the random movie recommendation:

## Overview
1. main.py - This script performs web scraping on IMDB's top-rated movies. It uses the 'requests' library to send a GET
   request to IMDB's website and retreive movie data. The BeautifulSoup library is used to parse the HTML response and
   extract relevant information. The extracted data (movie rank, name, year, rating, image URL) is saved to an EXCEL file
   using the 'openpyxl' library.
2. generate_html.py - The script reads data from the Excel file generated by 'main.py'. If data is available, it randomly
   selects a movie and extracts its details (rank, name, movie, rating, image URL). It generates an HTML page dynamically
   with the selected movie's details and saves it as 'random_movie.html'. The HTML includes links to the CSS file and
   buttons to open more information or generate another recommendation.
3. styles.css - This CSS file provides styling for the dynamically generated HTML page. It defines various classes
    to format elements like headers, images, buttons, and containers. The styling ensures a visually appealing layout.
4. Server.py - This script sets up a local web server to showcase the random movie recommendation. It uses the
  'http.server' module to create a server instance with a custom handler. The server serves the 'random_movie.html'
   and 'styles.css' files, as well as handing requestions for additional functionality. 
   
