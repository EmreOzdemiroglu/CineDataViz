# CineDataViz - A Comprehensive Movie Dataset Analysis

CineDataViz is a data analysis project focused on exploring and understanding a comprehensive movie dataset. The dataset includes various details about movies, such as budget, revenue, genres, director, release date, original language, vote average, and vote count.

This project provides a detailed analysis of the dataset using various data analysis techniques and visualizations. It aims to uncover patterns, trends, and relationships within the data, providing valuable insights into the movie industry.

## Dependencies
- Python
- Pandas
- Matplotlib
- Plotly
- Numpy

## Installation
To install the necessary libraries, you can use pip:

```
pip install pandas matplotlib numpy plotly

```
## How to Use

1. Clone this repository to your local machine.

2. Open the Jupyter notebook (`cinedataviz.ipynb`) in a Jupyter environment (like JupyterLab or Jupyter Notebook).

3. Run all the cells in the notebook to see the results of the analysis.



## Features

1. **Profit Calculation**: Calculates the profit for each movie in the dataset by subtracting the budget from the revenue.

2. **Most Profitable Movies**: Identifies and lists the most profitable movies in the dataset.

3. **Budget vs Revenue Visualization**: Creates a scatter plot to visualize the relationship between the budget of a movie and the revenue it generates.

4. **Popularity Score Calculation**: Calculates a popularity score for each movie, considering factors such as popularity, vote average, revenue, budget, and vote count.

5. **Most Popular Movies**: Identifies and lists the most popular movies based on the calculated popularity score.

6. **Popularity vs Vote Average Visualization**: Creates a scatter plot to visualize the relationship between the popularity of a movie and its vote average.

7. **Genre Analysis**: Performs genre analysis by extracting the genre information for each movie, calculating the popularity of each genre, and analyzing the popularity of genres over time.

8. **Director Analysis**: Performs director analysis by extracting the director information for each movie and identifying the directors who have made the most films or generated the highest revenue.

9. **Time Series Analysis**: Performs time series analysis by using the release date information of the movies and analyzing various attributes (such as budget, revenue, popularity, vote average) for changes over time.

10. **Language Distribution and Genre Popularity**: Creates histograms and bar graphs to show the distribution of original languages and genres of the movies, and analyzes which languages and genres produce and are popular in the most films.

11. **Revenue Over the Years**: Creates a line graph showing total revenue by release date (year) to visualize which years were the most profitable over time.

12. **Relationship Between Vote Average and Vote Count**: Creates a scatter plot showing the relationship between vote average and vote count to analyze whether a higher vote count is associated with a higher vote average.

13. **Success of Directors**: Creates a bar graph showing the top 10 directors who have generated the most revenue to identify which directors are the most profitable.

14. **Creation of More Complex Graphs**: Creates more complex graphs that provide deeper insights into the data.

15. **Dashboard Creation**: Creates a dashboard that presents all the visualizations and analyses in a user-friendly manner.

# Future Features for CineDataViz

1. **Movie Recommendation System**: Implement a movie recommendation system based on different parameters such as genre, director, actors, and user ratings. This could provide personalized movie recommendations to users based on their past viewing history and preferences.

2. **Sentiment Analysis of Movie Reviews**: Incorporate a sentiment analysis component that analyzes movie reviews to determine the overall audience sentiment towards a movie. This could provide additional insights into a movie's reception beyond numerical ratings.

3. **Box Office Prediction**: Develop a machine learning model to predict a movie's box office performance based on features such as budget, genre, director, and cast. This could be a valuable tool for producers and investors.

4. **Dashboard Enhancement**: Enhance the dashboard with additional interactive features such as filters, dropdowns, and sliders that allow users to customize the visualizations based on their interests. 

5. **Actor Analysis**: Similar to the director analysis, perform an actor analysis to identify the actors who have been in the most films or generated the highest revenue. 

6. **Movie Era Comparison**: Compare different eras of film (e.g., silent era, golden age, modern era) in terms of revenue, budget, genres, directors, and actors. 

7. **Geographical Analysis**: If data is available, perform a geographical analysis to visualize the revenue or popularity of movies in different countries or regions.

8. **Integration with External Databases**: Integrate the application with external databases or APIs to fetch real-time data or additional data that is not present in the current dataset.

9. **User Account and Authentication System**: Implement a user account and authentication system that allows users to save their preferences, bookmark their favorite movies, and share their views or reviews.

10. **Movie Trivia**: Include interesting trivia or facts about movies, which could make the application more engaging for users.

## Dataset Source

The dataset used in this project is sourced from Kaggle, a popular platform for data science competitions and datasets. The specific dataset used can be found at the following link: [Movies Dataset](https://www.kaggle.com/datasets/utkarshx27/movies-dataset). It includes a wide range of movie attributes such as budget, genres, revenue, popularity, vote count, and more.

## Contributions

Contributions to this project are welcome. If you find a bug or think of a feature that would be nice to have, please open an issue. If you want to contribute code, please open a pull request.

## Contact

If you have any questions, feedback, or suggestions, please open an issue or send an email to `ozdemirogluemre@gmail.com`.

## Acknowledgments

This project was inspired by the desire to understand the movie industry better and to apply data analysis techniques to a real-world dataset. Thanks to all the contributors who have helped improve this project.


## License
[MIT](https://choosealicense.com/licenses/mit/)
