#!/usr/bin/python

#############################
# Author: Chris Newman      #
# Version: 1.1.4            #
# Application: SysCheck.py  #
# Language: Python          #
#############################


# Colors class

class bcolors:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	HEADER = '\033[95m'
	RED = '\033[93m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m';

# Program variables

Application = ' Application: SysCheck.py';
AppName = ' Base System Check Utility';
Author = ' Author: Chris Newman ';
BlueColorStart = bcolors.BLUE;
BoldColorStart = bcolors.BOLD;
Break = '\n';
ColorEnd = bcolors.ENDC;
GreenColorStart = bcolors.GREEN;
Header = GreenColorStart + 'The Base System Check Utility is checking your system on:\n\n' + ColorEnd;
HeaderColorStart = bcolors.HEADER;
HeaderLine = '#############################';
HeaderLine2 = '############################';
Language = ' Language: Python';
RedColorStart = bcolors.RED;
Space = GreenColorStart + 'Checking System Space:\n\n' + ColorEnd;
SysInfo = GreenColorStart + 'Checking System Information:\n\n' + ColorEnd;
SysMem = GreenColorStart + 'Checking System Memory:\n\n' + ColorEnd;
SysUpdate = GreenColorStart + 'Checking System Hardware:\n\n' + ColorEnd;
UnderlineColorStart = bcolors.UNDERLINE;
Version = ' Version: 1.1.4';

# Program synopsis

print Break;
print GreenColorStart + HeaderLine + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Author + ColorEnd + GreenColorStart + "     #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Version + ColorEnd + GreenColorStart + "            #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Application + ColorEnd + GreenColorStart + "  #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Language + ColorEnd + GreenColorStart + "          #" + ColorEnd;
print GreenColorStart + HeaderLine + ColorEnd;
print Break;

# Basic program header

print Break;
print GreenColorStart + HeaderColorStart + AppName + ColorEnd;
print GreenColorStart + HeaderLine2 + ColorEnd;
print Break;

# Import text time controls

import sys
import os
from time import sleep

# Line text parameters

line0 = Break;
line1 = Header;
line2 = Break;
line3 = Space;
line4 = Break;
line5 = SysInfo;
line6 = Break;
line7 = SysMem;
line8 = Break;
line9 = SysUpdate;
line10 = Break;

# Controls for each character line

for char in line0:
	sleep(0.04)
	print 'A simple system check program';
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line1:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line2:
	sleep(0.09)
	os.system("date")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line3:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line4:
	sleep(0.09)
	os.system("df -h")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line5:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line6:
	sleep(0.09)
	os.system("python version.py")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line7:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line8:
	sleep(0.09)
	os.system("free -m")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line9:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line10:
	sleep(0.09)
	os.system("sudo lshw -short")
	sys.stdout.write(char)
	sys.stdout.flush()
	
#######
# END #
#######
