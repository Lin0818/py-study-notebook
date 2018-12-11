#implements a class StrKeyDict0 
import collections

class StrKeyDict0(dict):  #StrKeyDict0 inherits from dict.
    
    def __missing__(self, key):
        if isinstance(key, str):  #Check whether key is already a str. If it is, and it's missing, raise KeyError.
            raise KeyError(key)
        return self[str(key)]  #Build str from key and look it up
    
    def get(self, key, default=None):
        try:
            return self[key] 
        except KeyError:
            return default
    
    def __contain__(self, key):
        return key in self.keys() or str(key) in self.keys()

class StrKeyDict(collections.UserDict):
    
    # key not in dict
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]
    
    # key in dict
    def __contains__(self, key):
        return str(key) in self.data
    
    # d[key] = item
    def __setitem__(self, key, item):
        self.data[str(key)] = item

d = StrKeyDict0([('2', 'two'), ('4', 'four')])

print(d['2'])
#print(d[1])
print(d['4'])
print(d[4])
#print(d['1'])
print('2'in d)
