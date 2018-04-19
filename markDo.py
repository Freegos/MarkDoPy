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
#	* read random headers
#	* add summary (pdf)/menu (html)


import argparse
import re

def header(file):
	#Arg : file object unread (cursor still is on first line)
	#Return headers in indexed list
	headers = {'title': 'Unknow', 'date':'Unknow', 'author':'Unknow'}
	for l in file:
		if l[0] == "@":
			headers[l.split()[0][1:-1]] = ' '.join(l.split()[1:])
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
print("Analysing \"" + headers['title'] + "\" by " + headers['author'] + " the " + headers['date'])

outputFile.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>"""+ str(headers['title'])+"""</title>
	<meta name="author" content=" """ + str(headers['author']) + """ ">
</head>
<body>""")

#Prepare regex
#Title tag
h1 = re.compile('^#{1}([.^#]*)')		# Must be fixed
h2 = re.compile('^#{2}?([A-z0-9])')

for line in inputFile:
	tmp = h1.match(line)
	if tmp:
		print(tmp.group(1))
		line = "<h1>" + tmp.group(0) + "</h1>\n"
	
	outputFile.write(line)


#inputFile.readline()


outputFile.write("""</body>
	<html>""")

print("Saving")

# Closing files is fun
inputFile.close()
outputFile.close()

print("Done. Thank you for you use of markDoPy.")
print("This funny app was presented by Adrien Albaladejo")
