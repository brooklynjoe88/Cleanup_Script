import os
import datetime

#Replace File_Path with the location of the file E.G. c:/users/you/old_files
directory = r'File_Path'
today = datetime.datetime.today()

# Prints all file names in a directory
#for file in os.scandir(directory):
#    print(file)

# Display each file older than 30 days and ask if user wants it delete it.
for file in os.scandir(directory):

    t = os.stat(file)[8]
    age = datetime.datetime.fromtimestamp(t) - today

    if age.days <= -30:
        print(str(file) + " is " + str(age.days) + " days old.")
        question = input("Delete file? (Y/N):")
        if question == "Y" or question == "y":
            os.remove(file)
            print("File deleted")
        elif question == "N" or question == "n":
            print("File will not be deleted")
        else:
            print("Input does not match. Going to next file")

