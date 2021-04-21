## user variables (edit as needed)
TERATERM_LOCATION = r'c:\teraterm-4.92\ttermpro.exe'  #edit is not required
TERATERM_CMD_LINE = r'/M=c:\teraterm-4.92\ttl\adl_rmt.ttl'  #edit is not required
USB_POWER_SPLITTER_SN = '21030054'  #power splitter s/n, this must be configured correctly
LOOP_CNT = 5  #use 5 for Nx5 RMT
POWER_OFF_AT_LAST_LOOP = False  #set "False" when power off the SUT at the end is not desired
SUT_DISCHARGE_TIME = 15  #time in second for discharge between AC-off and AC-on


import os
import time
import subprocess

for i in range(LOOP_CNT):
    os.system("C:\KKLLAcCycle\KKLLAcCycle.exe  -sn=%s -sk=1  -ac=1"%USB_POWER_SPLITTER_SN)  #AC-on SUT
    pid = subprocess.Popen([TERATERM_LOCATION, TERATERM_CMD_LINE])
    pid.wait()  #wait till TeraTerm close
    if (i == LOOP_CNT-1):  #the final loop
        if (POWER_OFF_AT_LAST_LOOP):
            os.system("C:\KKLLAcCycle\KKLLAcCycle.exe  -sn=%s -sk=1  -ac=0"%USB_POWER_SPLITTER_SN)  #AC-off SUT
            time.sleep(SUT_DISCHARGE_TIME)
    else:
        os.system("C:\KKLLAcCycle\KKLLAcCycle.exe  -sn=%s -sk=1  -ac=0"%USB_POWER_SPLITTER_SN)  #AC-off SUT
        time.sleep(SUT_DISCHARGE_TIME)
