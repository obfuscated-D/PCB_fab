import PyPDF2
import sys
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def save_text_to_file(text, output_path):
    with open(output_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

def convert_pdf_to_text(pdf_path, output_path):
    text = extract_text_from_pdf(pdf_path)
    save_text_to_file(text, output_path)


def main(pdf_path, output_path):
    if not os.path.isfile(pdf_path):
        print(f"Error: The path {pdf_path} is not a file.")
        return
    if not os.path.isdir(os.path.dirname(output_path)):
        print(f"Error: The directory {os.path.dirname(output_path)} does not exist.")
        return
    if os.path.isfile(output_path):
        print(f"Warning: The file {output_path} already exists and will be overwritten.")   
    if not os.path.exists(pdf_path):
        
        print(f"Error: The file {pdf_path} does not exist.")
        return
    if not pdf_path.lower().endswith('.pdf'):
        print(f"Error: The file {pdf_path} is not a PDF.")
        return
    if os.path.exists(output_path):
        print(f"Warning: The file {output_path} already exists and will be overwritten.")
    convert_pdf_to_text(pdf_path, output_path)




path = sys.argv[1]
output_path = sys.argv[2]
main(path, output_path)
