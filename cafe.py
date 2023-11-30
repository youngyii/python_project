import getpass
import random

user = [["tanghuru", "hungry", [0,0,0,0]], ["python","happy", [0,0,0,0]]]

check = 0
while check == 0:
    print("════════ LOG IN ════════")
    id = input("id : ")
    pw = getpass.getpass("pw : ")
    
    for i in user:
        if id == i[0] and pw == i[1]:
            check = 1
            print("로그인 성공")
    if check == 0:
        print("id / password를 확인해 주세요")

print("1. 메뉴판 보기")
print("2. 메뉴 추천")
n = int(input("원하는 버튼(숫자)을 입력해주세요: "))
menu = [["아메리카노", "카페라떼", "카푸치노", "바닐라라떼", "카페모카"],
        ["그린티라떼", "토피넛라떼", "초코라떼", "고구마라떼", "딸기라떼"],
        ["요거트스무디", "블루베리스무디", "딸기스무디", "바나나스무디", "초코스무디"],
        ["페퍼민트티", "얼그레이티", "자몽티", "레몬티", "아이스티"]]

if n == 1:
    print("════════ MENU ════════")
    cnt = 1
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
            print(str(cnt) + "." + j)
            cnt += 1
        print()