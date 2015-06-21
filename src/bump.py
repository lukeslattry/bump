#!/usr/bin/env python3

# Bump 0.1
# A simple, single command to open a web project in sublime text and your default browser.

from sys import argv, exit
from subprocess import call
import os.path
from os import listdir

packagePath = ""
openAll = False

if argv[1] == "-a" :
	packagePath = argv[2]
	openAll = True
else :
	packagePath = argv[1]

if packagePath != "" :
	call( ["subl", "%s" % ( packagePath )] )
	if os.path.isfile( "%s/index.html" % ( packagePath ) ) :
		call( ["open", "%s/index.html" % ( packagePath )] )

if openAll :
	for file in os.listdir( "%s" % ( packagePath ) ) :
		if file.endswith( ".html" ) :
			call( ["open", "%s/%s" % ( packagePath, file )] )