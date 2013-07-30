
class ErrorsDTM(Exception):
    #print "myException"  
    def __init__(self, value):
        print "Error Using DTM Classsss:"
        self.parameter = value
        
class FrequencyError(ErrorsDTM):
    def __init__(self, value):
        self.parameter = value
        print value
        if value<0:
            print "Frequency must be greater than 0, received: " + str(value) 
        elif value>39:
            print "Frequency must be less than 39, received: " + str(value) 
class PacketTypeError(ErrorsDTM):
    def __init__(self, value):
        self.parameter = value
        if value<0:
            print "Packet Type must be greater than 0, received: " + str(value) 
        elif value>3:
            print "Packet Type must be less than 3, received: " + str(value)       
            
class LengthError(ErrorsDTM):
    def __init__(self, value):
        self.parameter = value
        if value<0:
            print "Length must be greater than 0, received: " + str(value) 
        elif value>0x25:
            print "Length must be less than 37, received: " + str(value)                     
