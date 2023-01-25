# 랜덤 비밀번호 생성기
# 1. 8~12자리 비밀번호
# 2. 영어대문자,소문자,특수기호가 포함

'''import string as s
import random as ran

def ran_password_generator():
    password = ''
    letter_count = ran.randrange(8, 13) # 자리 수
    temp_list = list(range(letter_count)) 
    
    total_string = s.ascii_letters + s.punctuation # 전체 경우의 수
    
    for one in temp_list:
        password = password + ran.choice(total_string)
    
    print(password)

ran_password_generator()'''

# 랜덤 비밀번호 생성기
# 1. 8~12자리 비밀번호
# 2. 영어대문자,소문자,특수기호가 포함
# 3. 특수기호는 이왕이면 적게 사용되도록 확률 조정

'''import string as s
import random as ran

def ran_password_generator():
    password = '' # 준비
    letter_count = ran.randrange(8, 13) # 자리 수
    letter_or_symbol = [0,1] # 0 = 알파벳, 1 = 특수기호
    for temp in range(letter_count): # 자리별로 알파벳/특수기호 선택해서 넣기
        type_choice = ran.choices(letter_or_symbol, weights = (80, 20)) # 확률 조정, 알파벳 = 80%, 특수기호 = 20%
        if type_choice == [0]:
            password = password + ran.choice(s.ascii_letters)
        elif type_choice == [1]:
            password = password + ran.choice(s.punctuation)
    print(password)
ran_password_generator()''' 


# 압축 파일 생성기
# 1. 반복된 문자가 있으면 이를 압축
# 예) aaaabbbcccdddd -> a4b3c3d4
# 2. 패턴 또한 압축
# 예) a4b3c3d4는 abcd순서대로 나열되었으므로, A4334D 이렇게 표현
# Cf) 원래는 통해 영어 소문자로만 표현된 무작위 1000자리를 압축하려고 했지만, 반복되는 알파벳이 많지 않아서 재익씨가 예시로 준 배열 사용하기로 함
'''for one in range(999):
        ran_string = ran_string + ran.choice(s.ascii_letters)'''

import string as s  # 패키지 import
import random as ran

def alzip(): 
    ran_string = input('Please enter your string: ') # 압축할 str 받기

    sep_index = [] # 비어있는 list 준비
    length = len(ran_string)
    for index in range(0, length-1): # range내에 len(ran_string)-1를 넣어서 range(0, len(ran_string)이라고 하면 오류 발생
        if ran_string[index] != ran_string[index+1]: # 만약에 앞이랑 뒤에 글자랑 일치하지 않으면
            sep_index.append(index) # 일치하지 않는 부분 인덱스 기록 ex) aaaabbbcccdddd는 [3, 6, 9]

    space_list =[] # 비어있는 list 준비
    ran_string = ran_string + ' ' # for index2~에서 index가 넘어가지 않도록
    sep_index.append(length-1) # 마지막 자리 추가
    select_beg = ran_string[0:sep_index[0]+1] # 만약 aaaabbbcccdddd이라면 aaaa 추가
    space_list.append(select_beg)
    length2 = len(sep_index)
    for index2 in range(1 , length2): # 만약 aaaabbbcccdddd이라면 bbb, ccc, dddd로 쪼개서 추가
        letter_number = sep_index[index2]
        select = ran_string [sep_index[index2-1]+1 : sep_index[index2]+1] 
        space_list.append(select) # 만약 aaaabbbcccdddd이라면 space_list = ['aaaa', 'bbb', 'ccc', 'dddd']

    for each in space_list: # 길이 추가
        count = len(each)
        space_list.append(str(count)) # 나중에 합하기 위해 str, 만약 aaaabbbcccdddd이라면 space_list = ['aaaa', 'bbb', 'ccc', 'dddd', '4', '3', '3', '4']

    length3 = int(len(space_list)/2) # 알파벳 묶음의 첫 글자만 선택, 만약 aaaabbbcccdddd이라면 'a' 'b' 'c' 'd'
    for pick in range(0, length3): 
        space_list[pick] = space_list[pick][0]

    temp_list = [] # 첫 글자 알파벳 + 매칭되는 뒤의 숫자
    for pick in range(0, length3):
        combine = space_list[pick] + space_list[length3 + pick]
        temp_list.append(combine)

    final = '' # alizip으로 결합1 
    for one in temp_list:  
        final = final + one

    final2 = '' # pattern으로 결합 2
    final2 = space_list[0].upper()
    for one2 in space_list:
        if one2.isdigit() is True:
            final2 = final2 + one2
    final2 = final2 + final[-2].upper()

    print('Alzip code is:', final)
    print('Pattern is:', final2)

alzip()


'''        space_string = ran_string[0:index2+1] + ' ' + ran_string[index2+1:]
        for index3 in sep_index:
            index3 = index3 + 1
'''