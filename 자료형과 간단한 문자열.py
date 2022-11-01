# 자료형 복습
# 문자열 에서 출력에서 작은 따음표를 표시하고 싶을 때, 큰 따음표로 감싼다.
'''
a = "python's favorite code is C++"
print (a)
'''

# 큰 따음표를 표시하고 싶을때는 그 반대로
# 둘 다 표시하고 싶을 때는 ',"를 \로 해준다.
'''
a = 'python\'s favorite code is C++'
print (a)
'''

#줄을 바꾸는 경우

'''
print("보통 줄을 바꾸고 싶으면\n을 사용하는데")
a = """
multiline 을 사용하면
마음대로 줄을 바꿀 수 있다.
"""
print (a)

'''

# 그냥 알아두기 \ㅁ qpfthfl \b 백스페이스 \000 널문자

# 숫자열 연산 복습
"""
print("="*30)
print("nice to meet you")
print("="*30)
"""

#문자열 인덱싱
'''
a = "donotusespacebaranymore"
b = a[8:-7]
print(b)
'''
#result "spacebar" 8번 인덱스가 s -7번이면 a가 나와야하는데 r이 나옴 연산이 8 <= a < -7이여서 -8까지 result 도출

#문자열 포메팅 복슴
# %d %s %f 를 주로 쓴다 %d 는 integer %s 는 string %f 는 floating-point이다.
'''
a = 13
b = "i'm string"
print("it is %d o'clock right now and %s" %(a,b))
'''

# 정렬 %Ns N은 만들 문자열의 크기를 나타내고 가장 뒤에 넣음 f를 사용할 경우 0.Nf인데 소수점 몇자리까지 표현할지임
"""
a = 123.123124142345
print ("%10.3f" %a)
"""
# 문자열 포메팅 
'''
print("today is {date} and the weather is {weather}".format(date = 1, weather = "cloudy")
'''
# 포메팅을 활용한 정렬은 오른쪽 :> 왼쪽 :< 가운데 :^이다.
"""
a = "sort"
print("{0:<10}" .format(a))
print("{0:>10}" .format(a))
print("{0:^10}" .format(a))
# 콜론과 정렬위치를 정하는 자리 사이에 문자를 넣는다면 공백대신 문자로 가능(아마도 char인듯함.)

print("{0:?<10}" .format(a))
"""
# f를 이용한 문자열 포매팅
'''
name = "mino"
age = 13;
print(f"my name is {name} age is {age}")
'''
# f를 이용한 문자열 포메팅에서 .format 형태가 아닌 것으로도 가능
# 원래형식
"""
a = "{0:>10}" .format("sort")
print (a)
"""
# using f
"""
a = f"{'hi':<10}"
print (a)

a = "{0:!^12}" .format("python")
print (a)
"""

# 문자열 관련 function
# 전부다 변수.기능 형식
'''
a = "why do you have to go? i'm going to find really i'm live"
print(a.count('a')) #문자 a 갯수 세기
b = a.find('y') # y라는 문자가 처음 나오는 위치 찾기
# find 대신 index를 사용해도 가능함
# join 함수는 먼저 선언후에 문자열 (문자 사이에 , 삽입)
str = "abcd"
result = ",".join(str)
print(result)
'''
# 모든 문자를 대문자로 바꾸는건 upper, 반대로 소문자는 lower이다.

# 문자열 바꾸기(replace)
'''
a = "like i need you"
b = a.replace("you", "myself")
print(b)
'''

# 문자열 나누기(split)

a = "like i need you"
b = a.split()
print (b)