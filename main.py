import arxiv
import PyPDF2
search = arxiv.Search(
    query="IEEE 2021",
    max_results=30
)

def check_space(string):
    count = 0
    for i in range(0, len(string)):
        if string[i] == " ":
            count += 1
    return count
# i=0
# for result in search.results():
#     result.download_pdf(dirpath="D:\PDFY", filename="paper{}.pdf".format(i))
#     i+=1
# print("Success")

# for x in range(30):
#     words = 1
#     filepath="D:\PDFY\paper{}.pdf".format(x)
#     f=open(filepath,"rb")
#     pdfReader = PyPDF2.PdfReader(f)
#     t = pdfReader.extractText()
#     e = len(t)
#     for y in t:
#         if y.isspace():
#             words+=1
#             e-=1
#     print("Znaki ze spacjami",len(t),
#     "\nZnaki bez spacji",e,
#     "\nWyrazy",words
#     )
for x in range(30):
    file = open(f"D:\\PDFY\\paper{x}.pdf", 'rb')
    ReadPDF = PyPDF2.PdfFileReader(f"D:\\PDFY\\paper{x}.pdf")
    pages = ReadPDF.numPages
    print(f"pdf {x}",pages)

    Tword = 0
    WText = ""
    for i in range(pages):
        pagesObj = ReadPDF.getPage(i)
        text = pagesObj.extractText()
        Tword+=len(text.split())
        WText = WText + text
    print(f"pdf {x}",Tword)
    string = WText
    print(check_space(string))
    # print(text.split())
    # print(pagesObj)
    # print(WText)

    # print(WText)
    print(len(WText))









