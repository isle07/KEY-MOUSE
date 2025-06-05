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
#4의 23459759승 구하기(였던것, 밑 코드가 실행안되서 어쩔수없이 지움)↓
asdf = MoreFourCal(4, 2)
print(asdf.pow())
#4를 0으로 나누면 오류 발생, 아래 해결
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
ef = SafeFourCal(4, 0)
print(ef.div())

class Family:
    lastname = "김"

print(Family.lastname)

qwer = Family()
wert = Family()
print(str(qwer.lastname) + ' ,' + str(wert.lastname))

Family.lastname = '박'
print(qwer.lastname + ' ,' + wert.lastname)
#str 씌워도되고, 안씌워도됨
