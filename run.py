import os
from PyPDF2 import PdfFileMerger, PdfFileReader
 
# Call the PdfFileMerger
mergedObject = PdfFileMerger()

os.chdir('C:/Users/Kalindu/Desktop/CombinePDF/FilestoCombine')

path, dirs, files = next(os.walk('C:/Users/Kalindu/Desktop/CombinePDF/FilestoCombine'))
file_count = len(files)

# Loop through all of them and append their pages
for fileNumber in range(1, file_count+1):
    mergedObject.append(PdfFileReader('test_' + str(fileNumber)+ '.pdf', 'rb'))
 
# Write all the files into a file which is named as shown below
os.chdir('C:/Users/Kalindu/Desktop/CombinePDF')
mergedObject.write("CombinedPDF.pdf")