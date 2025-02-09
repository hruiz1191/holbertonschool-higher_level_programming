#!/usr/bin/python3
__import__("sys")


class VerboseList(list):
    """List modifying Class"""
    
    
    def append(self, object) :
        print(f"Added [{object}] to the list.")
        return super().append(object)

    def extend(self, iterable):
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)
    
    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        return super().remove(value)
    
    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
