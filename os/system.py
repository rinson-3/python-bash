# os module used to work with files and directories

import os
import datetime

os.remove("novel.txt") # to remove the .txt file

os.rename("first.txt", "final.txt") # to rename the .txt file

print(os.path.exists("final.txt"))   # to check if the .txt file exists

print(os.path.getsize("spider.txt"))  # to check the filesize in bytes

print(os.path.getmtime("spider.txt"))   # to check last modified time (unix timestamp)

print(os.path.abspath("spider.txt"))   # to show the absolute path of the file

timestamp=os.path.getmtime("spider.txt")
print(datetime.datetime.fromtimestamp(timestamp))

print(os.getcwd())

os.mkdir("new_dir")  # create a new directory

os.chdir("new_dir")   # change to a new directory
print(os.getcwd())

os.rmdir("new_dir")   # remove a directory

print(os.listdir("google")) # lists the contents in a directory


# to check if the files in the google folder is a file or a folder 
dir="google"
for name in os.listdir(dir):
    fullname=os.path.join(dir, name)  # join function helps us to be independent of the OS. In linux and macOS its / but in windows its \
    if os.path.isdir(fullname):
        print(f"{fullname} is a directory")
    else:
        print(f"{fullname} is a file")