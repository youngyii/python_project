import getpass
from login import Login

def PwChange(users,n):
    while True:
        check = getpass.getpass("기존 비밀번호 입력: ")

        if check == users[n][1]:
            new_pw = getpass.getpass("새로운 비밀번호 입력: ")
            check_newpw = getpass.getpass("새로운 비밀번호 재확인: ")

            if new_pw == check_newpw:
                print("변경 성공!\n")
                return new_pw
            else:
                print("비밀번호가 맞지 않습니다. 다시 시도해 주세요.\n")
        else:
            print("비밀번호가 틀렸습니다. 다시 시도해 주세요.\n")
            

def LogOut(users,n):
    
    print("로그아웃 완료.")
    now= Login(users)
    
    return now