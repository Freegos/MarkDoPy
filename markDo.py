#!/usr/bin/python3

# author: Adrien Albaladejo

# Parse arguments
# Open source file
# Open output file
# Write html header
# Read each line of source file and parse them
# When a specific symbol is find (list?), line is send to function who edit it and add html tags
# The line is added to html file
# Write html end + close 2 files
# TADA

# TO-DO (v2):
#	* read other headers


import argparse

def header(file):
	#Arg : file openned without having been read
	#Return headers in list ù
	headers = {'title': 'Unknow', 'date':'Unknow', 'author':'Unknow'}
	for l in file:
		if l[0] == "@":
			headers[l.split()[0][1:-1]] = l.split()[1]
		else:
			break
	
	return headers




print("Welcome in markDoPy, a Python3 mark down interpreter for fun (please have fun reading that!)")
print("Initializing...")

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("input", help="Markdown file to treat (my_mark_down_file.mk)")
parser.add_argument("output", help="Filename for html file which will be created (example.html)")
args = parser.parse_args()
print("Input file is: " + args.input)
print("Output file is going to be: " + args.output)


# Open files
inputFile = open(args.input, 'r')
outputFile = open(args.output, 'w')
print("Files open or created")

headers = header(inputFile)

outputFile.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>"""+ str(headers[title])+"""</title>
	<meta name="author" content=" """ + str(headers[author]) + """ ">
</head>
<body>""")

for line in inputFile:
	print(line)

#inputFile.readline()


outputFile.write("""</body>
	<html>""")

# Closing files is fun
inputFile.close()
outputFile.close()
