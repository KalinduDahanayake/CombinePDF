import os
import tkinter
from PyPDF2 import PdfFileMerger
from tkinter import messagebox

noPages = 0

val = input("What would you like to call your PDF: ")

# Call the PdfFileMerger
mergedObject = PdfFileMerger()

# Change directory to folder containing PDFs to be combined
os.chdir('C:/Users/Kalindu/Desktop/CombinePDF/FilestoCombine')

for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
           mergedObject.append(filename)
           noPages += 1

# Write all the files into a file which is named as shown below
os.chdir('C:/Users/Kalindu/Desktop/CombinePDF')

if noPages > 0:
    mergedObject.write(str(val) + ".pdf")
else:
    messagebox.showerror("Error", "No pages given. \nPlace PDF to combine in the FilestoCombine Folder.")