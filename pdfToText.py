from PyPDF2 import PdfReader
file_read = "30-07-2021.pdf"
file_write = "2021 7 bond.txt"
reader = PdfReader(file_read)
text = ""
for page in reader.pages:
    text += page.extract_text()+"\n"
with open(file_write,"w") as file:
    file.write(text)

