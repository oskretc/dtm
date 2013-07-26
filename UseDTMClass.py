import serial
import time

from DTM import DTM
from ErrorsDTM import ErrorsDTM
#from nDTM import nDTM

Uart1 = '/dev/ttyAMA0'
DTMPort = serial.Serial(Uart1, 19200, timeout=1)

def PrintOutput(Cmd, DtmData):
    
    print Cmd + "->MSB:  " + "0x{0:02x}".format(DtmData[0]) + "  LSB:  " + "0x{0:02x}".format(DtmData[1])


mydtm=DTM()
#myndtm=nDTM()

mydtm.Reset()
PrintOutput("Reset" , mydtm.Send())
DTMPort.write(mydtm.SendStr())
time.sleep(1)

try:
    mydtm.StartTXTest(0,37,0)
    PrintOutput("Start TX" , mydtm.Send())
    DTMPort.write(mydtm.SendStr())
    time.sleep(2)
except ErrorsDTM as instance:
    print "error"
    a=0
    


mydtm.TestEnd()
DTMPort.write(mydtm.SendStr())
PrintOutput("TestEnd" , mydtm.Send())


DTMPort.close()
