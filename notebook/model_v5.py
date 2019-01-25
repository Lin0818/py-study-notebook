#LineItem take#5
# model_v5.py
import abc

class AutoStorage:
    __counter = 0
    
    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1
        
    def __get__(self, instance, owner):
        if instance is None:
            return self
        else: 
            return getattr(instance, self.storage_name)
        
    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)
        
class Validated(abc.ABC, AutoStorage):
    
    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)
        
    @abc.abstractmethod
    def validate(self, instance, value):
        """return validated value or raise ValueError"""
        
class Quantity(Validated):
    """a number greater than zero"""
    
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value
    
class NonBlank(Validated):
    """a string with at least one character"""
    
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value
