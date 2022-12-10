import Complex
inputs = [[1,1], [0,0], [10,10]]
#Answers verified using wolfram alpha.

def AdditionTest():
    testPassed = 0
    if Complex.complexAdd(inputs[0],inputs[1]) == [1,1]:
        testPassed += 1
    if Complex.complexAdd(inputs[0],inputs[2]) == [11,11]:
        testPassed += 1
    if(testPassed == 2):
        print("Addition test passed")
    else:
        print("Addition test failed")

def SubTest():
    testPassed = 0
    if Complex.complexSub(inputs[1],inputs[0]) == [-1,-1]:
        testPassed += 1
    if Complex.complexSub(inputs[2],inputs[0]) == [9,9]:
        testPassed += 1
    if(testPassed == 2):
        print("Subtraction test passed")
    else:
        print("Subtraction test failed")

def multTest():
    testPassed = 0
    if Complex.complexMult(inputs[1],inputs[0]) == [0,0]:
        testPassed += 1
    if Complex.complexMult(inputs[2],inputs[0]) == [0,20]:
        testPassed += 1
    if(testPassed == 2):
        print("Multiplication test passed")
    else:
        print("Multiplication test failed")
print(Complex.complexDiv(inputs[0],inputs[1]))

def DivTest():
    testPassed = 0
    if Complex.complexDiv(inputs[1],inputs[0]) == [0,0]:
        testPassed += 1
    if Complex.complexDiv(inputs[0],inputs[1]) != Complex.complexDiv(inputs[0],inputs[1]): #division by 0, compare if NaN
        testPassed += 1
    if Complex.complexDiv(inputs[2],inputs[0]) == [10,0]:
        testPassed += 1
    if(testPassed == 3):
        print("Division test passed")
    else:
        print("Division test failed")

def angleTest():
    testPassed = 0
    if(Complex.complexAngle([1,1]) == 45): #normal calculation test
        testPassed += 1
    if(Complex.complexAngle([-1,1]) == -45): #negative angle test
        testPassed += 1
    if(Complex.complexAngle([0,1]) == 90): #division by zero test
        testPassed += 1
    
    if(testPassed == 3):
        print("Angle test passed")
    else:
        print("Angle test failed")    

def magnitudeTest():
    testPassed = 0
    if(Complex.complexMagnitude([3,4]) == 5): 
        testPassed += 1
    if(Complex.complexMagnitude([-3,-4]) == 5): 
        testPassed += 1
    
    if(testPassed == 2):
        print("Magnitude test passed")
    else:
        print("Magnitude test failed")  


AdditionTest()
SubTest()
multTest()
DivTest()
angleTest()
magnitudeTest()
