# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 13:05:13 2016

@author: user1
"""
import time
import lnetatmo
import sys
sys.path.append('/Users/user1/Documents/python')
import weather.abs_hum as abs_hum
authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)
devList_lastdata={}
#print moduleData
#print moduleData.get("Noise")
# For each available module in the returned data that should not be older than one hour (3600 s) from now
for module, moduleData in devList.lastData(exclude=3600).items() :
   
    # Name of the module (or station embedded module), the name you defined in the web netatmo account station management
    print(module)
    devList_lastdata[module]=moduleData    
    # List key/values pair of sensor information (eg Humidity, Temperature, etc...)
    for sensor, value in moduleData.items() :
        # To ease reading, print measurement event in readable text (hh:mm:ss)
        if sensor == "When" : value = time.strftime("%H:%M:%S",time.localtime(value))
        print("%30s : %s" % (sensor, value))
def getAbs_hum(module):
    return abs_hum.get_abs_hum(devList_lastdata[module]['Humidity'],
                                devList_lastdata[module]['Temperature'])
out_abs_hum=getAbs_hum('outdoor')
in_abs_hum=getAbs_hum('indoor')
print ('outdoor absolute Humidity{}g/m3, indoor absolute Humidity{}g/m3'
.format(out_abs_hum, in_abs_hum))
print (devList.modulesNamesList()) #['outdoor', 'indoor']
print (devList.checkNotUpdated()) #None
print (devList.default_station) #Kamiyasu
print (devList.getAuthToken)
print (devList.MinMaxTH("Kamiyasu","outdoor","day"))