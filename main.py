import arxiv
import PyPDF2
import matplotlib.pyplot as plt
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
lhight = []
lleft = []
left = []
height = []
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
    lhight.append(Tword)
    lleft.append(x)
    left.append(len(WText))
    height.append(x)
    # print(text.split())
    # print(pagesObj)
    # print(WText)

    # print(WText)
    print(len(WText))
    # print(lword)
# tick_label = []
plt.bar(lleft, lhight, tick_label = lleft, width=0.8, color = ["green", "red"])
plt.xlabel('Artukuły')
plt.ylabel('Ilość słów')
plt.show()


# print(left[1])

# tick_label1=[]

# plt.subplot(131)
# plt.bar(height,left,tick_label=lleft,width=0.3)
# plt.xlabel('')
# plt.ylabel('ilość')
# plt.suptitle('Ilość znaków w artykule')
#
#
# plt.show()

















