import sys
sys.set_int_max_str_digits(999999999)
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
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
    
a = FourCal(4, 2)
b = FourCal(3, 8)
print(a.add())
print(b.add())
print(a.sub())
print(b.sub())
print(a.mul())
print(b.mul())
print(a.div())
print(b.div())

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
#4의 23459759승 구하기↓
asdf = MoreFourCal(4, 23459759)
print(asdf.pow())