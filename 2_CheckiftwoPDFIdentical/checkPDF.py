from pdfComparer import pdfComparer

compare = pdfComparer("./2_CheckiftwoPDFIdentical/dummy.pdf",
                      "./2_CheckiftwoPDFIdentical/dummy2.pdf")
print(compare.comparer())
