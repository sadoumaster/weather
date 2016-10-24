# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:08:12 2016

@author: user1
mtype:Humidity, Temperature, CO2, Noise, Pressure
"""
import sys
sys.path.append('/Users/user1/Documents/python')
import time, datetime
import lnetatmo
import weather.abs_hum as abs_hum
authorization = lnetatmo.ClientAuth()
devList = lnetatmo.DeviceList(authorization)
start= datetime.datetime(2016, 10, 23, 0, 0, 0)
start= int(time.mktime(start.timetuple()))
end= datetime.datetime(2016, 10, 23, 23, 59, 59)
end= int(time.mktime(end.timetuple()))
module='02:00:00:03:df:2e'#outdoor
#module='70:ee:50:03:d7:40'#indoor

measure_dict=devList.getMeasure( device_id='70:ee:50:03:d7:40',                             # Replace with your values
                       module_id=module,                             #    "      "    "    "
                       scale="30min",
                       mtype="Temperature,Humidity",
                       date_begin=start,
                       date_end=end)
'''
上記で以下の様に出力される。
{'body': {'1475248500': [25.8, 74],
          '1475250300': [25.8, 74],
~~~~
          '1475502300': [28.2, 77],
          '1475504100': [28.2, 77],
          '1475505900': [28.1, 77]},
 'status': 'ok',
 'time_exec': 0.32197690010071,
 'time_server': 1477304980}
'''
measure_times_list = [i for i in measure_dict["body"]]
measure_times_list.sort()

for i in measure_times_list:
    Temp=measure_dict['body'][i][0]
    Hum=measure_dict['body'][i][1]
    Abs_Hum=abs_hum.get_abs_hum(Hum, Temp)
    print('{}:Temp{}℃,Hum{}%,Abs Hum{}g/m3'.format(datetime.datetime.fromtimestamp(int(i)), 
          Temp, Hum, Abs_Hum))

time_temp_dict= {int(i):measure_dict['body'][i][0] 
                for i in measure_times_list} #timestamp:temperature
print (time_temp_dict)