import os
import pathlib
import argparse
from PyPDF2 import PdfFileMerger

parser = argparse.ArgumentParser(description='Append PDF files in a directory.')
parser.add_argument('-p',metavar='--path',help='path to target dirctory, default=current directory', type=str, nargs=1, default=[pathlib.Path(__file__).parent.absolute()])
parser.add_argument('-t', help='flag for order by time created, default=False', action="store_true", default=False)
parser.add_argument('-desc', help='flag for descending order, default=False', action="store_true", default=False)

args = parser.parse_args()

directory = args.p[0]

merger = PdfFileMerger()

order_by = os.path.getmtime if args.t else str

for e in sorted(os.listdir(directory), reverse = args.desc ):
    if e[-3:] == "pdf":
        merger.append(str(directory)+"/"+e)

merger.write("result.pdf")
merger.close()

print("Done!\U0001f600")

