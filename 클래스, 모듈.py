# 만약 한 프로그램 안에서 계산기가 두개 필요하다면.. 코드는
'''
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1
def add2(num):
    global result2
    result2 += num
    return result2
    
'''
# 계산기 하나마다 같은 기능이지만 다른변수와 함수를 만들어야함

# 클래스를 활용한다면

'''
class Calcurlator:
    def __init__(self):
        self.result = 0
        
    def add(self,num):
        self.result += num
        return self.result
Cal1 = Calcurlator()
Cal2 = Calcurlator()
    
'''

# 사칙연산 계산기 만들기
'''
class FourCal():
    
    def setdata(self,first,second): # 클래스 안의 함수 : 메서드(method)
        self.first = first
        self.second = second
    
    def add(self):
        return self.first + self.second
    def times(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second
    def sub(self):
        return self.first - self.second
a = FourCal() #class FourCal에 대한 객체 생성
a.setdata(3,5) #self에는 a가 들어가고 3 : first, 5 : second
# 한 프로그램 안에서 두개의 값이 들어온다면

b = FourCal()
b.setdata(6,9)
print(b.times())

# 함수의 절차 객채 선언, 데이터셋(setdata), 메서드 설정
'''

# 생성자

# 원래는 객체를 생성하고 그다음 setdata를 통해서 데이터셋을 했다면
'''
class test_1():
    def setdata(self,first,second):
        self.first = first
        self.second = second
aa = test_1()
aa.setdata(1,2)
print(aa.first)
'''
# __init__을 통해서 바로 값을 넣을 수 있다.
'''
class fourcal():
    def __init__(self,first,second):
        self.first = first
        self.second = second
    def add(self):
        return self.first + self.second
    def div(self):
        return self.first / self.second

 # 객처를 생성하면서 값을 넣어줄 수 있음

# 클래스 상속

# 만약 위와 같은 사칙연산 뿐만 이니라 이미 만들어진 클래스에 상속시킨다면
class morecal(fourcal):
    def pow(self):
        return self.first ** self.second

# method 오버라이딩

# a = fourcal(4,0) # Error : division by zero
# print(a.div())

# 방법을 해결하기 위해서는 상속된 클래스에서 부모클래스의 함수명을 그대로 사용

class safediv(fourcal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = safediv(5,0)
print(a.div())
'''

# 모듈(module)

# import를 통해서 python 모듈을 사용할 수 있게 한다. 또한 함수를 사용하기 위해서는
# from 모듈이름 import 모듈함수로 사용한다.
# 여러 함수를 사용하고 싶은 경우에는 from 모듈이름*와 모듈함수를 , 로 구분지어 적음

# if__name__=="__main__":의 의미
'''
모듈을 실행할 때 안에 있는 함수만 사용할 수 있게 한다.
'''
'''
import mod1

a = 1
b = 2
print(mod1.add(1,2))
'''
'''
from mod1 import add

print(add(1,4))
'''
'''
# from mod1 import add,sub
from mod1 import *

print(add(1234,12312))
print(sub(123123,14231))
'''

# 만약 mod1에 print를 추가한 경우
# import만 한 경우에도 print가 됨
'''
import mod2

print(mod2.PI)

# 모듈안에 있는 클래스를 사용하고자 하는 경우에는
a = mod2.Math()
print(a.solv(4))
'''

