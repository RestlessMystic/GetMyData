import os
import subprocess

PATH = os.getcwd()

def extract(filename):
	FILENAME = "unyaffs.exe " + "\"" + filename + "\""
	subprocess.call(FILENAME)
	return(os.getcwd())

def inputfile():
	file1 = raw_input("Enter Filename : ")
	filename = os.path.join(PATH, file1)
	return filename
