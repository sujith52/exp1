import streamlit as st

st.title('Novel world')

st.write('Hello world!')

import subprocess
subprocess.run(['pip', 'install', 'beautifulsoup4', '--force-reinstall'])
pip install pdfkit
# Import necessary libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pdfkit

# App title
st.title("Novel Reading Website")

# Novel link input
link = st.text_input("Enter the novel link")

# Generate PDF button
if st.button("Generate PDF"):
    try:
        # Send a GET request to the link
        response = requests.get(link)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract the text from the HTML content
            text = soup.get_text()
            
            # Generate PDF
            pdf = pdfkit.from_string(text, False)
            
            # Display the PDF
            st.download_button("Download PDF", pdf, "novel.pdf")
        else:
            st.write("Failed to retrieve the novel content")
    except Exception as e:
        st.write(f"Error: {e}")
