import json
import difflib
#데이타 변수에 제이슨파일 딕셔너리 형태로 로드
data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]    
    elif word.upper() in data:
        return data[word.upper()]    
    else :
        sim = difflib.get_close_matches(word ,data)
        for i in sim :
            print('찾으시는게 이것 입니까?(y/n)\n'+ i)
            y = input()
            if(y == 'y'):
                    return data[i]
            
        return '그런 단어는 없습니다.'
   
            

word = input("영어 단어 입력: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)


#         return items[items.index(i):]

