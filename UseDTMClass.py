import serial
import time
import sys  #Retry loop needed this

sys.path.insert(0, '/usr/share/adafruit/webide/repositories/tcp1')

from TCPClass import C3POServer

from DTM import DTM
from ErrorsDTM import ErrorsDTM

class RetryError(Exception):
    pass

def retryloop(attempts, timeout):
    starttime = time.time()
    success = set()
    for i in range(attempts): 
        success.add(True)
        yield success.clear
        if success:
            return
        if time.time() > starttime + timeout:
            break
    raise RetryError
    
def fancyretryloop(attempts, timeout=None, delay=0, backoff=1):
    starttime = time.time()
    success = set()
    for i in range(attempts): 
        success.add(True)
        yield success.clear
        if success:
            return
        duration = time.time() - starttime
        if timeout is not None and duration > timeout:
            break
        if delay:
            time.sleep(delay)
            delay = delay * backoff

    e = sys.exc_info()[1]

    # No pending exception? Make one
    if e is None:
        try: raise RetryError
        except RetryError as e: pass

    # Decorate exception with retry information:
    e.args = e.args + ("on attempt {0} of {1} after {2:.3f} seconds".format(i, attempts + 1, duration),)

    raise



#from nDTM import nDTM


def ReadUartWithRetry(Count):
    for retry in fancyretryloop(10, timeout=1):
        try:
            Response=DTMPort.read(Count)
        except OSError:
            print "retrying"
            time.sleep(0.01) 
            retry()
    return Response
    
def DTMMode(mydtm):
    mydtm.DataOut=[0x32, 0x06]
    DTMPort.write(mydtm.SendStr())
    mydtm.DataOut=[0x3E, 0x00]
    DTMPort.write(mydtm.SendStr())    
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    #time.sleep(1)

def DTMReset(mydtm):
    mydtm.Reset()
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001) 
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    #time.sleep(1)
    
def DTMStartTX(mydtm,Freq,Length,PacketType):
    mydtm.StartTXTest(Freq, Length, PacketType)
    DTMPort.write(mydtm.SendStr())
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    #time.sleep(5)
    
def DTMStartRX(mydtm,Freq,Length,PacketType):
    mydtm.StartRXTest(Freq,Length,PacketType)
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001) 
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    #time.sleep(5)    
    
def DTMTestEnd(mydtm):
    mydtm.TestEnd()
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001)    
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    #time.sleep(1)  

Uart1 = '/dev/ttyAMA0'
DTMPort = serial.Serial(Uart1, 19200, timeout=1)

mydtm=DTM(1)
#myndtm=nDTM()
Debug=0


print "trying to establish the server"    
s=C3POServer()

try:
    while 1:
        print "listening slow"
        s.StartListen()
        s.DoConnect()
        print '...connected!', s.Address

        DataIn=s.RecvData()   #Receive Commands

        
        eval(DataIn)
        
        s.SendData("OK:" + mydtm.RspMsg)     #Send ACK on the Command
        s.CloseConnection()
        
except ErrorsDTM as instance:
    print instance.__class__.__name__        
        
        
except KeyboardInterrupt:
    print "Keyboard Detected"
finally:
    print "Closing Server"
    s.CloseServer
    print "Closing Uart"
    DTMPort.close()

    
"""    


try:
    mydtm.Reset()
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001) 
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    time.sleep(1)
    
    if Debug:
        mydtm.DataOut=[0x32, 0x06]
        DTMPort.write(mydtm.SendStr())
        mydtm.DataOut=[0x3E, 0x00]
        DTMPort.write(mydtm.SendStr())    
        Response=ReadUartWithRetry(2)       
        mydtm.ParseResponseStr(Response)
        time.sleep(1)
    
    #mydtm.StartRXTest(0,0,1)
    
    mydtm.StartRXTest(Freq=0, Length=37, PacketType=0)
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001) 
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    time.sleep(5)    
    
    mydtm.TestEnd()
    DTMPort.write(mydtm.SendStr())
    #time.sleep(0.001)    
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    time.sleep(1)  
    
    mydtm.StartTXTest(Freq=0, Length=37, PacketType=0)
    DTMPort.write(mydtm.SendStr())
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    time.sleep(5)
    
    mydtm.TestEnd()
    DTMPort.write(mydtm.SendStr())
    Response=ReadUartWithRetry(2)       
    mydtm.ParseResponseStr(Response)
    
    
        if DataIn=="DTMReset":
           DTMReset(mydtm)
        if DataIn=="DTMStartTX":
            DTMStartTX(mydtm)
        if DataIn=="DTMStartRX":
            DTMStartRX(mydtm)
        if DataIn=="DTMTestEnd":
            DTMTestEnd(mydtm)
            


except ErrorsDTM as instance:
    print instance.__class__.__name__
    
finally:
    DTMPort.close()
    print "Port Closed"

"""