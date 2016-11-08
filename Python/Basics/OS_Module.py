# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import os
import time

cur_dir = os.getcwd()

print(cur_dir)

os.mkdir("test")

time.sleep(2)
os.rename("test", "test2")

time.sleep(2)
os.rmdir("test2")
