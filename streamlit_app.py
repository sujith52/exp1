import streamlit as st

st.title('Novel world')

st.write('Hello world!')

import subprocess
subprocess.run(['pip', 'install', 'beautifulsoup4', '--force-reinstall'])

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
            import pdfkit

# Specify the path to wkhtmltopdf
            config = pdfkit.configuration(wkhtmltopdf='/path/to/wkhtmltopdf')

# Generate PDF
            pdf = pdfkit.from_string(text, False, configuration=config)
            
            # Display the PDF
            st.download_button("Download PDF", pdf, "novel.pdf")
        else:
            st.write("Failed to retrieve the novel content")
    except Exception as e:
        st.write(f"Error: {e}")

#second phase
import streamlit as st
import pdfkit

# Generate HTML content
html = """
<html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
"""

# Render HTML content in Streamlit
st.markdown(html, unsafe_allow_html=True)

# Add jsPDF library to Streamlit
st.markdown('<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>', unsafe_allow_html=True)

# Generate PDF button
st.button("Generate PDF", key="generate_pdf")

# JavaScript code to generate PDF
pdf_js = """
<script>
  const generatePDF = () => {
    const doc = new jsPDF();
    const html = document.body.innerHTML;
    doc.fromHTML(html);
    doc.save('example.pdf');
  }
  document.querySelector('button[key="generate_pdf"]').addEventListener('click', generatePDF);
</script>
"""

# Add JavaScript code to Streamlit
st.markdown(pdf_js, unsafe_allow_html=True)

# Configure pdfkit
config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf')

# Generate PDF using pdfkit
pdf = pdfkit.from_string(html, False, configuration=config)

# Display PDF in Streamlit
st.download_button("Download PDF (pdfkit)", pdf, "example.pdf")
