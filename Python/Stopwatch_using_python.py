import threading
import sys
from time import *

hour = 0
minute = 0
sec = 0

timer = [hour,minute,sec]

stop = False

def get_input():
  global stop
  while True:
    user_input = input ("\n\nPress Enter to stop: ")
    if user_input == "":
      stop = True
      break

input_thread = threading.Thread(target=get_input, daemon=True)

print("Press Enter to start the STOPWATCH")
start = input("")
input_thread.start()

while (start == ""):
  
  timer[2] += 1
  if (timer[2] == 60):
    timer[2] = 0
    timer[1] += 1
    if (timer[1] == 60):
      timer[1] = 0
      timer[0] += 1
    


  print(f"\r\tStopwatch : {timer[0]:02}:{timer[1]:02}:{timer[2]:02}", end="")
  sleep(1)
  if stop:
    break
 

print("\n\t Stopwatch Stopped")



  
