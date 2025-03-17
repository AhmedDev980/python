# Provide the folder name as input and get the list of files in the particular folder as output

import os
# .split() is used to convert the folder names into list
folders = input("Enter the folder names:" ).split()

for folder in folders:
 try:
   files = os.listdir(folder)
 except FileNotFoundError:
  print ("Please provide the valid folder name. Looks loke this folder does not exist:" + folder )
  break
 # if we want to stop and comeout of the program after facing error we can provide break, if want to proceed with next folder names provide continue
 print("The list of files in the folder:" +folder )
 for file in files:
    print(file)
