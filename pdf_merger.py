import os
import sys

from PyPDF2 import PdfFileMerger

directory = sys.argv[1]

merger = PdfFileMerger()

for e in sorted(os.listdir(directory)):
    if e[-3:] == "pdf":
        merger.append(directory+"/"+e)

merger.write("result.pdf")
merger.close()

print("Done!\U0001f600")

