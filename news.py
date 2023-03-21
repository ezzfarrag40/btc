import os
import csv
from newsapi import NewsApiClient

# Set your API key here
api_key = '0442b51d7fd848d08f67363326b37d7f'

# Initialize the News API client
newsapi = NewsApiClient(api_key=api_key)

# Set the search query parameters
query = 'bitcoin'
from_date = '2022-01-01'
to_date = '2022-03-31'

# Fetch the news articles from the API
articles = newsapi.get_everything(q=query, from_param=from_date, to=to_date)

# Extract the relevant fields from each article
data = []
for article in articles['articles']:
    title = article['title']
    description = article['description']
    url = article['url']
    published_at = article['publishedAt']
    data.append([title, description, url, published_at])

# Save the data to a CSV file
filename = 'news_data.csv'
if os.path.exists(filename):
    mode = 'a'
else:
    mode = 'w'
with open(filename, mode, newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    if mode == 'w':
        writer.writerow(['title', 'description', 'url', 'published_at'])
    writer.writerows(data)
