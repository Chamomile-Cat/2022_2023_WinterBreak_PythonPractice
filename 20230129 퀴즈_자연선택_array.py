#0. 부모리스트는 1부터 10까지의 능력치
#1. 부모리스트에서 랜덤하게 2개를 뽑는다(mating)
#2. 부모의 능력치 범위안에서, 랜덤한 능력치를 가지는 자식을 2명 추출한다(reproducing)(이 과정은 자식개체수가 부모개체수보다 같거나 커질때까지 반복한다)
#3. 이후에 전체 개체중 평균이하인 개체를 제거한다 (natural selection)
#4. 이를 반복한다면 개체의 평균 능력치는 특정 숫자에 수렴하게 될텐데, 그 평균능력치가 9.5이상이면 반복을 중단한다
#5. 총 몇번 반복하였는지 나타낸다

#p = parent
#c = child

import numpy as np #초기 설정

pstats = np.arange(1,11,1)
def generation_count(turns):
    global pstats
    turns += 1 #값 추가

    pstat1 = np.random.choice(pstats) #부모
    pstat2 = np.random.choice(pstats)
    p_limit = np.arange(min(pstat1, pstat2), max(pstat1, pstat2)+1)

    for i in [0,1]: #자녀
        cstat = np.random.choice(p_limit)
        pstats = np.append(pstats, cstat) #추가

    if pstats.mean() >= 9.5:
        return turns
    else:
        pstats = pstats[pstats > pstats.mean()] #평균 초과만 선택
        return generation_count(turns) #재귀함수

each_turn_times = np.array([])  
for i in range(5):
    count = generation_count(0)
    each_turn_times = np.append(each_turn_times, count) # 확인
    pstats = np.arange(1,11,1)
 
print('The average times needed is:', np.mean(each_turn_times))
