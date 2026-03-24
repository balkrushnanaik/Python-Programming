from PyPDF2 import PdfWriter

try:
    merger = PdfWriter()

    pdfs = []

    n = int(input("Enter the number of files:\n"))

    for i in range(0, n):
        name = input(f"Enter the file name {i + 1}:\n")
        pdfs.append(name)

    for pdf in pdfs:
        merger.append(pdf)

    merger.write("merged-pdf.pdf")

    merger.close()
except Exception as e:
    print(e)