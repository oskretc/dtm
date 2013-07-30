import serial
import time

from DTM import DTM
from ErrorsDTM import ErrorsDTM
#from nDTM import nDTM

Uart1 = '/dev/ttyAMA0'
DTMPort = serial.Serial(Uart1, 19200, timeout=1)

def PrintOutput(Cmd, DtmData):
    
    print Cmd + "->MSB:  " + "0x{0:02x}".format(DtmData[0]) + "  LSB:  " + "0x{0:02x}".format(DtmData[1])


mydtm=DTM(1)
#myndtm=nDTM()

try:
    mydtm.Reset()
    DTMPort.write(mydtm.SendStr())
    Response=DTMPort.read(2)
    mydtm.ParseResponseStr(Response)
    time.sleep(1)
    
    #mydtm.StartRXTest(0,0,1)
    
    mydtm.StartRXTest(Freq=0, Length=37, PacketType=3)
    DTMPort.write(mydtm.SendStr())
    Response=DTMPort.read(2)
    mydtm.ParseResponseStr(Response)
    time.sleep(2)    
    
    mydtm.TestEnd()
    DTMPort.write(mydtm.SendStr())
    time.sleep(0.001)    
    Response=DTMPort.read(2)
    mydtm.ParseResponseStr(Response)
    


except ErrorsDTM as instance:
    print instance.__class__.__name__
    
finally:
    DTMPort.close()
