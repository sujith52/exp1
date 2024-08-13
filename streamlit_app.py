import streamlit as st
import requests
from bs4 import BeautifulSoup

# Create a title for your app
st.title("Novel Text Extractor")

# Create an input bar to take the novel link
novel_page_link = st.text_input("Enter the novel page link:")

# Create a button to display the text
if st.button("Extract Text"):
    # Send a GET request to the novel page
    response = requests.get(novel_page_link)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the text container on the page
    text_container = soup.find('div', {'class': 'chapter-content'})

    # Extract the text from the container
    if text_container is None:
        st.write("Unable to find text container on the page.")
    else:
        text = text_container.get_text()
        st.write(text)
