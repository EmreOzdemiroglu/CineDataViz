# Comprehensive Film Analysis and Visualization Project

This project aims to provide an in-depth analysis and visualization of a movie dataset, exploring various aspects such as profitability, popularity, genre distribution, director success, and more. The dataset includes a wide range of movie attributes such as budget, genres, revenue, popularity, vote count, and more.

## Current Features
- Profit calculation for each movie in the dataset.
- Identification and listing of the most profitable movies.
- Visualization of the relationship between budget and revenue.
- Calculation of a popularity score for each movie, considering factors such as popularity, vote average, revenue, budget, and vote count.
- Identification and listing of the most popular movies based on the calculated popularity score.
- Visualization of the relationship between popularity and vote average.

## Future Features
In the future, this project will be expanded to include the following analyses:

- Genre Analysis: Using the genre information of the movies, the most popular movie genres will be determined and the popularity of genres over time will be analyzed.
- Director Analysis: Using the director information of the movies, the directors who have made the most films or generated the highest revenue will be identified.
- Time Series Analysis: Using the release date information of the movies, various attributes (such as budget, revenue, popularity, vote average) will be analyzed for changes over time.
- Language Distribution and Genre Popularity: Histograms and bar graphs will be created according to the original languages and genres of the movies, showing which languages and genres produce and are popular in the most films.
- Revenue Over the Years: A line graph showing total revenue by release date (year) can be created. This will show which years were the most profitable over time.
- Relationship Between Vote Average and Vote Count: A scatter plot showing the relationship between vote average and vote count can be created. This will show whether a higher vote count is associated with a higher vote average.
- Success of Directors: A bar graph showing the top 10 directors who have generated the most revenue can be created. This will show which directors are the most profitable.

## Usage
The main script can be run with a dataset in CSV format. The dataset should include columns for 'budget', 'revenue', 'title', 'popularity', 'vote_average', and 'vote_count' at a minimum. The script will calculate the profit and popularity score for each movie, sort the movies by profit and popularity, and then create visualizations.

## Dependencies
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly

## Installation
To install the necessary libraries, you can use pip:

```
pip install pandas matplotlib seaborn plotly
```

## Dataset Source

The dataset used in this project is sourced from Kaggle, a popular platform for data science competitions and datasets. The specific dataset used can be found at the following link: [Movies Dataset](https://www.kaggle.com/datasets/utkarshx27/movies-dataset). It includes a wide range of movie attributes such as budget, genres, revenue, popularity, vote count, and more.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
