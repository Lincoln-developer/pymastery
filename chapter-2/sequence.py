# A sequence is an object that implements __getitem__ and  __len__
# and can be iterated over. Examples are strings, tuples, lists

from collections.abc import Sequence

class Item(Sequence):
    """A wrapper around the standard library object
       Object:-> list
    """
    # constructor(
    #name, age
    #)
    def __init__(self, *values) -> None:
        self._values = list(values)
    
    def __len__(self):
        return len(self._values)
    
    def __getitem__(self, item):
        return self._values.__getitem__(item)

names = Item("Lincoln", "Ang", "Jane", "Gabriella", "Henry")
print(names[::])

