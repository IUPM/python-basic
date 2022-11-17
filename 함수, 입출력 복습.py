# 매개변수를 2개 받고 값을 return 하는 경우
'''
def add(a,b):
    return a+b

print(add(1,2))
'''

# 매개변수가 없는 경우도 존재한다
'''
def nothing():
    print("haha")
    
nothing()
'''

# 매개변수의 값을 미리 default로 설정도 가능하다
'''
def test(a,b,c=4):
    return a+b+c


print(test(1,2))
'''

# 여러 개의 입력값을 받는 함수 만들기
'''
def add_many(*args): #굳이 args일 필요는 없지만 관례상.. for i 비슷한 느낌
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1,2,3,4,5,12,2,2,3,1,2,3,3,2,1)
print(result)
'''


# keyword 파라미터
'''
def print_kwargs(**kwargs): #그대로 딕셔너리를 만들수 있음
    print(kwargs)
    
print_kwargs(a=1) # key는 a, value는 1이 된다.
'''

# return 값은 언제나 하나
'''
def return_tuple(a,b):
    return a+b,a*b

print(return_tuple(3,4))
'''

# 파일 읽고 쓰기 
'''
f = open("새파일.txt", "w") # Git_test에 파일이 생성됨
f.close() # 파일 닫기
'''
# 모드로는 "w" : write 쓰기, "r" : read 읽기, "a" : add 추가하기 가 있다.
'''
f = open("D:/새파일.txt", "w")
for i in range(1,11):
    data = "%d번째 줄입니다 \n"%i
    f.write(data)
f.close()

for i in range(1,11):
    data = "%d번째 줄입니다 \n"%i
    print(data)    
'''
# f를 이용한 출력과 다른점은 txt에 적는것은 줄바꿈을 수동으로 해줘야함

# readline 관련
'''
f = open("D:/새파일.txt", "r")
while True:
    line = f.readline() # 한줄씩 받으면서 line변수에 저장함
    if not line : break
    print(line)
f.close()
'''

# readlines 함수 사용하기
'''
f = open("D:/새파일.txt", "r")

lines = f.readlines() # lines에 리스트형태로 읽어들임
for line in lines:
    print(line)
f.close()
'''

# read 함수 사용
'''
f = open("D:/새파일.txt", "r")
data = f.read() # 파일의 내용 전체를 문자열로 되돌려준다.
print(data)
f.close()
'''


