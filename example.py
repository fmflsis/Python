#예제 1
# def mult_two(a,b):
#     return a*b

# if __name__ == '__main__':
#     print(mult_two(3,2))
#     print(mult_two(1,0))


# #ex2
# def easy_unpack(elements):
#     return elements[0],elements[2:3],elements[-2:-1]

# if __name__ == '__main__':
#     print(easy_unpack((1,2,3,4,5,6,7,9)))
#     print(easy_unpack((1,1,1,1)))
#     print(easy_unpack((6,3,7)))




# #ex3
# def first_word(text):
#     return text.split()[0]

# if __name__ == '__main__':
#     print(first_word("Hello world"))


# #ex4
# def is_acceptable_password(password):
#     if len(password)<7 : return False
#     else : return True
    

# if __name__ == '__main__':
#     print(is_acceptable_password('short'))
#     print(is_acceptable_password('muchlonger'))
#     print(is_acceptable_password('ashort'))


# #ex5    
# def number_length(a):
#     return  len(str(a))

# if  __name__ == '__main__'   :
#     print(number_length(10))
#     print(number_length(0))
#     print(number_length(4))
#     print(number_length(44))


#ex6

# def backward_string(val):
#     return val[::-1]

# if __name__ == '__main__':
#     print(backward_string('val'))
#     print(backward_string(''))
#     print(backward_string('ohho'))
#     print(backward_string('123456789'))

#ex7

# def remove_all_before(items, i):
#     if i in items :
#         return items[items.index(i):]
#     else:
#         return items    

# if __name__ == '__main__':
#     print(list(remove_all_before([1, 2, 3, 4, 5], 3)))
#     print(list(remove_all_before([1, 1, 2, 2, 3, 3], 2)))
#     print(list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)))
#     print(list(remove_all_before([1, 1, 5, 6, 7], 2)))
#     print(list(remove_all_before([], 0)))
#     print(list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)))

# def is_all_upper(text):
#     if text.upper() == text:
#         return True
#     else:
#         return False

# if __name__ == '__main__':
#     print(is_all_upper('ALL UPPER'))
#     print(is_all_upper('all lower'))
#     print(is_all_upper('mixed UPPER and lower'))
#     print(is_all_upper(''))

# ex9 
def replace_first(items):
    if len(items) > 1:
        items.append(items.pop(0))

    return items

if __name__ == '__main__' :
    print(list(replace_first([1, 2, 3, 4])))
    print(list(replace_first([1])))
    print(list(replace_first([])))
    
#ex10
def max_digit(number):

    return max(str(number))

if __name__ =='__main__':
    print("Example:")
    print(max_digit(0))
    print(max_digit(52))
    print(max_digit(634))
    print(max_digit(1))
    print(max_digit(10000))

