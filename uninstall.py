# -*- coding: utf-8 -*-
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage

def APPUnInstall(aaapp):
    device.removePackage(aaapp) 


device = MonkeyRunner.waitForConnection()

if not device:
    print("getmobile break")
else:
    print("getmobile Connect")
 
APPUnInstall('com.shuame.sprite')

print('ok')