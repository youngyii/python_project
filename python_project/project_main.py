from login import Login
from menu import show_menu,recommend_menu
from mypage import PwChange, LogOut
from order import Ordering
from history import History
from point import GetPoint

#기본 정보
user = [["tanghuru", "hungry", [0, 3, 5, 0], 500], ["python", "happy", [0, 0, 0, 0], 0]]
menu = [["아메리카노", 2500], ["카페라떼", 3000], ["카푸치노", 3000], ["바닐라라떼",3500], ["카페모카",3500],
        ["그린티라떼", 4000], ["토피넛라떼", 4000], ["초코라떼", 4000], ["고구마라떼", 4000], ["딸기라떼", 4000],
        ["요거트스무디", 4500], ["블루베리스무디", 4500], ["딸기스무디", 4500], ["바나나스무디", 4500], ["초코스무디", 4500],
        ["페퍼민트티", 3500], ["얼그레이티", 3500], ["자몽티", 4000], ["레몬티", 4000], ["아이스티", 2500]]

#로그인
now_user = Login(user)
pg = 1
    
while pg == 1: 
    if now_user == 0:
        filename = "tanghuru.txt"
    elif now_user == 1:
        filename = "python.txt" 
    
    #번호 선택
    print("1. 메뉴판 보기")
    print("2. 메뉴 추천")
    print("3. 주문")
    print("4. 주문 내역 보기")
    print("5. 마이페이지\n")

    n = int(input("원하는 버튼(숫자)을 입력하세요: "))

    #번호 선택에 따른 모듈
    if n == 1:
        show_menu(menu)
    elif n == 2:
        recommend_menu(user,now_user,menu)
    elif n == 3:
        Ordering(menu, user, now_user, filename)    
    elif n == 4:
        History(filename)
    elif n == 5:
        print("\n════════ 마이페이지 ════════\n")
        print("1. 비밀번호 변경\n2. 로그아웃\n3. 앱 종료\n")
        choice = input("숫자를 입력하세요: ")
        if choice == "1":
            user[now_user][1] = PwChange(user, now_user)
        elif choice == "2":
            now_user = LogOut(user,now_user)
        elif choice == "3":
            print("앱을 종료합니다.")
            pg = 2      
        else:
            print("잘못된 입력입니다.")
    else:
            print("잘못된 입력입니다.")