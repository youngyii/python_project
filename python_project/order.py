from point import GetPoint

def Ordering(menu, user, now_user, filename):
    file = open(filename, 'a', encoding="UTF-8")
    file.write("\n════════ 주문 내역 ════════\n")

    pay = 0  # 지불할 금액
    continueOption = "O"

    while continueOption == "O" or continueOption == "o":
        orderIdx = int(input("주문할 메뉴 번호를 입력하세요: "))
        if orderIdx < 1 or orderIdx > 20:
            print("메뉴 번호(1~20)를 정확히 입력해 주세요.\n")
            continue

        orderCategory = (orderIdx - 1) // 5
        orderMenu = menu[orderIdx - 1][0]
        orderPrice = menu[orderIdx - 1][1]

        while True:
            orderNum = int(input(orderMenu + "를 몇 잔 주문할지 숫자를 입력하세요: "))
            if orderNum < 1:
                print("1 이상을 입력해 주세요.")
                continue

            pay += orderNum * orderPrice
            
            #카테고리별 주문 횟수 업데이트
            user[now_user][2][orderCategory] += orderNum
            
            #주문 목록 업데이트
            file.write(f"{orderMenu} {orderNum}잔\n")
            break

        continueOption = input("\n주문을 계속하시겠습니까? (O/X): ")

    file.write(f"\n총 가격: {pay}원\n")
    file.close()
    print(f"\n총 가격: {pay}원\n")
    print(f"포인트 뽑기를 진행합니다.")
    pp = GetPoint()
    user[now_user][3] += pp
    print(f"{pp}포인트 획득!")
    print(f"보유 포인트: ", end="")
    
    if user[now_user][3] < 1000:
        print("\U0001F331", end="")
    elif user[now_user][3] < 2000:
        print("\U0001F33F", end="")
    else:
        print("\U0001F333", end="")
    print(f"{user[now_user][3]}p\n")
    
    if user[now_user][3] >= 2000:
        pointOption = input("결제시 포인트를 사용하시겠습니까? (O/X): ")
        if pointOption == "O" or pointOption == "o":
            print(f"결제할 금액: {pay - user[now_user][3]}원")
            user[now_user][3] = 0
        elif pointOption == "X" or pointOption == "x":
            print(f"결제할 금액: {pay}원")
    else:
        print("포인트 사용은 \U0001F333나무 단계(2000p이상)부터 가능합니다.")
        print(f"결제할 금액: {pay}원")
    print("\n주문이 완료되었습니다.\n")