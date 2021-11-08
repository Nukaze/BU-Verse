# CS310 127G Project310 Anupun Khumthong 1640705560
# BU Society Program #nukaze-
import getpass
import os
import time

feedlst, postlst, disnamelst = [], [], []                                   # contentfeed
userlst, pwkeylst, idclst, sessionlst  = [], [], [], []                       # LoginSystem
namelst, snamelst, majorlst, facultylst, majorlst = [], [], [], [], []      # Personal data
adminlst = []
uname = ""
timer,idx = 0,0
uiclear = lambda: os.system('cls')
headsignup = ("+" * 64 + "\n" + "< [ BU-Verse Sign-up ] >".center(64) + "\n" + "+" * 64)
headlogin = ("|"*64 + "\n" + "< [ BU-Verse Login ] >".center(64) + "\n" + "|"*64)


def loading_progress(timer,interval,delay):
    print("[",end="")
    for i in range(timer):
        time.sleep(interval)
        loadprogress = "■" * i * 4
        print("%s" % loadprogress, end="")
    print("]")
    time.sleep(delay)

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
            uiclear()
            print("#" * 64)
            print("< [ Welcome to BU-Verse ] >".center(64))
            print("* Please Login to continue! ".center(64))
            print("#" * 64)
            print("[1] Login")
            print("[2] Sign-up")
            print("[0] Exit the Program")
            print(userlst, pwkeylst, idclst, disnamelst)
            gout = input("Press select menu : ")
            if gout == "1":
                print("[ Going to Login.. ]")
                loading_progress(4,0.1,0.2)
                buverse_login()
            elif gout == "2":
                print("[ Going to Sign-up.. ]")
                loading_progress(4,0.3,0.5)
                buverse_signup()
            elif gout == "0":
                time.sleep(0.25)
                uiclear()
                time.sleep(0.15)
                print("."*64)
                exit("[ Exiting the BU-Verse.. ]".center(64) + "\n"+"."*64)
            else:
                print("!! Invalid Menu, Please try again.")
                time.sleep(1)

def buverse_signup():       # 0000000000000
    uiclear()
    print(headsignup)
    uname = input("Enter Your Username \n> ")
    with open('buvs_userdb.txt','r') as dbuser:
        if uname not in dbuser:
            userlst.append(uname)
            idx = userlst.index(uname)
            print(userlst)
            buverse_getpwkey(idx)
        else:
            strx64 = "x"*64
            print(strx64.center(64))
            print("[ Sorry, this Username is already taken. ]".center(64))
            print("[ Please try again. ]".center(64))
            print(strx64.center(64))
            print("")
            buverse_signup()
        #buverse_getpwkey()
        idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
        while len(idc) != 13 or idc.isalpha():
            print("ID card must have 13 characters and number only")
            idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
        idclst.append(idc)
        disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
        disnamelst.append(disname)
        print(userlst, pwkeylst, idclst, disnamelst)
        dbuser = open('buvs_userdb.txt', 'w')
        dbkey = open('buvs_keydb.txt', 'w')
        dbidc = open('buvs_idcdb.txt', 'w')
        dbuser.write(userlst[idx]+""+disnamelst[idx])
        dbkey.write(pwkeylst[idx])
        dbidc.write(idclst[idx])
        dbuser.close()
        dbkey.close()
        dbidc.close()
    print("[ BU-Verse Sign-up Successfully. ]")
    print("\n"*5)

def buverse_getpwkey(idx):
    pwkey1 = getpass.getpass("Enter Your Password (Must have more than 8 characters) \n> ")
    while len(pwkey1) < 8:
        uiclear()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx],end="\n")
        print("!! Password Must have more than 8 characters.")
        pwkey1 = getpass.getpass("Enter Your Password (Must have more than 8 characters) \n> ")
    pwkey2 = getpass.getpass("Confirm Your Password (Must have more than 8 characters) \n> ")
    if pwkey1 == pwkey2:
        pwkeylst.append(pwkey1)
    else:
        uiclear()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx])
        print("[ # Those passwords didn't match!! Please try again. ]")
        buverse_getpwkey(idx)

def buverse_login():
    uiclear()
    print(headlogin)
    uname = input("USERNAME : ".rjust(24))
    pwkey = input("PASSWORD : ".rjust(24))
    if uname in userlst:
        pass
    print("\n" * 3)
    input("go menu")


"""
login?guide
file = open('profile.txt','r')
datalst = file.read().splitlines()
t = input("Enter t ")
x = 0
print(datalst)
while True:
        if t in datalst:
            u_sesion = datalst.index(t)
            print(u_sesion)
            print("go in")
            break
        else:
            print("Get out")
            break
"""


buverse_main()