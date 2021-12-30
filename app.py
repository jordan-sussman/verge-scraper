import requests
from bs4 import BeautifulSoup

# Good soup
webpage = requests.get('https://www.theverge.com') # Get HTML from page
soup = BeautifulSoup(webpage.content, 'html.parser') # Parse content

# Refine the soup
data = soup.select("#content > div.l-hero > div > div > div > div > h2") # Select all articles with titles
first10 = data[:10] # Max 10 article limit

# Loop through refined soup
for article in first10:
    url = article.find('a', href=True) # Parse url from refined soup data
    print("Title:", article.text, "\n" "Link:", url['href'], "\n") # Display each article's title and link
