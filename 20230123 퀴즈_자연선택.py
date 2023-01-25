# 0. 부모리스트는 1부터 10까지의 능력치
# 1. 부모리스트에서 랜덤하게 2개를 뽑는다(mating)
# 2. 부모의 능력치 범위안에서, 랜덤한 능력치를 가지는 자식을 2명 추출한다(reproducing)(이 과정은 자식개체수가 부모개체수보다 같거나 커질때까지 반복한다)
# 3. 이후에 전체 개체중 평균이하인 개체를 제거한다 (natural selection)
# 4. 이를 반복한다면 개체의 평균 능력치는 특정 숫자에 수렴하게 될텐데, 그 평균능력치가 9.5이상이면 반복을 중단한다
# 5. 총 몇번 반복하였는지 나타낸다

# p = parent
# ran = random
# c= child

'''
## global을 사용한 경우
import random
turns = 0
pstats = list(range(1,11))

def newgeneration():

    global turns # 여기에서 global을 사용하지 않을 방법이 있을까요? 
    turns=turns+1

    ranindex1 = random.randrange(0, len(pstats))
    ranindex2 = random.randrange(0, len(pstats))
    ranpstat1 = pstats[ranindex1]
    ranpstat2 = pstats[ranindex2]

    if ranpstat1 <= ranpstat2:
        cstat1 = random.randrange(ranpstat1, ranpstat2+1)
        cstat2 = random.randrange(ranpstat1, ranpstat2+1)
    if ranpstat1 >= ranpstat2:
        cstat1 = random.randrange(ranpstat2, ranpstat1+1)
        cstat2 = random.randrange(ranpstat2, ranpstat1+1)
    pstats.append(cstat1)
    pstats.append(cstat2)

    if sum(pstats)/len(pstats) >= 9.5:
        print(turns)
        return
    for stat in pstats:
        if stat <= sum(pstats)/len(pstats):
            pstats.remove(stat)
    newgeneration()

newgeneration()
'''

## global을 사용하지 않은 경우
import random
pstats = list(range(1,11))
templist = []

def newgeneration(turns):
    turns=turns+1

    ranindex1 = random.randrange(0, len(pstats))
    ranindex2 = random.randrange(0, len(pstats))
    ranpstat1 = pstats[ranindex1]
    ranpstat2 = pstats[ranindex2]

    if ranpstat1 <= ranpstat2:
        cstat1 = random.randrange(ranpstat1, ranpstat2+1)
        cstat2 = random.randrange(ranpstat1, ranpstat2+1)
    if ranpstat1 >= ranpstat2:
        cstat1 = random.randrange(ranpstat2, ranpstat1+1)
        cstat2 = random.randrange(ranpstat2, ranpstat1+1)
    pstats.append(cstat1)
    pstats.append(cstat2)

    average = sum(pstats)/len(pstats)

    if average >= 9.5:
        print(turns)
        return
    for stat in pstats:
        if stat <= average:
            templist.append(stat)
    for stat2 in templist:
        pstats.remove(stat2)
    templist.clear()
    newgeneration(turns)

newgeneration(0)
