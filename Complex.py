#Need to implement complex numbers.
#Will implement in the form of a + jB.
#This can be done with a list, 'a' is stored in first, 'B' is stored in second element.
#complex_number = [1,2] #this represents 1 + 2j.

import math

def complexAdd(*complex_numbers):
    '''Add n amount of complex numbers'''
    realBuffer = 0
    complexBuffer = 0
    for number in complex_numbers:
        realBuffer += number[0]
        complexBuffer += number[1]
    return [realBuffer, complexBuffer]

def complexSub(*complex_numbers):
    '''Substract n amount of complex numbers'''
    realBuffer = complex_numbers[0][0]
    complexBuffer = complex_numbers[0][1]
    for number in complex_numbers[1:]:
        realBuffer -= number[0]
        complexBuffer -= number[1]
    return [realBuffer, complexBuffer]

def complexMult(complex_number1, complex_number2):
    '''Multiply two complex numbers'''

    a = complex_number1[0]
    c = complex_number2[0]
    A = complex_number2[1]
    B = complex_number1[1]
    #Multiplication of (a+jA)(c+jB) simplifies into:
    realBuff =  a * c - A * B
    complexBuff = a * A + B * c

    return [realBuff, complexBuff]

def complexDiv(complex_number1, complex_number2):
    '''Divide two complex numbers: Arg1 / Arg2'''
    a = complex_number1[0]
    c = complex_number2[0]
    b = complex_number1[1]
    d = complex_number2[1]
    #division of (a + jb)/(c + jd) simplifies into:
    if (c != 0 or d != 0):
        realBuff = (a * c + b * d) / (c**2 + d**2)
        complexBuff = (b * c - a * d) / (c**2 + d**2)
        return [realBuff, complexBuff]
    else:
        return [float('nan'), float('nan')]

def complexAngle(complex_number):
    '''Calculate the angle of the vector between real and complex'''  
    if (complex_number[0] == 0 and complex_number[1] != 0): #prevent div by 0
        return math.copysign(90, complex_number[1]) 
    return math.degrees(math.atan(complex_number[1] / complex_number[0]))

def complexMagnitude(complex_number):
    '''Calculates magnitude of a single complex number'''
    return math.sqrt(complex_number[0]**2 + complex_number[1]**2)