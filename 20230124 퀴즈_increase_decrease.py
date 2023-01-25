# 1. 아래 함수의 결과값을 예상하시오. 
# 2. 코드의 추가 및 제거 없이  코드의 위치만 바꿔서 increasing 함수를 제작하시오. 

def decreasing(num, count):
    num += 1
    count += 1
    if count < 5:
        decreasing(num, count)
    print(num)

decreasing(0,0)

# 1. num += 1은 num = num +1이라는 뜻이다. 분명 숫자는 올라는 것처럼 보이는데, 왜 함수의 이름이 decreasing이지? 왜 결과는 5, 4, 3, 2, 1이 되는 것일까.
# 왜냐하면 재귀함수이니까!

# 2

def decreasing(num, count):
    num += 1
    count += 1
    print(num)
    if count < 5:
        decreasing(num, count)

decreasing(0,0)
