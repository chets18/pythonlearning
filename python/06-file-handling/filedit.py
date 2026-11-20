"""
with open("/home/chetraj/clone/nimasa-website-demo/Education consultancy.txt", "r") as file:
    reads=file.read()
print(reads)


"""

#let access how many files are there in our download folder only using python program 
from pathlib import Path 
file_open = Path.home() / "Downloads"

print(file_open)
for file in file_open.iterdir():   #path.iterdir() is a method used to loop through and list all files and subdirectories inside a specific folder
    print(file.name)
    print(file.suffix)
    

#However, it only looks one level deep. It will show you the folders sitting directly inside the main folder, but it will not look inside those folders to see what is inside them.


# if you want to look inside subfolders

from pathlib import Path

main_folder = Path.home() / "Downloads" #this is just example you can put any folder path here 

# This will find absolutely everything, even deep inside subfolders
for item in main_folder.rglob("*"):
    print(item)
