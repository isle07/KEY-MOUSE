class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 8)
print(a.add())
print(b.add())
print(a.sub())
print(b.sub())
print(a.mul())
print(b.mul())
print(a.div())
print(b.div())