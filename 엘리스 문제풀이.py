'''
# 1번
card = []
red_pocket = []
blue_pocket = []
card_box = []

a = input()
b = a.split(" ")
card = [int(i) for i in b]
for i in card:
    if i >= 0:
        red_pocket.append(i)
    else:
        blue_pocket.append(i)
card_box.append(red_pocket)
card_box.append(blue_pocket)
print(card_box)

# 2번

H = int(input())
A = int(input())
B, C, D = input().split(" ")
B = int(B)
C = int(C)
D = int(D)
elice_rent = H*A
coding_rent = 0
if C > H:
    coding_rent = B
else:
    coding_rent = B + (H-C)*D
if elice_rent > coding_rent:
    print(coding_rent)
else:
    print(elice_rent)

'''
# 4번
'''
signal1 = {'a': 'n', 'b': 'd', 'c': 'a', 'd': 'b', 'e': 'e', 'f': 'l', 'g': 'j', 'h': 'o', 'i': 'z', 'j': 'u', 'k': 'y', 'l': 'v', 'm': 'w', 'n': 'q', 'o': 'x', 'p': 'r', 'q': 'p', 'r': 'f', 's': 'g', 't': 't', 'u': 'm', 'v': 'h', 'w': 'i', 'x': 'c', 'y': 'k', 'z': 's'}

signal2 = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}

def decode(code):
    a = code.split(" ")[0]
    b = code.split(" ")[1]
    text = ''
    for i in range(0, len(a)):
        if int(a[i]) == 0:
            text += signal1[b[i]]
        else:
            text += signal2[b[i]]
    return text

code = input()

text = decode(code)

print(text)


# 심화 문자의 빈도 조사하기

string = input()
alpha_cnt = {}

string =  # TODO: 문자열의 모든 문자를 소문자로 변환합니다.

for char in string:
    # TODO: 글자가 알파벳이라면 alpha_cnt 딕셔너리를 이용하여 그 횟수를 기록
    
    

# TODO: string의 첫번째 문자가 등장한 횟수를 출력
'''


# 심화 당근 탐지기
'''
carrot = input().split(" ")

rabbit = int(input())
rcount = 0
lcount = 0
for i in range(rabbit-1,-1,-1):
    if carrot[i] == "O":
        lcount +=1
        
for j in range(rabbit-1,5):
    if carrot[j] == "O":
        rcount += 1
        
    
if lcount > rcount:
    print("왼쪽")
elif lcount < rcount:
    print("오른쪽")
elif lcount == rcount:
    print("동일")
'''

# 심화 문자열 데이터 압축하기

def encode(text):
    code = ""  
    zip = 0
    for i in (0,len(text)-2):
        if text[i] == text[i+1]:
            zip += 1
        else:
            if zip >=3:
                code += text[i] + str(zip)
            elif zip <=2:
                code += text[i]*2
            zip = 0
            code += text[i]
    return code

text = input()

print(encode(text))
