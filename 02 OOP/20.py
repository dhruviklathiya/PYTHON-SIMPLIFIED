# Multilevel inheritance
class level0:
    def __init__(self,attribute1,attribute2,attribute3):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = attribute3
    def get_info(self):
        return f"Attribute1 is {self.attribute1}, Attribute2 is {self.attribute2}, Attribute3 is {self.attribute3}, Attribute4 is {self.attribute4}, Attribute5 is {self.attribute5}, Attribute6 is {self.attribute6}, Attribute7 is {self.attribute7}, "

class level1(level0):
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5):
        super().__init__(attribute1,attribute2,attribute3)
        self.attribute4 = attribute4
        self.attribute5 = attribute5

class level2(level1):
    def __init__(self,attribute1,attribute2,attribute3,attribute4,attribute5,attribute6,attribute7):
        super().__init__(attribute1,attribute2,attribute3,attribute4,attribute5)
        self.attribute6 = attribute6
        self.attribute7 = attribute7

subchild = level2(1,2,3,4,5,6,7)
print(subchild.get_info())