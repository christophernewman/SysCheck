#!/usr/bin/python

#############################
# Author: Chris Newman      #
# Version: 1.1.6            #
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
SysClean = GreenColorStart + 'Running System Cleanup:\n\n' + ColorEnd;
SysUpdate = GreenColorStart + 'Checking and Installing System Updates:\n\n' + ColorEnd;
SysHw = GreenColorStart + 'Checking System Hardware:\n\n' + ColorEnd;
UnderlineColorStart = bcolors.UNDERLINE;
Version = ' Version: 1.1.6';
Complete = GreenColorStart + 'SysCheck Completed\n\n' + ColorEnd;

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
line9 = SysHw;
line10 = Break;
line11 = SysUpdate;
line12 = Break;
line13 = SysClean;
line14 = Break;
line15 = Complete;
line16 = Break;

# Controls for each character line

for char in line0:
	sleep(0.04)
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo + Author: Chris Newman >> check.log")
	os.system("echo + Version: 1.1.6 >> check.log")
	os.system("echo + Application: SysCheck.py >> check.log")
	os.system("echo + Language: Python >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo >> check.log")
	os.system("echo Base System Check Utility >> check.log")
	os.system("echo ------------------------- >> check.log")
	os.system("echo >> check.log")
	print 'SysCheck Started';
	os.system("echo SysCheck started >> check.log")
	os.system("echo >> check.log")
	os.system("echo The Base System Check Utility is checking your system on: >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line1:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line2:
	sleep(0.09)
	os.system("tput setaf 3; date")
	os.system("echo >> check.log")
	os.system("tput setaf 3; date >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line3:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line4:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Space: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; df -h")
	os.system("echo >> check.log")
	os.system("tput setaf 3; df -h >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line5:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line6:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Information: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; python version.py")
	os.system("echo >> check.log")
	os.system("tput setaf 3; python version.py >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line7:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line8:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Memory: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; free -m")
	os.system("echo >> check.log")
	os.system("tput setaf 3; free -m >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line9:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line10:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo lshw -short >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line11:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line12:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line13:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line14:
	sleep(0.09)
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line15:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in line16:
	sleep(0.09)
	os.system("echo SysCheck Completed on: >> check.log")
	os.system("date >> check.log")
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	os.system("tput sgr0; tput bel;")
	sys.stdout.write(char)
	sys.stdout.flush()

	
#######
# END #
#######
