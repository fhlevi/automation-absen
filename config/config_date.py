import datetime
import time 

days = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"]

dateNow = datetime.datetime.now()
timeInformation = time.localtime()

today = days[timeInformation[6]]