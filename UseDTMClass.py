from DTM import DTM
from nDTM import nDTM




def PrintOutput(Cmd):
    print Cmd + "->MSB:  " + "0x{0:02x}".format(mydtm.DataOut[0]) + "  LSB:  " + "0x{0:02x}".format(mydtm.DataOut[1])


mydtm=DTM()
#myndtm=nDTM()

mydtm.Reset()
PrintOutput("Reset")

mydtm.StartRXTest(0,0,3)
PrintOutput("Start RX")
mydtm.StartTXTest(0,0,0)
PrintOutput("Start TX")
mydtm.TestEnd()
PrintOutput("Test End")
