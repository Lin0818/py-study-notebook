# evaltime.py
from evalsupport import deco_alpha
from evalsupport import MetaAleph

print('<[1]> evaltime module start')

class ClassOne():
    print('<[2]> ClassOne body')
    
    def __init__(self):
        print('<[3]> ClassOne.__init__')
        
    def __del__(self):
        print('<[4]> ClassOne.__del__')
        
    def method_x(self):
        print('<[5]> ClassOne.method_x')
    
    class ClassTwo(object):
        print('<[6]> ClassTwo body')
        
@deco_alpha
class ClassThree():
    print('<[7]> ClassThree body')
    
    def method_y(self):
        print('<[8]> ClassThree.method_y')

class ClassFour(ClassThree):
    print('<[9]> ClassFour body')
    
    def method_y(self):
        print('<[10]> ClassFour.method_y')

class ClassFive(metaclass=MetaAleph):
    print('<[6]> ClassFive body')
    
    def __init__(self):
        print('<[7]> ClassFive.__init__')
        
    def method_z(self):
        print('<[8]> ClassFive.method_y')
        
class ClassSix(ClassFive):
    print('<[9]> ClassSix body')
    
    def method_z(self):
        print('<[10]> ClassSix.method_y')
    
if __name__ == '__main__':
    print('<[11]> ClassOne tests', 30 * '.')
    one = ClassOne()
    one.method_x()
    print('<[12]> ClassThree tests', 30 * '.')
    four = ClassFour()
    four.method_y()
    print('<[13]> ClassFive tests', 30 * '.')
    five = ClassFive()
    five.method_z()
    print('<[14]> ClassSix tests', 30 * '.')
    six = ClassSix()
    six.method_z()
