import sys
import os
# from spire.doc import *
# from spire.doc.common import *
from docx2pdf import convert

def convertToPdf(PathIn, PathOut):
    # Check if the input file exists
    if not os.path.exists(PathIn):
        print("File not found: " + PathIn)
        return
    
    # Check if the output file exists, remove it if it does
    if os.path.exists(PathOut):
        os.remove(PathOut)
    
    # # Create a Document object
    # document = Document()
    
    # # Load a Word DOCX file from path
    # document.LoadFromFile(PathIn)

    # # Save the file to a PDF file
    # document.SaveToFile(PathOut, FileFormat.PDF)
    # document.Close()
    
    # Convert the file to PDF using the docx2pdf library (https://pypi.org/project/docx2pdf/)
    # Note: This library requires the use of the Microsoft Word application
    convert(PathIn, PathOut)
    
if __name__ == "__main__":
    pathIn = sys.argv[1]
    pathOut = sys.argv[2]
    convertToPdf(pathIn, pathOut)