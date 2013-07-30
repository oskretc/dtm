from DTM import DTM
from ErrorsDTM import ErrorsDTM
from nDTM import nDTM


mydtm=DTM(1)
#myndtm=nDTM()

try:
    mydtm.Reset()
    mydtm.StartRXTest(0,0,1)
    mydtm.StartTXTest(Freq=25, Length=33, PacketType=3)
    mydtm.TestEnd()
    Response=[0x01,0x00]
    mydtm.ParseResponse(Response)
    

except ErrorsDTM as instance:
    print instance.__class__.__name__
