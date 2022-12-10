import Complex
inputs = [[1,1], [0,0], [10,10]]
# Answers verified using wolfram alpha.

class TestComplex:

    def test_addition(self):
        assert Complex.complexAdd(inputs[0],inputs[1]) == [1,1]
        assert Complex.complexAdd(inputs[0],inputs[2]) == [11,11]

    
    def test_sub(self):
        assert Complex.complexSub(inputs[1],inputs[0]) == [-1,-1]
        assert Complex.complexSub(inputs[2],inputs[0]) == [9,9]

    def test_mult(self):
        assert Complex.complexMult(inputs[1],inputs[0]) == [0,0]
        assert Complex.complexMult(inputs[2],inputs[0]) == [0,20]

    
    def test_div(self):
        assert Complex.complexDiv(inputs[1],inputs[0]) == [0,0]
        assert Complex.complexDiv(inputs[0],inputs[1]) != Complex.complexDiv(inputs[0],inputs[1]) #division by 0, compare if NaN
        assert Complex.complexDiv(inputs[2],inputs[0]) == [10,0]


    
    def test_angle(self):
        assert Complex.complexAngle([1,1]) == 45 #normal calculation test
        assert Complex.complexAngle([-1,1]) == -45 #negative angle test
        assert Complex.complexAngle([0,1]) == 90 #division by zero test

   
    def test_magnitude(self):
        assert Complex.complexMagnitude([3,4]) == 5.0
        assert Complex.complexMagnitude([-3,-4]) == 5.0
        
