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
strdata= ''.join(chr(e) for e in mydtm.Send())
print strdata
DTMPort.write(strdata)

try:
    mydtm.StartRXTest(0,0,3)
except ErrorsDTM as instance:
    a=0
    
PrintOutput("Start RX" , mydtm.Send())
mydtm.StartTXTest(0,0,0)
PrintOutput("Start TX" , mydtm.Send())
mydtm.TestEnd()
PrintOutput("Test End" , mydtm.Send())

DTMPort.close()
