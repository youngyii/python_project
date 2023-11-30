import getpass

user_id = "tanghuru"
user_pw = "qorhvk"
check = 0

while(check==0):
    print("-----로그인-----")
    id = input("id : ")
    pw = getpass.getpass("pw : ")
    
    if((id == user_id) and (pw == user_pw)):
        check = 1
        print("로그인 성공")
    else:
        check = 0
        print("id / password를 확인해 주세요")

        
    
        

    


