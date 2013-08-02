from ErrorsDTM import ErrorsDTM
from ErrorsDTM import FrequencyError
from ErrorsDTM import PacketTypeError
from ErrorsDTM import LengthError

class DTM:
    """Class DTM
    """
    # Attributes:
    Frequency = 0  # (int8) 
    Length = None  # (int8) 
    PacketType = None  # (int8) 
    #PayloadSize = None  # (int8) 
    Event = None  # (bool) 
    Status = None  # (bool) 
    PacketCount=0
    DataOut = [0 , 0]  # (Array) 
    DataIn = None  # (Array) 
    Command = None  # () 
    Verboise= 0
    
    #Constants
    MAX_FREQ = 39
    MIN_FREQ = 0
    CMD_TXT = {0b0000 : "Reset",
               0b0100: "Start RX", 
               0b1000: "Start TX",
               0b1100: "Test End"}

    # Operations
    def __init__(self, verboise=0):
        self.Verboise=verboise
        if self.Verboise:
            print "Object Initialized"
        
        
    def SetFrequency(self, Freq):
        """function SetFrequency
        
        Freq: 
        
        returns 
        """
        if (Freq <= self.MAX_FREQ and Freq >= self.MIN_FREQ):
            self.Frequency=Freq & 0b00111111
        else:
            raise FrequencyError(Freq)
        return None # should raise NotImplementedError()
    
    def SetPacketType(self, PacketType):
        """function SetPacketType
        
        PacketType: 
        
        returns 
        """
        #print PacketType
        if (PacketType<=3 and PacketType>=0):
            self.PacketType=PacketType & 0b00000011
        else:
            raise PacketTypeError(PacketType)
        return None # should raise NotImplementedError()
    
    def SetLength(self, Length):
        """function SetLength
        
        Length: 
        
        returns 
        """
        if (Length<=0x25 and Length>=0):
            self.Length=Length & 0b00111111
        else:
            raise LengthError(Length)
        
        return None # should raise NotImplementedError()
    
    def Send(self):
        """function Send
        
        returns 
        """
        return self.DataOut # should raise NotImplementedError()

    def SendStr(self):
        """function Send
        
        returns 
        """
        return ''.join(chr(e) for e in self.DataOut) # should raise NotImplementedError()        
    
    def StartTXTest(self, Freq=0, Length=0, PacketType=0):
        """function StartTXTest
        
        returns 
        """
        self.Command=0b1000
        self.SetFrequency(Freq)
        self.SetLength(Length)
        self.SetPacketType(PacketType)
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def StartRXTest(self, Freq=0, Length=0, PacketType=0):
        """function StartRXTest
        
        returns 
        """
        self.Command=0b0100   #01XX
        self.SetFrequency(Freq)
        self.SetLength(Length)
        self.SetPacketType(PacketType)
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def TestEnd(self):
        """function TestEnd
        
        returns 
        """
        self.Command=0b1100   #11XX
        self.Frequency=0
        self.PacketType=0
        self.Length=0       
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def Reset(self):
        """function Reset
        
        returns 
        """
        self.Frequency=0
        self.PacketType=0
        self.Length=0
        self.Command=0
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def __CalculateTransaction(self):
        """function CalculateTransaction
        
        returns 
        """
        self.DataOut[0]=(self.Command<<4) | self.Frequency
        self.DataOut[1]=(self.Length<<2) | self.PacketType
        self.PrintOutput()
        return None # should raise NotImplementedError()
    def PrintOutput(self):
        if self.Verboise:
            print self.CMD_TXT[self.Command] + "->MSB:  " + "0x{0:02x}".format(self.DataOut[0]) + "  LSB:  " + "0x{0:02x}".format(self.DataOut[1])    
    
    def ParseResponseStr(self, StrData):
        i=0
        DataIn=[0,0]
        if len(StrData)==2:
            for data in StrData:
                try:
                    DataIn[i] = ord(str(data))
                except ValueError:
                    DataIn[i] = 0
                i+=1
            
        else:
            DataIn=[0xFF,0xFF]
            
        self.ParseResponse(DataIn)
            
    def ParseResponse(self, DataIn):
        print DataIn
        if DataIn[0] & 0b10000000:
            self.Event=1
            self.PacketCount=((DataIn[0] & 0b01111111) * 0x100) + DataIn[1]
        else:
            self.Event=0
            if DataIn[1] & 0b00000001:
                self.Status=1
            else:
                self.Status=0
        
        if self.Verboise:
            if self.Event:
                print "Packet report with PacketCount= : " + str(self.PacketCount)
            else:
                print "Status message:"
                if self.Status: 
                    print "\t\tError"
                else:
                    print "\t\tSuccess"
    
    
    
