import streamlit as st

st.title('Novel world')

st.write('Hello world!')

import streamlit as st

# App title
st.write("Novel Website")

# Introduction
st.write("Welcome to our novel website!")

# Novel chapters
chapters = {
    "Chapter 1": "Chapter 1 content",
    "Chapter 2": "Chapter 2 content",
    "Chapter 3": "Chapter 3 content"
}

# Select chapter
chapter = st.selectbox("Select a chapter", list(chapters.keys()))

# Display chapter content
st.write(chapters[chapter])

# Author information
st.write("Author: [Your Name]")

# Contact information
st.write("Contact: [Your Email]")

# Social media links
st.write("Follow us on social media:")
st.write("[Twitter](https://twitter.com/your_twitter_handle)")
st.write("[Facebook](https://facebook.com/your_facebook_page)")
