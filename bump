#!/usr/bin/env python3

# Bump 0.2
# A simgle, simple command to open your web projects in sublime text and your default browser

from sys import argv, exit
from subprocess import call
import os.path
from os import listdir

package = ""
packagePath = ""
openAll = False
openBrowser = True
openSublime = True

if argv[1][0] != "-" :
	package = argv[1]

else :
	if "a" in argv[1] :
		openAll = True
	
	if "b" in argv[1] :
		openSublime = False
	
	if "s" in argv[1] :
		openBrowser = False
	
	package = argv[2]

packagePath = package

if packagePath != "" and openSublime :
	call( ["subl", "%s" % ( packagePath )] )

if openBrowser :
	if os.path.isfile( "%s/index.html" % ( packagePath ) ) :
		call( ["open", "%s/index.html" % ( packagePath )] )

if openAll and openBrowser :
	for file in os.listdir( "%s" % ( packagePath ) ) :
		if file.endswith( ".html" ) :
			call( ["open", "%s/%s" % ( packagePath, file )] )
