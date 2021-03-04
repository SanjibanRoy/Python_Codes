import time
import datetime

data=[
'2020001'
]
def getpath(array):
    for x in array:
        subvar=str(x[2:8])
        date=datetime.datetime.strptime(subvar, '%y%j').date()
        datee=date.strftime('%d-%m-%Y')
        print(time_stamp)
getpath(data)    
