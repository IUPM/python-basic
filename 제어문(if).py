# if문 복습

# 들여쓰기에 주의할 것, 조건문이 끝나면 :

# 만약 3000원 이상의 돈을 가지고 있다면 택시를 타고 그렇지 않으면 걸어가라
'''
money = 2000
if money >= 3000:
    print("get a taxi")
else:
    print("Just work")
'''
# x가 S에 있는가?에서 x in S로 표현 가능함 x not in S도 물론 가능

# 조건문에서 아무것도 없이 넘어가려면 pass를 쓰면 된다.
'''
money = 4000
if money >= 3000:
    pass
else:
    print("Just work")
'''
# while 문 복습 시작
'''
tree_hit = 0

while(tree_hit <= 10):
    print("나무를", tree_hit, "번 찍었습니다")
    tree_hit += 1
print("나무 쓰러집니다")
'''
# 여러 선택지중 입력받는 예제
'''
prompt = """
1. Add
2. Del
3. List
4. Quit
"""
while 1:
    print(prompt)
    num = int(input())
    if num == 4:
        print("thx for your ")
        break;  #while을 끝내고 싶은 경우
    else:
        continue; # while의 처음으로 돌아가고 싶은 경우
'''
# Ctrl + C 를 누르면 무한루프 탈출 가능

# for 문

# 5명이 시험을 봤을 때 60점을 넘으면 합 못 넘으면 불합
'''
marks = [90, 25, 67, 45, 80]
num = 0
for i in marks:
    if i > 60:
        print("%d student is pass" %(num + 1))
    else:
        print("%d student is fail" %(num + 1))  
    num += 1
'''
# for문에서 역시 continue를 사용할 수 있다.

# range 함수는 범위 (1,10)일 경우 9까지

# range를 활용한 for문
'''
add = 0
for i in range(1, 11):
    add += i
print(add)
'''
# 리스트 내포(리스트 안에서 for문과 if문 가능)
""" 리스트 안에 있는 숫자들을 *3 (with for문)
for num in a:
    result.append(num*3)
print(result)
"""
''' 위와 같은 기능이지만 리스트 내포를 사용
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)
'''

# 리스트 내포(if 문을 같이 활용하는 경우)
'''
a = [1,2,3,4]
result = [num * 3 for num in a if num%2==0]
print(result)
'''
# 또한 리스트의 자료형들을 바꾸고 싶을때도 가능하다

a = ['1', '2', '3', '4']
b = [int(i) for i in a]
print(b)
# 원래 코드
c = ['1', '2', '3', '4']
d =  []
'''
for i in range(0,len(c)):
    d.append(int(c[i]))
print(d)
'''
for i in c:
    d.append(int(i))
print(d)