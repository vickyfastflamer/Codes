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
merge_pdfs([r"C:\Users\vicky\Downloads\temp\re6(1).pdf",r"C:\Users\vicky\Downloads\temp\re6(2).pdf",r"C:\Users\vicky\Downloads\temp\re6.pdf",
r"C:\Users\vicky\Downloads\temp\RenewableExp6.pdf",
r"C:\Users\vicky\Downloads\temp\Report.pdf",
r"C:\Users\vicky\Downloads\temp\Report_2.pdf",
r"C:\Users\vicky\Downloads\temp\Report_3.pdf",
r"C:\Users\vicky\Downloads\temp\RenewableExp5.pdf"], 'merged_har.pdf')
print("the following pdfs are merged")
