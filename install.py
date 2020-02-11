#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system("clear")
#icon
os.system("chmod +x ico.png")
os.system("sudo mkdir /usr/share/icons/NoteTux")
os.system("sudo cp ico.png /usr/share/icons/NoteTux")

#desktop
os.system("sudo cp NoteTux.desktop /usr/share/applications")

#main
os.system("chmod +x notetux.py")
os.system("sudo cp notetux.py /usr/bin")
print "Quraşdırılma uğurla tamamlandı"
