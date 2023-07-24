import PyPDF2
import sys

# Function to extract text
def extract_text_from_pdf(file_path, keywords):
    pdf_file = open(file_path, 'rb')
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text = page.extract_text()
        search_keywords_in_text(text, keywords, page_num)
    pdf_file.close()
    return text

# Function to search text for keywords
def search_keywords_in_text(text, keywords, page_num):
    lines = text.split('\n')
    for line_num, line in enumerate(lines, start=1):
        for keyword in keywords:
            if keyword.lower() in line.lower():
                print(f'Page {page_num+1}: {line}')
                break

# Command-line arguments
file_path = sys.argv[1]
keywords = sys.argv[2:]

extract_text_from_pdf(file_path, keywords)
