# 리스트는 대괄호로 감싼 모양에 요소들을 넣어준다
# 문자열(string)을 다룰때와 비슷함
# 리스트를 중첩하여 쓸 경우 (2차원) 중첩된 리스트 역시 요소임

# ex_1 A = [1,2,3,4,5]에서 [2,3]을 만들어보자

# sol)
'''
A = [1,2,3,4,5]
B = A[1:3] #3번째까지 가지 않기때문에 3까지

print(B)
'''
# 리스트 길이를 구하는 len
'''
a = [1,2,3,4,5,6]
print(len(a))
'''
# 리스트 관련 fuction del 객체 (remove 함수로도 가능하다.)
'''
a = [1,2,3,4,5,6]
del a[3:]
print(a)
'''

# 객채.append (insert 역시 가능하다.)
'''
a = [1,2,3,4,5]
a.append(1)
print(a)
#리스트에 리스트를 추가하는것 역시 가능하다.
'''
# sort 함수 역시 존재한다.
# reverse 는 리스트 안에 존재하는 요소들을 반대로 만들어준다.

# pop 함수 객채.pop(자리)
# 요소를 저장하고 리스트에서 삭제
'''
a = [1,2,3]
b = a.pop(2)
print(a, "\n", b)
'''
# 튜플(tuple)

# 튜플은 리스트와 달리 자료를 삭제,추가,변경 할 수 없다 나머지에는 차이 X

# 딕셔너리 자료형

# 기본 딕셔너리 자료형 {key1: value1, key2 : value2}

dic = {'name' : 'mino', 'phone' : '9420', 'birth' : "1234"}

print(dic)

# 딕셔너리 쌍 추가

dic[3] = 'hi'

print (dic)
# 이름으로 쌍 추가도 가능하다.
dic['height'] = 1234
print(dic)

del dic['height'] # 삭제
print (dic)


# value 얻기

print(dic['name'])

# 리스트나 튜플, 문자열에 해당하는 indexing 방식이 아님 key로 value
# 또한 key에는 동일한 이름을 사용할 수 X, 리스트역시 불가능(value O)

# 딕셔너리 key들의 리스트 만들기

dic_keys = dic.keys()
print(dic_keys)
# 여기서 dic_keys는 튜플안에 리스트가 있는 형태
# 리스트로만 바꾸려면..
b = list(dic.keys())
print (b)

# key, value 쌍 얻기
# dic.items()를 통해서 얻을 수 있다. list(dic.items()) 가능

# dic.clear() 전부다 삭제

