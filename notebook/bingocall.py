#bingocall.py
import random

class BingoCage:
    """BingoCage is a class trying callable, it is replace operate ()"""
    def __init__(self, items):
        # items, any iterable
        self._items = list(items)
        random.shuffle(self._items)  #乱序

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick form empty BingoCage')

    def __call__(self):  #callable, shortcut to bingo.pick()
        return self.pick()

Bingo = BingoCage(range(3))
Bingo.pick()
