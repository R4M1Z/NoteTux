#!/usr/bin/env python

import os
os.system("clear")
#icon
os.system("chmod +x ico.png")
os.system("sudo cp ico.png /usr/share/icons/")

#desktop
os.system("sudo cp NoteTux.desktop /usr/share/applications")

#main
os.system("chmod +x notetux.py")
os.system("sudo cp notetux.py /usr/bin")

#sh
os.system("chmod +x startnt.sh")
os.system("sudo mkdir /usr/share/icons/Notetux")
os.system("sudo cp startnt.sh /usr/bin/")
