# CS310 127G Project310 Anupun Khumthong 1640705560
# BU Society Program #nukaze-
#import msvcrt as msv
feedlst, postlst, disnamelst = [], [], []                                   # contentfeed
userlst, keylst,  = [],[]                                                   # LoginSystem
namelst, snamelst, majorlst, facultylst, majorlst = [], [], [], [], []      # Personal data
adminlst = []
uname = "Max"

#def wait():
    #msv.getch()

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
                print("Going to Login..")
                buverse_login()
            elif gout == "2":
                print("Going to Sign-up..")
                buverse_signup()
            elif gout == "0":
                exit("[ Exiting the BU-Verse.. ]")

def buverse_signup():
    print("+ " * 32)
    print("< [ BU-Verse Sign-up ] >".center(64))
    print("+ " * 32)
    uname = input("Enter Your Username \n> ")
    pwkey = input("Enter Your Password (Must have more than 8 characters) \n> ")
    uid = int(input("Enter Your ID card Number (Must be number and more equal 13 character) \n> "))
    print("\n"*5)

def buverse_login():
    print("|"*64)
    print("< [ BU-Verse Login ] >".center(64))
    print("|"*64)
    print("\n" * 5)






buverse_main()