# x = 1
# y = float(2)
# z = str(3)
# print(x,int(y),z)
# # print(type(x),type(y),type(z))
# x = -10
# if x*2 > x:             #들여 쓰기를 잘 지켜야함
#     print("크다")
# else:
#     print("작거나 같다.")

#if 문
# name = '앨리스'
# if name == '앨리스':
#     print('반가워요' + name)
# print('종료')

#for 문 range

# for i in range(2, 10):
#     for n in range(1, 10):
#         print('{}x{}={}'.format(i, n, n*i),end=" ")
#     print()
    
'''  멀티 주석
예제 1    
a= "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

예제2
n = 0
value = 0
while n < 1000:
    n +=1
    
    if n%3 == 0:
        value += n    
    if n == 1000 : break
print(value)

예제3
n=1
while n<6:
    i=0
    while i<n:
        print('*',end="")
        i+=1   
    n+=1
    print()

#예제4
total = 0
A = [70,60,55,75,95,90,80,80,85,100]
for num in A:
    total += num
print(total) 
print(total/len(A))
''' #멀티 주석 끝
'''
#외부 모듈
import sys
print('헬로우')
sys.exit() # 프로그램 종료
print('헬로우') # 종료후 실행되지않음'''

'''
# 내부 함수
# 함수
def hello():
    print('하이!')
    print('안녕!')
    print('니 하오!')

hello()
hello()
hello()

#매개변수가 있는 함수
def hello(name):
    print('하이'+name)

hello('길동')
hello('펭수')

def add10(num):
    return num + 10

print(add10(1))
print(add10(2))

def is_odd(num):
    if num%2 == 0 : print('짝수')
    else : print('홀수')

is_odd(1)
is_odd(2)
is_odd(3)

def is_avg(*num):
    total = sum(num)
    print(total/len(num))

is_avg(1,3,6)
is_avg(1,7,8,2)
'''

# 전역 변수
# x = 10
# def foo():
#     print(x) #전역변수 출력

# foo()
# print(x) #전역변수 출력

# def spam():
#     eggs = 99
#     bacon()
#     print(eggs)

# def bacon():
#     ham = 101
#     eggs = 0

# spam()   

# 에러처리 try/except
# def div10(num) :
#     try:
#         return 10/num
#     except ZeroDivisionError : #무슨에러인지 알때 (0으로 나누면 안되는거)
#         print('에러: 0으로 나눌수 없음')
#     # except : 모를때 표기
#     # return 이 없는 함수는 none을 리턴
# print(div10(2))
# print(div10(0))
# print(div10(5))

# 리스트와 튜플 []. ()
# ham = ['개','고양이','박쥐','곰']
# ham [1:] #리스트 1번부터 끝까지
# ham [1:3] #리스트 1번부터 3까지
# ham [:2] #리스트 처음부터 2까지

#인덱스는 수정가능하나 문자열은 수정 불가능

#예제 1~2 숫자 소수 문자열 리스트가 들어있는 myList 생성
# myList =[1,1.1,'111',[1,2,3]]
# print(myList)
# print(type(myList[0]),type(myList[1]),type(myList[2]),type(myList[3]))

# # 문자열 바꾸기 replace
# a = "인생은 짧다."
# print(a.replace)
# print(a)

# 문자열 포매팅

# # %d 숫자
# number=7
# print('나는 도시락 %d 개를 먹었다.' %number)
# print('나는 도시락 %s 개를 먹었다.' %'여러')
# print("나는 도시락 %d 개를 %s 먹었다." % (7, '배터지게'))

# # 포맷 함수 format 이용
# print("나는 도시락 {} 개를 먹었다." .format('여러'))    #포맷 함수를 사용
# print("나는 도시락 {} 개를 먹었다." .format(1/2))

# #여러개 일때
# print("나는 도시락 {} 개를 {}먹었다." .format(3, '여러개 '))    #다중 괄호 적용
# print("나는 도시락 {1} 개를 {0}먹었다." .format(3, '여러개 '))  #괄호의 숫자 순서대로 들어감


# 파일 생성하기
# f = open('fruits.txt', encoding='utf-8')
# # print(f.read()) #커서가 있어서 두번 안 읽어짐
# content = f.read()
# f.close()
# print(content)      # 여러개 가능
# print(content)

#파일을 with 로 열기 (알아서 닫아줌)
# with open('fruits.txt', encoding='utf-8') as f:
#     content = f.read()

# print(content)
# print(content)


# # 파일 쓰기 (없으면 생성)
# with open('vegi.txt','w', encoding='utf-8') as f:
#     f.write('무\n')
#     f.write('배추\n')
#     f.write('토마토\n')
#     f.write('브로콜리\n')

# 파일 쓰기 (없으면 생성)
# with open('vegi.txt','a', encoding='utf-8') as f:
#     f.write('무\n')
#     f.write('배추\n')
#     f.write('토마토\n')
#     f.write('브로콜리\n')

# with open('vegi.txt','a+', encoding='utf-8') as f:
#     f.write('붙여쓰기\n')
#     f.seek(0) # 커서를 첫번째 줄로 이동
#     content = f.read()

# print(content)
# with open('fruits.txt', encoding='utf-8') as a:
#      content1 = a.read()

# with open('vegi.txt', encoding='utf-8') as b:
#      content2 = b.read()

# with open('fruitVegi.txt','a+', encoding='utf-8') as f:
#     f.write(content1)
#     f.write(content2)
#     f.seek(0) # 커서를 첫번째 줄로 이동
#     content = f.read()
# print(content)

# 무한 반복 파일 읽어오기
import time #시간 조절

while True:
    with open('vegi.txt', encoding='utf-8') as f:
        print(f.read())
        time.sleep(1) #초당 단위