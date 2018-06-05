#!/usr/bin/env python

"""
MIT License

Copyright (c) 2018 Bryan Angelo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os, shutil, time

while 1:
	# input
	drive = raw_input("Enter USB device drive letter to be repaired: ").split(":")[0]
	
	# if device drive is mounted.
	print("Checking input...")
	if os.path.exists("{0}:\\".format(drive)):
		# check if RECYCLER path exists.
		print("Searching RECYCLER path...")
		if os.path.exists("{0}:\\RECYCLER".format(drive)):
			# remove RECYCLER path and all of its contents.
			# we should, because it's a waste of space.
			shutil.rmtree("{0}:\\RECYCLER".format(drive))
			print("RECYCLER removed sucessfully!")
		else:
			print("no RECYCLER path found...")
		
		# check if autorun.inf file exists.
		print("Searching autorun.inf file...")
		if os.path.exists("{0}:\\autorun.inf".format(drive)):
			# remove "autorun.inf".
			# we should, because it's a waste of space (1)
			os.remove("{0}:\\autorun.inf".format(drive))
			print("autorun.inf removed sucessfully!")
		else:
			print("no autorun.inf file found...")
		
		# list all microsoft link file.
		# os.system("del *.lnk") :"V
		print("Removing *.lnk files...")
		
		# link files count
		countlnkfiles = 0
		for files in os.listdir("{0}:\\".format(drive)):
			
			# check if it has ".lnk".
			if files[-4:] == ".lnk":
				
				# remove ".lnk" file.
				# we should, because it's a waste of space (2)
				os.remove("{0}:\\{1}".format(drive, files))
				print("[removed] {0}:\\{1}".format(drive, files))
				countlnkfiles += 1
		
		if countlnkfiles > 1:
			print("\nJust got removed {0} link files.\nAnd I dont know if most of them are shortcut link to your programs and files! :D".format(countlnkfiles))
		else:
			print("\nI removed nothing.")
		
		if os.path.exists("{0}:\\Files".format(drive)):
			# make hidden 'Drive files' path visible.
			# why? because we need to see it.
			os.system("attrib -s -h Files")#[WIP] change the name if nescessary
			
			# recover files.
			print("Recovering affected files...")
			
			# affected files count
			countaffctfiles = 0
			for paths_files in os.listdir("{0}:\\Files".format(drive)):
				os.system("move {0}:\\Files\\{1} {0}:\\".format(drive, paths_files))
				print("[recovered] {0}:\\{1}".format(drive, paths_files))
				countaffctfiles += 1
				
			if countaffctfiles > 0:
				print("{0} files recovered.".format(countaffctfiles))
			else:
				print("[WARNING] Couldn't recover files.")
			
		print("Use this program again when your device storage drive got infected again with RECYCLER virus! :D")
	elif drive == "":
		print("404 input not found...")
		
		# delay.
		time.sleep(3)
		
		# clear.
		os.system("cls")
	elif drive == "exit" or drive == "quit":
		print("Thank you for using this program!\nquitting now...")
		
		# delay
		delay(1)
		
		# break the loop
		break
		