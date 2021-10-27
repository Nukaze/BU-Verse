# CS310 127G Project310 Anupun Khumthong 1640705560
# BU Society Program #nukaze-
import getpass
feedlst, postlst, disnamelst = [], [], []                                   # contentfeed
userlst, keylst, sessionlst  = [], [], []                                   # LoginSystem
namelst, snamelst, majorlst, facultylst, majorlst = [], [], [], [], []      # Personal data
adminlst = []
uname = ""
def buverse_main():
    if uname in userlst:
        print("#"*64)
        print("< [ BU-Verse ] >".center(64))
        print("< [ Welcome Back %s ] >".center(64) %uname)
        print("#"*64)
        print("/" * 64)
        print("/" * 64)
        print("\\" * 64)
        print("\\" * 64)
    else:
        while True:
            print("#" * 64)
            print("< [ Welcome to BU-Verse ] >".center(64))
            print("* Please Login to continue! ".center(64))
            print("#" * 64)
            print("[1] Login")
            print("[2] Sign-up")
            print("[0] Exit the Program")
            gout = input("Press select menu : ")
            if gout == "1":
                print("[ Going to Login.. ]")
                buverse_login()
            elif gout == "2":
                print("[ Going to Sign-up.. ]")
                buverse_signup()
            elif gout == "0":
                exit("[ Exiting the BU-Verse.. ]")

def buverse_signup():       # 0000000000000
    print("+" * 64)
    print("< [ BU-Verse Sign-up ] >".center(64))
    print("+" * 64)
    uname = input("Enter Your Username \n> ")
    dbuser = open('buvs_userdb.txt','r+')
    if uname not in dbuser:
        dbuser.write(uname)
    else:
        strx64 = "x"*64
        print(strx64.center(64))
        print("[ Sorry, this Username is already taken. ]".center(64))
        print("[ Please try again. ]".center(64))
        print(strx64.center(64))
        print("")
        buverse_signup()
    dbuser.close()
    pwkey1 = getpass.getpass("Enter Your Password (Must have more than 8 characters) \n> ")
    while len(pwkey1) < 8 :
        print("* Password Must have more than 8 characters.")
        pwkey1 = getpass.getpass("Enter Your Password (Must have more than 8 characters) \n> ")
    pwkey2 = getpass.getpass("Confirm Your Password (Must have more than 8 characters) \n> ")
    if pwkey1 == pwkey2:
        keylst.append(pwkey1)
    else:
        print("* Those passwords didn't match!! Please try again.")
        buverse_signup()
    uid = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    while len(uid) != 13 or pwkey1.isalpha():
        print("ID card must have 13 characters and number only")
        uid = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
    print("[ BU-Verse Sign-up Successfully. ]")
    print("\n"*5)

def buverse_login():
    print("|"*64)
    print("< [ BU-Verse Login ] >".center(64))
    print("|"*64)
    print("\n" * 5)


buverse_main()