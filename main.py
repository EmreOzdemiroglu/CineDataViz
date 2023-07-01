import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv('movie_dataset.csv')

# Calculate profit
df['profit'] = df['revenue'] - df['budget']

# Sort all movies by their profit
df_sorted = df.sort_values('profit', ascending=False)

# Visualize movies by their profit
plt.figure(figsize=(12, 8))
sns.barplot(x=df_sorted['profit'].head(10), y=df_sorted['title'].head(10))
plt.xlabel('Profit')
plt.ylabel('Movie Title')
plt.title('Most Profitable Movies')
plt.show()

# Visualize the relationship between budget and revenue
fig = px.scatter(df, x='budget', y='revenue', hover_data=['title'], title='Relationship Between Movie Budget and Revenue')
fig.show()

# Calculate popularity score
df['popularity_score'] = df['popularity'] * df['vote_average'] * df['revenue'] * df['budget'] * df['vote_count']

# Determine the most popular movies
top_popular_movies = df.sort_values('popularity_score', ascending=False).head(10)

# Popularity score graph
fig = px.bar(top_popular_movies, x='original_title', y='popularity_score', 
             hover_data=['popularity', 'vote_average', 'revenue', 'budget', 'vote_count'], color='popularity_score',
             labels={'popularity_score':'Popularity Score', 'original_title':'Movie'},
             title='Most Popular Films')
fig.show()
