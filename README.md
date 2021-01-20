# Movie Industry Analysis for Microsoft

**Author**: Aziza Gulyamova

![director_shot](images/director_shot.jpeg)

## Overview


The purpose of this project is to help Microsoft better understand movie industry and figure out what kind of movies are doing the best currently in the world. Using this analysis Microsoft can build up a strategy for creating their own movies that will be profitable and popular.
Through this analysis, I will show some interesting trends in the data pertaining to what successful movies have in common. 
***

## Business Problem

In order to better understand the movie industry and find out what kind of movies Microsoft should produce to get the most of it, in this project I seek to answer 4 questions that Microsoft could consider before making the decision to enter movie industry and start filming:

* What genres are the most popular and giving the most profit?
* Is there a correlation between the average ratings and the runtime of the movie?
* Is there a correlation between movie's release date and gross profit?
* What are the Top 10 successful studios and what are their content ratings focus?

The questions will provide Microsoft valuable insight on which genres it should focus on to increase its likelihood of generating high gross sales. Does it need to consider the runtime of the movie when filming, what is the best time to release the movie for higher profit and what movie content it should focus on.



![hollywood](images/Hollywood_Sign_(Zuschnitt).jpg)
***

## Data

For this project, in order to analyze the world's movie industry, the data was used from following sources:
* IMDB
* Box Office Mojo
* The Number movie Budgets
* Rotten Tomatoes

The datasets above contain various types of information about each movie, ranging from the release date, the director, the studio, to other information like the budget, the profit, the audience and critic scores from different sites.
***

![seats](images/backlight-consulting-home-hero-darkened-cinema-inside.jpg)
***

## Methods

This Project uses descriptive analysis method, like distribution and bar graphs, statistical functions. Using this method, I filter out less meaningful information and compare performance of films across differnts data sources.

* Grouping and merging some datasets helps to categorize the information and retrieve necessary data only. In this case, joining IMDB Tables and The Number Movies Table, combining average ratings and genres, group the datasets by genre, title, studio and etc. 

* Building plots and graphs improve the ability to comprehend the data and be able to analyze it better. As in this project, figure out what are the top genres and their ROI, what are the best seasons to release movies and what are top studios. 

* Statistical methods help to calculate the average values. Correlations and distributions were used for this purpose . In this case, calculate correlation between average rating and runtime, calculate the average return on investment.
***


## Results

* The analysis shows that out of 30 Top genres the most profitable ones are "Adventure, Animation, Comedy", "Action, Adventure, Sci-Fi", "Action, Adventure, Fantasy" and "Action, Adventure, Comedy" genres. But the most produced genres are "Drama", "Documentary" and "Comedy" while having low return on investment.

<img src = "images/genres.png" width = 600 align = "middle">

* The calculation of correlation between average rating and runtime of the movie, shows that these two datasets are not related.

* The most profitable months for movie releasing are May, June, July, November. During these months tickets sales are high, because of the summertime, whereas in April, September, October and December are the least profitable times. The largest number of movies are released in December, due to holiday season.

<img src = "images/profit.png" width = 600 align = "middle">

* The most common content rating is "R" rating, which is movies for audience older than 17. The least produced ones are "G"- General Audience and "PG" - Parental Guidance Suggested. Large number of movies by "Netflix" have not been rated ("NR" - not rated).

<img src = "images/rating.png" width = 600 align = "middle">
***

## Conclusion

This analysis provides Microsoft with insight to movie industry on factors to consider increasing the chance of producing movies that will hit the top in cinematography. The following are the recommendations:

* It would be the most profitable for Microsoft to make movies in "Adventure, Animation, Comedy", "Action, Adventure, Sci-Fi", "Action, Adventure, Fantasy" and "Action, Adventure, Comedy", because they have highest return on investment and not the most produced genres. Thus, increasing the chances to get interest of audience.

* When producing movies, do not give extra attention to runtime, because the ratings are not correlated with length of movie.

* The most profitable months for movie release are May, June, July and November. Microsoft would hit highest ROI during these months. Also, it is recommended to avoid releasing in April, September, October and December, since profits are low during these times and December has the highest amount of releases.

* When choosing the content rating, it would be suggested to choose the most popular one, such that "R". Because it would have high chances to get interest of audience. Or choose the least produced one as a niche, which might be less competitive.



***

## Further Analysis

Modeling following analysis could give more detailed insights to Microsoft about the industry:

* **Study of relation between average rating and actors in the movie** could be helpful to strategize the casting for the movie
* **Comparing the profits from domestic gross and worldwide gross** will help to focus on proper audience and market
* **Analysis of movies based on critics rating and directors**, will help to identify which directors get the highest ratings from critics. 

***

## For More Information


Please review my full analysis in my [Jupyter Notebook](./Movie_Industry_Analysis_for_Microsoft.ipynb) or my [presentation](./Movie_Industry_Analysis.pptx).

For any additional questions, please contact **Aziza Gulyamova. Email: agulyamova14@gmail.com**
