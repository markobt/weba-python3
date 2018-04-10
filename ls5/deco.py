import datetime
import os
import sys

print(datetime.datetime.now())
print(os.cpu_count())
print(sys.maxsize.bit_length())

start = datetime.datetime.now()

curDir = os.getcwd()
print(curDir)






