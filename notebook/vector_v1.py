#vector_v1.py
#multi-dimensional Vector class
from array import array
import reprlib
import math

class Vector:
    typecode = 'd'
    
    def __init__(self, components):
        self.__components = array(self.typecode, components)
        self._score = 3

    @property
    def score(self):
        return self._score
        
    def __iter__(self):
        return iter(self.__components)
    
    def __repr__(self):
        components = reprlib.repr(self.__components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)
    
    def __str__(self):
        return str(tuple(self))
    
    def __bytes(self):
        return (bytes([ord(self.typecode)]) + 
               bytes(self.__components))
    
    def __eq__(self, other):
        return tuple(self) == tuple(other)
    
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))
    
    def __bool__(self):
        return bool(abs(self))
    
    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)
