
class ErrorsDTM(Exception):
    #print "myException"  
    def __init__(self, value):
        print "Error Using DTM Classsss:"
        self.parameter = value
        
class FrequencyError(ErrorsDTM):
    def __init__(self, value):
        self.parameter = value
        if value<0:
            print "Frequency must be greater than 0, recieved: " + str(value) 
        elif value>39:
            print "Frequency must be less than 39, received: " + str(value) 
        
