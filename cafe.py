import getpass
import random

user = [["tanghuru", "hungry", [0,3,0,0], 0], ["python","happy", [0,0,0,0], 0]]

print(len(user))
check = 0
while check == 0:
    print("════════ LOG IN ════════")
    id = input("id : ")
    pw = getpass.getpass("pw : ")
    
    for i in range(len(user)):
        if id == user[i][0] and pw == user[i][1]:
            check = 1
            now_user = i
            print("로그인 성공")
    if check == 0:
        print("id / password를 확인해 주세요")

print("1. 메뉴판 보기")
print("2. 메뉴 추천")
print("3. 주문")
print("4. 주문 내역 보기")
print("5. 마이페이지")

n = int(input("원하는 버튼(숫자)을 입력해주세요: "))
menu = {0:{1:"아메리카노", 2:"카페라떼", 3:"카푸치노", 4:"바닐라라떼", 5:"카페모카"},
        1:{6:"그린티라떼", 7:"토피넛라떼", 8:"초코라떼", 9:"고구마라떼", 10:"딸기라떼"},
        2:{11:"요거트스무디", 12:"블루베리스무디", 13:"딸기스무디", 14:"바나나스무디", 15:"초코스무디"},
        3:{16:"페퍼민트티", 17:"얼그레이티", 18:"자몽티", 19:"레몬티", 20:"아이스티"}}

if n == 1:
    print("════════ MENU ════════")
    for i in range(4):
        if i == 0:
            print("[Coffee]")
        elif i == 1:
            print("[Latte]")
        elif i == 2:
            print("[Smoothie]")
        elif i == 3:
            print("[Tea]")
        for j in menu[i]:
            print(str(j) + "." + menu[i].get(j))
        print()

elif n == 2:
    print("════════ 추천 메뉴 ════════")
    max_category = 0
    user_category = user[now_user][2]
    for i in range(len(user_category)):
        if max_category < user_category[i]:
            max_category = i
            
    recommend = random.choice(list(menu[max_category].keys()))
    print(f"{recommend}. {menu[max_category][recommend]}")