from DTM import DTM
from ErrorsDTM import ErrorsDTM
from nDTM import nDTM




def PrintOutput(Cmd, DtmData):
    
    print Cmd + "->MSB:  " + "0x{0:02x}".format(DtmData[0]) + "  LSB:  " + "0x{0:02x}".format(DtmData[1])


mydtm=DTM()
#myndtm=nDTM()

mydtm.Reset()
PrintOutput("Reset" , mydtm.Send())
try:
    mydtm.StartRXTest(0,0,3)
except ErrorsDTM as instance:
    a=0
    
PrintOutput("Start RX" , mydtm.Send())
mydtm.StartTXTest(0,0,0)
PrintOutput("Start TX" , mydtm.Send())
mydtm.TestEnd()
PrintOutput("Test End" , mydtm.Send())
