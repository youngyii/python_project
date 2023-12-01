import getpass
import random

user = [["tanghuru", "hungry", [0,3,5,0], 500], ["python","happy", [0,0,0,0], 0]]

check = 0
while check == 0:
    print("════════ LOG IN ════════")
    id = input("id : ")
    pw = getpass.getpass("pw : ")
    
    for i in range(len(user)):
        if id == user[i][0] and pw == user[i][1]:
            check = 1
            now_user = i
            print("로그인 성공\n")
    if check == 0:
        print("id / password를 확인해 주세요")

print("1. 메뉴판 보기")
print("2. 메뉴 추천")
print("3. 주문")
print("4. 주문 내역 보기")
print("5. 마이페이지\n")

n = int(input("원하는 버튼(숫자)을 입력해주세요: "))
menu = [["아메리카노", 2500], ["카페라떼", 3000], ["카푸치노", 3000], ["바닐라라떼",3500], ["카페모카",3500],
        ["그린티라떼", 4000], ["토피넛라떼", 4000], ["초코라떼", 4000], ["고구마라떼", 4000], ["딸기라떼", 4000],
        ["요거트스무디", 4500], ["블루베리스무디", 4500], ["딸기스무디", 4500], ["바나나스무디", 4500], ["초코스무디", 4500],
        ["페퍼민트티", 3500], ["얼그레이티", 3500], ["자몽티", 4000], ["레몬티", 4000], ["아이스티", 2500]]

if now_user == 0:
        filename = "tanghuru.txt"
elif now_user == 1:
    filename = "python.txt"   
file = open(filename, "w", encoding="UTF-8")
file.close()
if n == 1:
    cnt = 1
    print("════════ MENU ════════")
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

elif n == 2:
    print("════════ 추천 메뉴 ════════")
    max_category = 0
    user_category = user[now_user][2]
    for i in range(len(user_category)):
        if user_category[max_category] < user_category[i]:
            max_category = i
            
    recommend = random.randint(0, 4) + max_category * 5
    print(f"{recommend}. {menu[recommend][0]} {menu[recommend][1]}원")
    print(f"{user[now_user][0]}님의 주문 내역을 참고한 추천 메뉴입니다.")
            
elif n == 3:
    file = open(filename, 'a', encoding="UTF-8")
    file.write("\n[주문 내역]\n")
    
    pay = 0     # 지불할 금액      
    continueOption = "O"
    file = open(filename, 'a', encoding="UTF-8")
    while continueOption == "O" or continueOption == "o":
        orderIdx = int(input("주문할 메뉴 번호를 입력하세요: "))
        if orderIdx < 1 or orderIdx > 20:
            print("메뉴 번호(1~20)를 정확히 입력해 주세요.\n")
            continue
        
        orderCategory = (orderIdx - 1) // 5       # 카테고리
        orderMenu = menu[orderIdx - 1][0]   # 메뉴명
        orderPrice = menu[orderIdx - 1][1]  # 메뉴 가격 
            
        while True:
            orderNum = int(input(orderMenu + "를 몇 잔 주문할지 숫자를 입력하세요: "))
            if orderNum < 1:
                print("1 이상을 입력해 주세요.")
                continue
                
            pay += orderNum * orderPrice
                
            # 카테고리별 주문 횟수 업데이트
            user[i][2][orderCategory] += orderNum
            # 주문 목록 업데이트
            file.write(f"{orderMenu} {orderNum}잔\n")
            break
        
        continueOption = input("\n주문을 계속하시겠습니까? (O/X): ")
    
    file.write(f"\n총 가격: {pay}")
    file.close()    
    print(f"\n총 가격: {pay}")
    print(f"보유 포인트: {user[now_user][3]}p\n")

    pointOption = input("결제시 포인트를 사용하시겠습니까? (O/X): ")
    if pointOption == "O" or pointOption == "o":
        print(f"\n결제할 금액: {pay - user[now_user][3]}")
        user[now_user][3] = 0
    elif pointOption == "X" or pointOption == "x":
        print(f"\n결제할 금액: {pay}")
    print("\n주문이 완료되었습니다.\n")

elif n == 4:
    file = open(filename, "r", encoding="UTF-8")
    res = file.read()
    print(res)
    file.close()