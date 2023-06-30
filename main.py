import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Veri setini yükle
df = pd.read_csv('movie_dataset.csv')

# Karı hesapla
df['profit'] = df['revenue'] - df['budget']

# Tüm filmleri karlarına göre sırala
df_sorted = df.sort_values('profit', ascending=False)

# Karlarına göre filmleri görselleştir
plt.figure(figsize=(12, 8))
sns.barplot(x=df_sorted['profit'].head(10), y=df_sorted['title'].head(10))
plt.xlabel('Kar')
plt.ylabel('Film Başlığı')
plt.title('En Karlı Filmler')
plt.show()

# Bütçe ile gelir arasındaki ilişkiyi görselleştir
fig = px.scatter(df, x='budget', y='revenue', hover_data=['title'], title='Film Bütçesi ve Geliri Arasındaki İlişki')
fig.show()


"""import pandas as pd
import matplotlib.pyplot as plt

# Veri setini yükle
df = pd.read_csv('movie_dataset.csv')

# Karı hesapla
df['profit'] = df['revenue'] - df['budget']

# En karlı filmleri belirle
most_profitable_movies = df.sort_values('profit', ascending=False).head(10)

print("En karlı filmler:")
print(most_profitable_movies[['title', 'profit']])

# Bütçe ile gelir arasındaki ilişkiyi görselleştir
plt.figure(figsize=(10, 6))
plt.scatter(df['budget'], df['revenue'], alpha=0.5)
plt.title('Film Bütçesi ve Geliri Arasındaki İlişki')
plt.xlabel('Bütçe')
plt.ylabel('Gelir')
plt.show()
"""