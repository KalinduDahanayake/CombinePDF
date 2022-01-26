from msilib.schema import File
import os
from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()

os.chdir('C:/Users/Kalindu/Desktop/CombinePDF/FilestoCombine')

path, dirs, files = next(os.walk('C:/Users/Kalindu/Desktop/CombinePDF/FilestoCombine'))

for filename in os.listdir('.'):
       if filename.endswith('.pdf'):
           mergedObject.append(filename)

# Write all the files into a file which is named as shown below
os.chdir('C:/Users/Kalindu/Desktop/CombinePDF')
mergedObject.write("CombinedPDF.pdf")