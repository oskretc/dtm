from ErrorsDTM import ErrorsDTM
from ErrorsDTM import FrequencyError

class DTM:
    """Class DTM
    """
    # Attributes:
    Frequency = 2  # (int8) 
    Length = None  # (int8) 
    PacketType = None  # (int8) 
    PayloadSize = None  # (int8) 
    Event = None  # (bool) 
    Status = None  # (bool) 
    DataOut = [0 , 0]  # (Array) 
    DataIn = None  # (Array) 
    __Command = None  # () 
    

    # Operations
    def SetFrequency(self, Freq):
        """function SetFrequency
        
        Freq: 
        
        returns 
        """
        Freq=Freq & 0b00111111
        if (Freq<=39 & Freq>=0):
            self.Frequency=Freq & 0b00111111
        else: 
            raise FrequencyError(Freq)
        
        
        return None # should raise NotImplementedError()
    
    def SetPacketType(self, PacketType):
        """function SetPacketType
        
        PacketType: 
        
        returns 
        """
        self.PacketType=PacketType & 0b00000011
        return None # should raise NotImplementedError()
    
    def SetPayloadSize(self, PayloadSize):
        """function SetPayloadSize
        
        PayloadSize: 
        
        returns 
        """
        self.PayloadSize=PayloadSize & 0b00111111
        return None # should raise NotImplementedError()
    
    def Send(self):
        """function Send
        
        returns 
        """
        return self.DataOut # should raise NotImplementedError()
    
    def StartTXTest(self, Freq, PayloadSize, PacketType):
        """function StartTXTest
        
        returns 
        """
        self.Command=0b1000
        self.SetFrequency(Freq)
        self.SetPayloadSize(PayloadSize)
        self.SetPacketType(PacketType)
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def StartRXTest(self, Freq, PayloadSize, PacketType):
        """function StartRXTest
        
        returns 
        """
        self.Command=0b0100   #01XX
        self.SetFrequency(Freq)
        self.SetPayloadSize(PayloadSize)
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
        self.PayloadSize=0       
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def Reset(self):
        """function Reset
        
        returns 
        """
        self.Frequency=0
        self.PacketType=0
        self.PayloadSize=0
        self.Command=0
        self.__CalculateTransaction()
        return None # should raise NotImplementedError()
    
    def __CalculateTransaction(self):
        """function CalculateTransaction
        
        returns 
        """
        self.DataOut[0]=(self.Command<<4) | self.Frequency
        self.DataOut[1]=(self.PayloadSize<<2) | self.PacketType
        return None # should raise NotImplementedError()
    

