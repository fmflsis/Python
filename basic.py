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
'''
def is_avg(*num):
    total = sum(num)
    print(total/len(num))

is_avg(1,3,6)
is_avg(1,7,8,2)

