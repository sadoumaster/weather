# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:05:13 2016

@author: user1
"""
import time
import lnetatmo
authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)

#print moduleData
#print moduleData.get("Noise")
# For each available module in the returned data that should not be older than one hour (3600 s) from now
for module, moduleData in devList.lastData(exclude=3600).items() :
   
    # Name of the module (or station embedded module), the name you defined in the web netatmo account station management
    print(module)
    
    # List key/values pair of sensor information (eg Humidity, Temperature, etc...)
    for sensor, value in moduleData.items() :
        # To ease reading, print measurement event in readable text (hh:mm:ss)
        if sensor == "When" : value = time.strftime("%H:%M:%S",time.localtime(value))
        print("%30s : %s" % (sensor, value))
print (devList.modulesNamesList())
print (devList.checkNotUpdated())
print (devList.default_station)
print (devList.getAuthToken)
print (devList.MinMaxTH("Kamiyasu","outdoor","day"))
print (devList.__init__(authorization))