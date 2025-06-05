class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

a = FourCal()
a.setdata(4, 2)
b = FourCal()
print(a.first)
b.setdata(3, 7)
print(b.first)
print(a.first)
