import random

def show_menu(menu):
    cnt = 1
    print("\n════════ MENU ════════")
    for i in range(20):
        if i == 0:
            print("\n[Coffee]")
        elif i == 5:
            print("\n[Latte]")
        elif i == 10:
            print("\n[Smoothie]")
        elif i == 15:
            print("\n[Tea]")
        print(f"{cnt}. {menu[i][0]} {menu[i][1]}원")
        cnt += 1
    print()

def recommend_menu(user,now_user,menu):
    print("\n════════ 추천 메뉴 ════════")
    max_category = 0
    user_category = user[now_user][2]
    for i in range(len(user_category)):
        if user_category[max_category] < user_category[i]:
            max_category = i
                
    recommend = random.randint(0, 4) + max_category * 5
    print(f"{recommend}. {menu[recommend][0]} {menu[recommend][1]}원")
    print(f"{user[now_user][0]}님의 주문 내역을 참고한 추천 메뉴입니다.\n")