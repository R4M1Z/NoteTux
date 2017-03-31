#!/usr/bin/env python

import os
os.system("clear")
#icon
os.system("chmod +x ico.ico")
os.system("sudo mv ico.ico /usr/share/icons/")

#desktop
os.system("sudo mv NoteTux.desktop /usr/share/applications")

#main
os.system("chmod +x notetux.py")
os.system("sudo mv notetux.py /usr/bin")

#sh
os.system("chmod +x startnt.sh")
os.system("sudo mkdir /usr/share/icons/Notetux")
os.system("sudo mv startnt.sh /usr/bin/")
