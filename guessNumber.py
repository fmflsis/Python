import random

min = 1
max = 20
count = 0
guessNum = random.randint(min,max)

print('이름이 무엇인가요?')
Name = input() #입력받기

print('안녕하세요' + Name + '님' + str(min) +'에서' + str(max)+ '까지 숫자중 하나를 생각합니다.')

while True:   
    Num = int(input('맟춰보세요.\n'))
    if count<6 :
        if Num< guessNum : 
            print('그 수보다 큰수') 
            count = count + 1
        elif Num>guessNum: 
            print('그 수보다 작은수') 
            count = count + 1
        else:
            print('잘 맟췄어요!' + Name + '님' + str(count) + '번 만에 맟췄어요!')
            break
    else :
        print('You died')
        break       
        
