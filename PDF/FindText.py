import PyPDF2, os

path = str(input("Please provide path of the PDF file you which to process: \n"))

try:
    if os.path.exists(path):
        os.chdir(path)
except Exception as e:
    print(e)

files =[]
for root, subfolder, filename in os.walk(path):
    files.append(str(filename))

pdf = []
for file in files:
    if file.endswith(".pdf"):
        index = str(files.index(file)+1)
        print(index + ". " + str(file))
        pdf.append(file)

if not pdf:
    print("There is no pdf in the given path")
    exit
else:
    while True:
        try:
            select_ind = int(input("Which file would you like to search (Enter only number!):\n"))
        except (ValueError):
            print("Sorry, numbers only.")
            continue

        if select_ind <= 0 or select_ind > len(pdf):
            print("Please select a number on the list")
        else:
            break

    select_pdf = pdf[select_ind+1]

search = input("Search phrase:\n")
pdf_file = open(select_pdf, "rb")
pdf_obj = PyPDF2.PdfFileReader(pdf_file)

for page in range(pdf_obj.getNumPages()):
    page_obj = pdf_obj.getPage(page)
    text = page_obj.extractText()

    if search in text:
        print("Found keyword on page" + str(page))