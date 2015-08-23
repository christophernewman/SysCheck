
SysCheck - The Base System Check Utility.
=========================================

Homepage: http://www.xnetproject.net/

Version : 1.1.5

Language: Python

Author  : Chris Newman <chris@xnetproject.net>

Files
-----

SysCheck.py
version.py
README (This File)
CHANGELOG

Contents
--------

   This README file is split into the following sections.
 Please read it all before reporting bugs, or problems:

	Introduction
	Supported Platforms
	Installing
	Configuration
	Running
	Customization
        Documentation   
	Mailing Lists
	Reporting Bugs
	License  (GPL)
	Alternative Solutions
	Thanks
        Comments / Suggestions / Patches?

	Recent Changes


Introduction
------------

  This application provides an opensource system check utility with detailed
functions to make some system administration tasks easier.


--
 NOTE: The Base System Check Utility requires root privledges to properly run
-


Supported Platforms
-------------------

  This software was primarily developed under Ubuntu Mate GNU/Linux, and 
 should run on any similar GNU/Linux development platform.

  Because the software is written with the portable scripting
 language, Python, it should also run under other flavors of Unix/Linux.

  SysCheck has been tested upon the following platforms:

	Ubuntu  	Debian		Ubuntu Mate		


 
   --
  (*) Commands specific to Debian-Based environments for updates/cleanups.
This can be modified to work in other flavors or Linux.



Installing under Linux
---------------------

  From the archive simply unpack in any location.

  The software can be executed by running the following command within the
directory the application files:

sudo python SysCheck.py

  After executing the application; a series of commands will print in 
terminal specifying the status of each command.


Configuration
-------------

  As long as Python is installed; the application should not require any
additional configurations

NOTE:

  Optional configurations can be made to match Non-Debian enviroments to
execute certain functions.


Running
-------

  The first time you start the application the check will start 
immediately.


Customization
-------------

  The SysUpdate and SysClean functions for control line12, and control
line14 can be customized to work in other flavors that use different package
management systems and functions.


Documentation
-------------

  The documentation included with this software includes this
 'README' which explains the usage for this program.


Mailing Lists
-------------

  There are no current mailing lists at this time.


Reporting Bugs
--------------

  For a bug report to be useful it needs to contain as
 much information as possible.

  A simple means of giving all the relevant information is
 to send an e-mail to: chris@xnetproject.net
 
	
  Enter the text of your report into the text area, and click
 on the submit button.
  
  To assure prompt attention please include the
 following information:

   1. Your operating system, and version:
	Run 'uname -a', and 'arch' and send me the results.

   2. The version of SysCheck you're using.
	Run SysCheck and send me the results


License
-------

  As the name might suggest, this software is distributed under 
 the terms of the GNU Public License, version 2.

  Please find a copy of the GNU Public License included with the
 source archive in the file COPYING, it will also be accessible
 from the server itself; read the startup banner for details.


Alternative Solutions
---------------------

  Here's a brief list of alternative solutions which
 you may want to investigate if this software doesn't
 quite meet your needs.


   Linux Health Check - http://linoxide.com/linux-shell-script/shell-script-check-linux-system-health/



Thanks
------

  I want to thank the open source community for all the great information,
advise as well as the many tutorials for the Python language that helped 
make this program possible.


Comments / Suggestions / Patches?
---------------------------------

  I optimistically welcome comments, feedback, suggestions, updated
 documentation and contributed themes/logos.



Chris
---
<chris@xnetproject.net>
