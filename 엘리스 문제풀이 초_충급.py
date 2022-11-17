'''
# 말썽쟁이 도도새

# 지시사항을 참고하여 코드를 작성하세요.

def vomit(food):
    t = 0
    for i in food:
        if i == "웩":
            return t
        else:
            t += 1
            
# 값을 확인하기 위한 코드입니다. 값을 변경해가며 테스트해 보세요!
print(vomit(['과자', '과자', '과자', '커피', '과자', '웩', '음료수', '음료수', '과자', '커피', '커피', '커피']))
'''

# 중급 구슬꾸러미 (질문할 것)
'''
red = 250
blue = 40
white = 10
a = int(input())
count = 0
while True:
    if a >= red:
        a -= red
        count += 1
    if a >= blue:
        a -= blue
        count += 1
    if a >= white:
        a -= white
        count += 1
    if a == 0:
        print(count)
        break;
    else:
        print(-1)
        break;
'''

# 중급 마천루
'''
a = int(input())
if a < 6:
    for i in range(1,a+1):
        print("*"*i)
else:
    for i in range(1, 6):
        print("*"*i)
    for j in range(1,a-4):
        print("*"*5)
'''

# 중급 문자열 앞뒤 검사하기
'''
a = input()
for i in range(0,int((len(a)/2))):
    if a[i] == a[-i-1]:
        print("Same")
    else:
        print("Different")
'''     

# 중급 커피전문점 수타박수입니다!
'''
ame = 4100
cafe = 4600
caramel = 5100
sum = 0
guest = int(input())

for i in range(0, guest):
    menu = str(input())
    if menu == "아메리카노":
        sum += ame
    elif menu == "카페라떼":
        sum += cafe
    else:
        sum += caramel
print(sum)
'''

# 중급 더치페이 계산하기
'''
menu={"떡볶이":5000,
"김밥":2000,
"튀김세트":3000,
"순대":4000,
"라면":6000,
"콜라":1000,
"사이다":1000
}
a=0 # A가 먹은 금액
b=0 # B가 먹은 금액
c=0 # C가 먹은 금액

k=0 # 함께 먹은 금액


while True:
    div = input()
    if len(div) == 2:
        if int(div) == -1:
            break
    my_list = div.split(",")
    la = my_list
    if la[0] == "A":
        if la[1] in menu:
            a += menu[la[1]]*int(la[2])
    if la[0] == "B":
        if la[1] in menu:
            b += menu[la[1]]*int(la[2])
    if la[0] == "C":
        if la[1] in menu:
            c += menu[la[1]]*int(la[2])
    if la[0] == "K":
        if la[1] in menu:
            k += menu[la[1]]*int(la[2])

k = k // 3   # 함께 먹은 금액은 세명이 동등하게 나누어 냄

a+=k
b+=k
c+=k

print ('A',a)
print ('B',b)
print ('C',c)
'''

# 중급 좋아하는 숫자만 골라내기
'''
num_tuple = ('2','3','5','6','7','8','9')
result = []

text = input()

for i in text:
    if i in num_tuple:
        result.append(i)
    if len(result) == 5:
        break  

print(result)
'''

# 중급 잘린 피라미드 만들기
'''
text = input() # 지시사항 1번

start = int(text.split(',')[0])
end = int(text.split(',')[1])
if end > 15:
    end = 15
if start >= end or start >= 15:
    print("오류")
else:
    for i in range(start, end+1):
        print(i*("*"))
'''

# 중급 겹치는 구간 찾기

amin = int(input())
amax = int(input())
bmin = int(input())
bmax = int(input())

amin 