import numpy as np


class ArrayList:
    def __init__(self):
        self.elems = [None, None]

    def append(self, value):
        for elem in self.elems:
            if elem == None:
                elem == value
            else:
                for i in range(len(self.elems)):
                    self.elems.append(None)

    def get(self, index):
        pass

    def length(self):
        counter = 0
        for elem in self.elems:
            if elem is not None:
                counter += 1
            else:
                pass
        return counter


if __name__ == "__main__":
    list = ArrayList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
