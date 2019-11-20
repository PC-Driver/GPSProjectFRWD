# SeniorProjectGPSScript
GPS Script for the AT&amp;T 2nd Generation IoT Kit for our senior project. This script takes location information and sends the data to a firebase database to be used for the mobile application.



AT&T second generation IoT kit
The instrutions found below are done on a windows 10 machine. Furthermore, this is under the assumption that the user is using a working IoT SIM card with the ATT 2nd Generation Kit (from here on out it will be called the SK2)
0) Download the connection manager found here https://github.com/CloudConnectKits/WNC/blob/master/WNCCM_1.0.9.msi?raw=true
0.5) Download the user manual found on the Github page for further reference https://github.com/att-iotstarterkits/sk2-Users-Guide

1) Download the file found here https://s3-us-west-1.amazonaws.com/td-marketplace-assets/SDK01/M18Q2_v12.09.182151_APSS_OE_v01.07.183121.zip - extract into your root directory
2) open a command terminal inside the folder you just extracted
3) enter the command "./adb devices" - this should note that the adb server has started and the listed devices are: "WNC_ADB" (authenticated)
4) from here you have two ways to program, either by utilizing the 3rd party command line app, Git Bash or by going to the online IDE editor found at 192.168.8.1
5) for the purposes of running this project, use 192.168.1.1 and click on "IDE" on the top of the page
6) enter the directory python-firebase and then double click on senior_project.py
7) at this point run the connection manager application you installed earlier go to profile settings and make sure that profile one says "m2m64.com.attz", if it does not, edit it to make it say "m2m64.com.attz".
	once you are done editing, the modem will should restart - wait until the connection says "LTE" at the top of the connection manager program. Running this project on 3G may yield errors
	note: do not press the "connect" button found in home, doing so will interrupt the connection between your computer and the program. Furthermore, if the device does not say LTE after some time, please unplug and replug the SK2 and apply m2m64.com.attz again.
8) once the connection says "LTE", double click on senior_project.py in the IDE and click on run at the bottom left corner of your browser. it may ask for the full command, just press ok or enter and the program will run
9) if you are reading this, chances are the database used to keep record of the GPS location may be long gone, if so simply replace 'https://bluetoothlegattandgraphclean.firebaseio.com/' on the python script with your own database and the GPS coordinates will be sent to that.


