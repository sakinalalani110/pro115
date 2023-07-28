#For renaming the existing file
#os stands for "Operating System" in Python. 
#It is a built-in module that provides a way to interact with the underlying operating system.

#import os - step 1
import os

#give src. and destn. files path for renaming the existing file
source = "/Users/sakinalalani/Desktop/document_files/document_files/main.txt"
destination = "/Users/sakinalalani/Desktop/document_files/document_files/newfile.txt"

#finally rename them
os.rename(source, destination)