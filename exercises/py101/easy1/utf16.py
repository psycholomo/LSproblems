def utf16_value(string):
    sum_ = 0
    for char in string:
        sum += ord(char)
    return sum_


import time
from time import ctime
import pyautogui
from datetime import datetime, timedelta, timezone
import ntplib


pyautogui.PAUSE = 0.001
#                  year, M, D, H, min, sec, microsec)
runTime = datetime(2025, 6, 25, 5, 19, 15, 0)
seconds_to_subtract = 100
delta = timedelta(seconds=seconds_to_subtract)
syncTime = runTime - delta

runTimeStamp = runTime.timestamp()



def get_ntp_time(host='pool.ntp.org'):
    """
    Retrieves the time from an NTP server.

    Args:
        host (str): The hostname or IP address of the NTP server.

    Returns:
        str: The time from the NTP server, formatted as a string.
    """
    try:
        c = ntplib.NTPClient()
        response = c.request(host, version=3)
        #return ctime(response.tx_time)
        #return datetime.datetime.utcfromtimestamp(response.tx_time)
        return response.tx_time
    except ntplib.NTPException as e:
        return f"Error: {e}"


while True:
  now = datetime.now()
  if now > syncTime:
   ntp_now = get_ntp_time()

   print(ntp_now)

   if isinstance(ntp_now, str):
      time.sleep(40)
      ntp_now = get_ntp_time()

   if isinstance(ntp_now, str):
      ntp_now = datetime.now().timestamp()


      

   pause_time = runTimeStamp - ntp_now
   print(pause_time)
   
   time.sleep(float(pause_time))
   
   print("clicking")
   pyautogui.click(149,204)
   pyautogui.click(149,485)
   pyautogui.click(158,775)

   pyautogui.click(154,1054)
   pyautogui.click(157,1333)
   pyautogui.click(152,1618)

   pyautogui.click(1188,209)
   pyautogui.click(1192,498)
   pyautogui.click(1195,785)
   pyautogui.click(1202,1056)

   break
