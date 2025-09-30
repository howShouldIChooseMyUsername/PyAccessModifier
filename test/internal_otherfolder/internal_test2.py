from PyAccessModifier import *

@internal
class Test3:
    def __init__(self):
        print("Internal Test")

    @internal
    def test(self):
        print("Internal Test in def")