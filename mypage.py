import getpass

def PwChange():
    while True:
        check = getpass.getpass("기존 비밀번호 입력: ")

        if check == pw:
            new_pw = getpass.getpass("새로운 비밀번호 입력: ")
            check_newpw = getpass.getpass("새로운 비밀번호 재확인: ")

            if new_pw == check_newpw:
                print("변경 성공!")
                break
            else:
                print("비밀번호가 맞지 않습니다. 다시 시도해 주세요.")
        else:
            print("비밀번호가 틀렸습니다. 다시 시도해 주세요.")

def LogOut():
    #저장된 user 정보 초기화 하기
    print("로그아웃 완료.")
    
# 비밀번호 변경
pw = "assa" #>> 합친 후에 저장된 비번 불러오는 걸로 바꾸기

choice = input("비밀번호 변경 (1 입력)\n로그아웃 (2 입력) : ")

if choice == "1":
    PwChange()
elif choice == "2":
    LogOut()
else:
    print("잘못된 입력입니다.")

