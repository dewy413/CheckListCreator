import os
from colorama import just_fix_windows_console
just_fix_windows_console()

selection = -1


#class menu:


def readfile(file_loc):
	list = []
	file = open(file_loc, "r")
	lines = file.readlines()
	for line in lines:
		list.append(line):
	
	return list

red_text = lambda string: u"\u001b[31m" + string + u"\u001b[0m"
blue_text = lambda string: u"\u001b[34m" + string + u"\u001b[0m"
green_text = lambda string: u"\u001b[32m" + string + u"\u001b[0m"

red_back = lambda string: u"\u001b[41m" + string + u"\u001b[0m"
blue_back = lambda string: u"\u001b[44m" + string + u"\u001b[0m"
green_back = lambda string: u"\u001b[42m" + string + u"\u001b[0m"


string = "hello"
text = ""
while(selection != "end"):
	os.system('cls')
	print("1. Create a list\n2. Load a list\n")
	selection = input()
	if(selection = "1")
