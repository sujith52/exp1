import streamlit as st
import requests
from bs4 import BeautifulSoup

# Novel page link
novel_page_link = "https://lightnovel.novelupdates.net/book/emperors-domination/chapter-1"

# Send a GET request to the novel page
response = requests.get(novel_page_link)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the text container on the page
text_container = soup.find('div', {'class': 'text-container'})

# Extract the text from the container
text_container = soup.find('div', {'class': 'text-container'})
if text_container is None:
    st.write("Unable to find text container on the page.")
else:
    text = text_container.get_text()
    st.write(text)


