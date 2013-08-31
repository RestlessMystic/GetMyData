import subprocess
import os

PATH = os.getcwd()
FILENAME = os.path.join(PATH, raw_input("Enter filename : "))
FILENAME = "unyaffs.exe " + "\"" + FILENAME + "\""
print FILENAME
subprocess.call(FILENAME)