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

# Fill NaN with 'Unknown' and convert to string
df['genres'] = df['genres'].fillna('Unknown').astype(str)

# Now apply the split operation
df['genres'] = df['genres'].apply(lambda x: x.split(','))

# Convert release_date to datetime
df['release_date'] = pd.to_datetime(df['release_date'])

# Explode the dataframe on genres
df_exploded = df.explode('genres')

# Calculate the top 10 genres
top_10_genres = df_exploded['genres'].value_counts().head(10).index.tolist()

# Filter the dataframe to include only the top 10 genres
df_top_10_genres = df_exploded[df_exploded['genres'].isin(top_10_genres)]

# Group by genres and year, then count the number of movies
genre_popularity = df_top_10_genres.groupby([df_top_10_genres['release_date'].dt.year, 'genres']).size().reset_index(name='counts')

# Pivot the data for visualization
genre_popularity_pivot = genre_popularity.pivot(index='release_date', columns='genres', values='counts').fillna(0)

# Plot the data
plt.figure(figsize=(10, 8))
for genre in genre_popularity_pivot.columns:
    plt.plot(genre_popularity_pivot.index, genre_popularity_pivot[genre], label=genre)
plt.legend()
plt.xlabel('Year')
plt.ylabel('Number of Movies')
plt.title('Popularity of Top 10 Genres Over Time')
plt.show()
