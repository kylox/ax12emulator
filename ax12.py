class Ax12:

    register = [12,0,0,1,1,250,0,0,255,3,70,60,140,255,3,2,36,36,0,0,1,1,32,32
            ,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,0] #the ax  register 50 
    current_register = []

    #initialisation of the ax register code in the hard way

    def init():
        current_register = register

    #global interaction with the ax12 register

    def getID ():
        return register[3]
    def setID (newID):
        register[3] = newID

    def getBaudRate():
        return register[4]
    def setBaudRate(newBaud):
        register[4]= newBaud

    def getReturnDelay():
        return register[5]
    def setReturnDelay(newReturnDelay):
        register[5] = newReturnDelay

    def getCWAngleLimitLow():
        return register[6]
    def setCWAngleLimitLow(new):
        register[6] = new

    def getCWAngleLimitHigh():
        return register[7]
    def setCWAngleLimitHigh(new):
        register[7] = new

    def getCCWAngleLimitLow():
        return register[8]
    def setCCWAngleLimitLow(new):
        register[8] = new

    def getCCWAngleLimitHigh():
        return register[9]
    def setCCWAngleLimitHigh(new):
        register[9] = new

    def getGoalPositionL():
        return register[25]
    def setGoalPositionL(goal):
        register[25] = goal

    def getGoalPositionH():
        return register[26]
    def setGoalPositionH(goal):
        register[26] = goal

    def getPresentPositionL():
        return register[31]
    def setPresentPositionL(pos):
        register[31] = pos

    def getPresentPositionH():
        return register[32]
    def setPresentPositionH(pos):
        register[32] = pos
    #usefull fonction

    #move to an anlge between 0 to 300 
    def move(pos):
        realpos = pos*1023/300
        if( realpos > 2047 or realpos < 0):
            print ("error : value not in bounds : position between 0 and 300")
        elif (realpos < 1023):
            print ("rotating counterclockwise...")
            if (realpos < 256):
                setGoalPositionL(realpos)
            else:
                setGoalPositionL(realpos & 6)
                setGoalPositionH(realpos & 4)
                print (hex(getGoalPositionL()))
                print (hex(getGoalPositionH()))




