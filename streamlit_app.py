# Novel Website
## Import Libraries
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pdfkit

## App Title
st.title("Novel Reading Website")

## Novel Link Input
novel_link = st.text_input("Enter the novel link")

## Generate PDF Button
if st.button("Generate PDF"):
    try:
        response = requests.get(novel_link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text = soup.get_text()
            config = pdfkit.configuration(wkhtmltopdf='D:\\startup\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            pdf = pdfkit.from_string(text, False, configuration=config)
            st.download_button("Download PDF", pdf, "novel.pdf")
        else:
            st.write("Failed to retrieve the novel content")
    except Exception as e:
        st.write(f"Error: {str(e)}")

# HTML Content
## Generate HTML Content
html_content = """
<html>
  <body>
    <h1>Hello, World!</h1>
  </body>
</html>
"""

## Render HTML Content in Streamlit
st.markdown(html_content, unsafe_allow_html=True)

## Add jsPDF Library to Streamlit
st.markdown('<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>', unsafe_allow_html=True)

## Generate PDF Button
st.button("Generate PDF", key="generate_pdf")

## JavaScript Code to Generate PDF
pdf_js = """
<script>
  const generatePDF = () => {
    const doc = new jsPDF();
    const html = document.querySelector('body > h1').innerHTML;
    doc.fromHTML(html);
    doc.save('example.pdf');
  }
  document.querySelector('button[key="generate_pdf"]').addEventListener('click', generatePDF);
</script>
"""

## Add JavaScript Code to Streamlit
st.markdown(pdf_js, unsafe_allow_html=True)

## Generate PDF using pdfkit
config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf')
pdf = pdfkit.from_string(html_content, False, configuration=config)

## Display PDF in Streamlit
st.download_button("Download PDF (pdfkit)", pdf, "example.pdf")
