import random

def GetPoint():
    p= [100, 200, 300, 400, 500]
    return random.choice(p)

# 테스트 >> 합친후에 리스트에 넣는 걸로 변경
random_point = GetPoint()
print(random_point)

