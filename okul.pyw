#python version 3.8.8

import datetime
import os
x = datetime.datetime.now()
total = 0
if(15-x.hour<0):
    exit()
else:
    total = ((15-x.hour)*3600)-(x.minute*60)
    cmd = "shutdown -s -t {}".format(total)
    os.system(cmd)
