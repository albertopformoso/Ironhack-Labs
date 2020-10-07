![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API and Web Data Scraping

### Process

First I searched for a data set to work with, I used a netflix catalogue obtained from kaggle (https://www.kaggle.com/shivamb/netflix-shows) 
With this data set I droped the columns I don't need and check the columns with missing values and make a plan to fill them either with web scraping or api.

Then to use the OMDb API and have precise results I needed the IMDb movies id so I web scrapped IMDb site to obtain them. To do so I first tried to make a while loop obtaining each value of the titles column but I had problems and it wasn't very eficient so I made a function to obtain the id of the movies and later used an '.apply' to the data frame.

Once I obtained the id's of the movies and tv shows it's time to use the API to retrive information. So I firs made some functions to obtain the missing information on directro's, cast and country columns because these ones has the most missing values that I could obtain from the API, also I made some functions to retrive IMDb, Rotten Tomatoes and Metacritic scores to make some analysis. Then I applied the functions to the columns and created new columns for the scores.

It is important to mention that the retriving functions took a long time and I tried to use the multiprocessing library but on Jupyter the kenrel broke every time I tried to use it so I need to investigate to solve this problem and this could be considered a future improvement.

Finally with the data frame filled with the information and the scores of each rating site I performed some analysis.

The pie chart tell us there are more movies than tv shows on the netflix catalogue I retrived. The catalogue has information of thv shows and movies available on Netflix as of 2019

![](output/plots/MoviesVsTVShows.png)
**Figure 1** - Movies vs Tv Shows

The horizontal barchart indicates us which are the countries with more content on the platform.

![](output/plots/TopCountriesWithMoreContent.png)
**Figure 2** - Top Content On Each Country

Also I made a line chart indicating the quantity of movies and tv shows released by year.

![](output/plots/MoviesAndTVShowsByReleaseYear.png)
**Figure 3** - Movies and TV Shows by Year Realese

And finally the scores of the different platforms and wich score is more offten given by the platform

![](output/plots/IMDb_ratings.png)
**Figure 4** - IMDb Scores

![](output/plots/Rotten_tomatoes_ratings.png)
**Figure 5** - Rotten Tomatoes Scores

![](output/plots/metacritic_ratings.png)
**Figure 6** - Metacritic Scores