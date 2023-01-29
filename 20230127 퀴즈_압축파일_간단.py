# 압축 파일 생성기
# 1. 반복된 문자가 있으면 이를 압축
# 예) aaaabbbcccdddd -> a4b3c3d4
# 2. 패턴 또한 압축
# 예) a4b3c3d4는 abcd순서대로 나열되었으므로, A4334D 이렇게 표현
# Cf) 원래는 통해 영어 소문자로만 표현된 무작위 1000자리를 압축하려고 했지만, 반복되는 알파벳이 많지 않아서 재익씨가 예시로 준 배열 사용하기로 함


import string as s  # 패키지 import
import random as ran

def alzip(): 
    ran_string = input('Please enter your string: ') # 압축할 str 받기

    sep_index = [index for index in range(0, len(ran_string)-1) if ran_string[index] != ran_string[index+1]] # 뒷 알파벳과 일치X 인덱스 기록 ex) [3, 6, 9]
    sep_index.insert(0,-1) # 첫자리 추가
    sep_index.append(len(ran_string)-1) # 마지막 자리 추가

    alzip_result = ''
    pattern_result = ''
    for index2 in range(1 , len(sep_index)): # 만약 aaaabbbcccdddd이라면 bbb, ccc, dddd로 쪼개서 추가
        select = ran_string [sep_index[index2-1]+1 : sep_index[index2]+1] 
        alzip_result = alzip_result + select[0] + str(len(select))
    
    pattern_result = pattern_result + alzip_result[0].upper()
    for each in alzip_result:
        if each.isdigit() is True:
            pattern_result = pattern_result + each
    pattern_result = pattern_result + alzip_result[-2].upper()

    print('Alzip code is:', alzip_result)
    print('Pattern is:', pattern_result)

alzip()
