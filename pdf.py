import PyPDF2

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfReader(r"" + path)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output, 'wb') as out:
        pdf_writer.write(out)

# Example usage:
merge_pdfs([r"path of file1.pdf", r"path of file2.pdf", r"path of file3.pdf"], 'merged.pdf')
print("the following pdfs are merged")
