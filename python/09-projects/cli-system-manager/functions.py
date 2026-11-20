import subprocess

class see:
    pass

class edit:
    pass

# see how much storage is left, used
class Storage(see):
    def run():
        choose = {1 : "RAM", 2 : "Overall"}
        for keys, value in choose.items():
            print(f"{keys}. {value}")
        store = int(input("Pick one: "))
        
        if store == 1: 
            result = subprocess.run("free -h", capture_output=True, text = True)
            total, used, free, percent = result.stdout.splitlines()[1].split()[1:5]
            print(f"Total disk: {total}\nDisk used: {used}\nDisk available: {free}\nDisk usage: {percent}")
        if store == 2:
            result = subprocess.run(["df" ,"-h"], capture_output=True, text = True)
            total, used, free, percent = result.stdout.splitlines()[1].split()[1:5]
            print(f"Total disk: {total}\nDisk used: {used}\nDisk available: {free}\nDisk usage: {percent}")


#see what's the size of a folder
class FolderSize(see):
    def run(self):
        FileName = input("Enter the file you want to know size of")
        subprocess.run("du -h "+FileName,shell=True,check=True)

class TaskManager(see):
    def run(self):
        subprocess.run("top",shell=True,check=True)

class Date(see):
    def run(self):
        subprocess.run("date", shell=True, check=True)

class DigitalWellbeing(see):
    def run(self):
        subprocess.run("")

class FindFile(see):
    def run(self):
        FileName = input("Enter the file name")
        subprocess.run("find / -name "+FileName,shell=True,check=True)
    def FindNumber(self):
        FileExtention = input("Enter file extention (e.g. pdf, mp4, .png etc.)")
        if "." in FileExtention:
            FileExtention = FileExtention[1:]
            subprocess.run("")

class FileArrangement(edit):
    def run(self):
        FileExtention = input("Enter the file extention you want to move")
        FolderName = input("Enter the folder name you want to move in.")
        subprocess.run(" ")
