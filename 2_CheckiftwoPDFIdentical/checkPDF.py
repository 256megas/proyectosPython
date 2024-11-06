from pdfComparer import PdfComparer

compare = PdfComparer("./2_CheckiftwoPDFIdentical/dummy.pdf",
                      "./2_CheckiftwoPDFIdentical/dummy2.pdf")
print(compare.comparer())
