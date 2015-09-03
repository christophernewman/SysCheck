#!/usr/bin/python

#
#   Author: Chris Newman 
#   Version: 1.1.7 (Final)
#   Application: SysCheck.py
#   Language: Python
#
#   Copyright 2015 Xnet Project
#   All Rights Reserved.

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#   License for the specific language governing permissions and limitations
#   under the License.



# Colors class

class bcolors:
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	HEADER = '\033[95m'
	RED = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m';
	
# Program variables

Application = ' Application: SysCheck.py';
AppName = ' SysCheck Utility';
Author = ' Author: Chris Newman ';
BlueColorStart = bcolors.BLUE;
BoldColorStart = bcolors.BOLD;
Break = '\n';
ColorEnd = bcolors.ENDC;
GreenColorStart = bcolors.GREEN;
Header = GreenColorStart + 'The SysCheck Utility is checking your system on:\n\n' + ColorEnd;
HeaderColorStart = bcolors.HEADER;
HeaderLine = '#############################';
Headercase2 = '############################';
Language = ' Language: Python';
RedColorStart = bcolors.RED;
Space = GreenColorStart + 'Checking System Space:\n\n' + ColorEnd;
SysInfo = GreenColorStart + 'Checking System Information:\n\n' + ColorEnd;
SysMem = GreenColorStart + 'Checking System Memory:\n\n' + ColorEnd;
SysClean = GreenColorStart + 'Running System Cleanup:\n\n' + ColorEnd;
SysUpdate = GreenColorStart + 'Checking and Installing System Updates:\n\n' + ColorEnd;
SysHw = GreenColorStart + 'Checking System Hardware:\n\n' + ColorEnd;
UnderlineColorStart = bcolors.UNDERLINE;
Version = ' Version: 1.1.7 (Final)';
Complete = GreenColorStart + 'SysCheck Complete:\n\n' + ColorEnd;

# Program synopsis

print Break;
print GreenColorStart + HeaderLine + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Author + ColorEnd + GreenColorStart + "     #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Version + ColorEnd + GreenColorStart + "    #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Application + ColorEnd + GreenColorStart + "  #" + ColorEnd;
print GreenColorStart + "#" + HeaderColorStart +  Language + ColorEnd + GreenColorStart + "          #" + ColorEnd;
print GreenColorStart + HeaderLine + ColorEnd;
print Break;
print"#   Copyright 2015 Xnet Project";
print"#   All Rights Reserved.";
print Break;
print"#   Unless required by applicable law or agreed to in writing, software";
print"#   distributed under the License is distributed on an" + RedColorStart + " AS IS " + ColorEnd + "BASIS, WITHOUT";
print"#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the";
print"#   License for the specific language governing permissions and limitations";
print"#   under the License.";
print Break;

# Basic program header

print Break;
print GreenColorStart + HeaderColorStart + AppName + ColorEnd;
print GreenColorStart + Headercase2 + ColorEnd;
print Break;

# Import text time controls

import sys
import os
import platform
from time import sleep
	
# Case parameters

case0 = Break;
case1 = Header;
case2 = Break;
case3 = Space;
case4 = Break;
case5 = SysInfo;
case6 = Break;
case7 = SysMem;
case8 = Break;
case9 = SysHw;
case10 = Break;
case11 = SysUpdate;
case12 = Break;
case13 = SysClean;
case14 = Break;
case15 = Complete;
case16 = Break;

# OS distribution

dist = platform.linux_distribution(
                    supported_dists=('redhat', 'debian', 'SuSE', 'mandrake', 'Ubuntu'))[0];



# Controls for each character line


for char in case0:
	sleep(0.04)
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo + Author: Chris Newman >> check.log")
	os.system("echo + Version: 1.1.7 Final >> check.log")
	os.system("echo + Application: SysCheck.py >> check.log")
	os.system("echo + Language: Python >> check.log")
	os.system("echo +---------------------------+ >> check.log")
	os.system("echo >> check.log")
	os.system("echo SysCheck Utility >> check.log")
	os.system("echo ------------------------- >> check.log")
	os.system("echo >> check.log")
	print 'SysCheck Started';
	os.system("echo SysCheck started >> check.log")
	os.system("echo >> check.log")
	os.system("echo The SysCheck Utility is checking your system on: >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case1:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case2:
	sleep(0.09)
	os.system("tput setaf 3; date")
	os.system("echo >> check.log")
	os.system("tput setaf 3; date >> check.log")
	os.system("echo >> check.log")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case3:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case4:
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
for char in case5:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case6:
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
for char in case7:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case8:
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
for char in case9:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case10:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install lshw -y && lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; lshw -short >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('redhat'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install lshw -y && lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; lshw -short >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Fedora'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install lshw -y && lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; lshw -short >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('debian'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get nstall lshw -y && lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; lshw -short >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Ubuntu'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get install lshw -y && lshw -short")
	os.system("echo >> check.log")
	os.system("tput setaf 3; lshw -short >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
else:
	os.system("echo >> check.log")
	os.system("echo Checking System Hardware: >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list.")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case11:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case12:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('redhat'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Fedora'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('debian'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Ubuntu'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get update -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
else:
	os.system("echo >> check.log")
	os.system("echo Checking and Installing System Updates: >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list.")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case13:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case14:
	sleep(0.09)
if dist == ('CentOS'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum-utils -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('redhat'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum-utils -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Fedora'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum-utils -y")
	os.system("echo >> check.log")
	os.system("tput setaf 3; yum install yum utils -y >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --leaves --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --problems >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --orphans --all >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --cleandupes >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels")
	os.system("echo >> check.log")
	os.system("tput setaf 3; package-cleanup --oldkernels >> check.log")
	os.system("echo >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only")
	os.system("echo >> check.log")
	os.system("tput setaf 3; /usr/sbin/yum-complete-transaction --cleanup-only >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("echo")
elif dist == ('debian'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
elif dist == ('Ubuntu'):
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean")
	os.system("echo >> check.log")
	os.system("tput setaf 3; sudo apt-get autoremove && sudo apt-get clean && sudo apt-get autoclean >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
else:
	os.system("echo >> check.log")
	os.system("echo Running System Cleanup: >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list.")
	os.system("echo ERROR: CHECK FAILED!! - OS Version Unsupported. Please check the software supported version list. >> check.log")
	os.system("echo")
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case15:
	sleep(0.04)
	sys.stdout.write(char)
	sys.stdout.flush()
for char in case16:
	sleep(0.09)
	os.system("echo")
	os.system("echo >> check.log")
	os.system("echo SysCheck Completed on:")
	os.system("echo SysCheck Completed on: >> check.log")
	os.system("echo")
	os.system("date >> check.log")
	os.system("date")
	os.system("echo >> check.log")
	os.system("echo ----- >> check.log")
	os.system("echo >> check.log")
	os.system("echo")
	os.system("tput sgr0; tput bel;")
	sys.stdout.write(char)
	sys.stdout.flush()
