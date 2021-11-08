# CS310 127G Project310 Anupun Khumthong 1640705560
# BU Society Program #nukaze-
from prompt_toolkit import prompt
import hashlib
import os
import time

feedlst, postlst, disnamelst = [], [], []                                   # contentfeed
userlst, pwkeylst, idclst, sessionlst  = [], [], [], []                     # LoginSystem
namelst, snamelst, majorlst, facultylst, majorlst = [], [], [], [], []      # Personal data
userxlst,pwxlst = [],[]
uname = ""

timer,idx,sessionActive = 0,0,0
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

def buvs_lstclear():
    userlst.clear()
    pwkeylst.clear()
    idclst.clear()
    disnamelst.clear()
    sessionlst.clear()

def buvs_navigate():
    print("\\"*64)
    nav = input("[ Choose [Y] back to Main menu or [x] to exit. ]\n> "+"\n"+"/" * 64)
    print("/" * 64)
    if nav.upper() == "Y":
        print("[ Going back to the Main menu ]")
    elif nav.upper() == "X":
        buvs_exit()
    else: buvs_navigate()


def buvs_exit():
    time.sleep(0.25)
    uiclear()
    time.sleep(0.15)
    print("." * 64)
    exit("[ Exiting the BU-Verse.. ]".center(64) + "\n" + "." * 64)

def buverse_main(sessionActive):
    print("ssact =",sessionActive)
    if sessionActive == 1:
        print("#"*64)
        print("< [ BU-Verse ] >".center(64))
        print("< [ Welcome Back %s ] >".center(64) %uname)
        print("#" * 64)
        print("/" * 64)
        print("/" * 64)
        print("\\" * 64)
        print("\\" * 64)
        input("Enter Main Bu-verse")
    else:
        while True:
            uiclear()
            buvs_lstclear()
            print("ssact =",sessionActive)
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
                buvs_exit()
            else:
                print("!! Invalid Menu, Please try again.")
                time.sleep(1)

def buverse_signup():       # 0000000000000
    uiclear()
    buvs_lstclear()
    print(headsignup)
    uname = input("Enter Your Username \n> ")
    with open('buvs_userdb.txt','r') as dbuser:
        if uname not in dbuser:
            userlst.append(uname)
            idx = userlst.index(uname)
            buverse_getpwkey(idx)
        else:
            strx64 = "x"*64
            print(strx64.center(64))
            print("[ Sorry, this Username is already taken. ]".center(64))
            print("[ Please try again. ]".center(64))
            print(strx64.center(64))
            print("")
            buverse_signup()
        idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
        while len(idc) != 13 or idc.isalpha():
            print("ID card must have 13 characters and number only")
            idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
        idclst.append(idc)
        disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
        disnamelst.append(disname)
        print(userlst, pwkeylst, idclst, disnamelst)
        dbuser = open('buvs_userdb.txt', 'a')
        dbkey = open('buvs_keydb.txt', 'a')
        dbidc = open('buvs_idcdb.txt', 'a')
        dbuser.write(userlst[idx]+" "+disnamelst[idx]+"\n")
        dbkey.write(pwkeylst[idx]+"\n")
        dbidc.write(idclst[idx]+"\n")
        dbuser.close()
        dbkey.close()
        dbidc.close()
    print("[ BU-Verse Sign-up Successfully. ]")
    print("\n"*5)

def buverse_getpwkey(idx):
    pwkey1 = prompt("Enter Your Password (Must have more than 8 characters) \n> ",is_password = True)
    while len(pwkey1) < 8:
        uiclear()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx],end="\n")
        print("!! Password Must have more than 8 characters.")
        pwkey1 = prompt("Enter Your Password (Must have more than 8 characters) \n> ",is_password = True)
    pwkey2 = prompt("Confirm Your Password (Must have more than 8 characters) \n> ",is_password=True)
    if pwkey1 == pwkey2:
        pwhashed = pwhash(pwkey1)
        pwkeylst.append(pwhashed)
    else:
        uiclear()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx])
        print("[ # Those passwords didn't match!! Please try again. ]")
        buverse_getpwkey(idx)

def pwhash(pwkey1):
    return hashlib.sha256(str.encode(pwkey1)).hexdigest()

def pwdehash(pwkeyx, dehash):
    return pwhash(pwkeyx) == dehash

def buverse_login():
    uiclear()
    buvs_lstclear()
    with open('buvs_userdb.txt', 'r')as dbuser:
        dbkey = open('buvs_keydb.txt','r')
        while True:
            userdata = dbuser.readline().split()
            pwkeydata = dbkey.readline().split()
            if userdata != [] and pwkeydata != []:
                userlst.append(userdata[0])
                disnamelst.append(userdata[1])
                pwkeylst.append(pwkeydata[0])
            else: break
        print(userlst)
        print(pwkeylst)
        dbkey.close()

    with open('buvs_xlogindb.txt','r')as dbxlog:
        while True:
            xdata = dbxlog.readline().split()
            if xdata != []:
                userxlst.append(xdata[0])
                pwxlst.append(xdata[1])
            else: break
        print(userxlst,pwxlst)

    print(headlogin)
    username = input("USERNAME : ".rjust(24))
    pwkeylog = prompt("PASSWORD : ".rjust(24),is_password=True)
    print("|" * 64)
    if username in userlst:
        idx = userlst.index(username)
        if pwdehash(pwkeylog, pwkeylst[idx]):
            print("[ Password Matched loging-in.. ]".center(64))
            print("^"*64)
            input("# Press Any key to continue  > ")
            sessionActive = 1
            buverse_main(sessionActive)
        else:
            print("|"*64)
            print("[ Wrong Password, Please try again.. ]")
            print("|" * 64)
            time.sleep(4)
            buverse_login()
    else:
        print("[ Sorry, Username not found. ]".center(64))
        buvs_navigate()

def buverse_passwordchecklogin(idx):
    dbkey = open('buvs_keydb.txt', 'r')
    pwkeyline = dbkey.read().splitlines()
    print(pwkeyline)
    for run in range(len(pwkeyline)):
        pwkeylst.append(run)
        print(pwkeylst)

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


buverse_main(sessionActive)