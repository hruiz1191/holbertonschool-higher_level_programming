#!/usr/bin/python3


class CountedIterator:
    """Class to mimic iter"""
    def __init__(self, data):
        self.data = iter(data)
        self.counter = 0

    def get_count(self):
        """returns count"""
        return self.counter

    def __next__(self):
        """override __next__"""
        try:
            item = next(self.data)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
