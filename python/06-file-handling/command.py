import subprocess

subprocess.run(["df", "-h"])

#alternative 

#cmd = input("free -h")

subprocess.run(["free", "-h"])


#now, i want more centric answer


r = subprocess.run(["df", "-h", "/"], capture_output=True, text=True)
total, used, free, percent = r.stdout.splitlines()[1].split()[1:5]

print(f"Total disk: {total}\nDisk used: {used}\nDisk available: {free}\nDisk usage: {percent}")

#stdout means standard output not standout, and without capture_output and text being true it'll not return exact terminal output in string and won't strong the value in r.stdout 