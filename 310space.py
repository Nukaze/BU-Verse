# CS310 127G Project310 Anupun Khumthong 1640705560
# BU Society Program #nukaze-
from prompt_toolkit import prompt
import hashlib
import os
import time

feedlst, postlst, disnamelst = [], [], []                                   # contentfeed
userlst, pwkeylst, idclst, sessionlst  = [], [], [], []                     # LoginSystem
namelst, snamelst, majorlst, facultylst, majorlst = [], [], [], [], []      # Personal data
adminlst = []
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

def buverse_main(sessionActive):
    userlst.clear();pwkeylst.clear();idclst.clear();disnamelst.clear()
    if sessionActive == 1:
        print("#"*64)
        print("< [ BU-Verse ] >".center(64))
        print("< [ Welcome Back %s ] >".center(64) %uname)
        print("#" * 64)
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
    userlst.clear();pwkeylst.clear();idclst.clear();disnamelst.clear()
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
    #pwkey1 = getpass.getpass("Enter Your Password (Must have more than 8 characters) \n> ",ispassword = True)
    while len(pwkey1) < 8:
        uiclear()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx],end="\n")
        print("!! Password Must have more than 8 characters.")
        pwkey1 = prompt("Enter Your Password (Must have more than 8 characters) \n> ",is_password = True)
    pwkey2 = prompt("Confirm Your Password (Must have more than 8 characters) \n> ",is_password=True)
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
    userlst.clear();pwkeylst.clear();idclst.clear();disnamelst.clear()
    print(headlogin)
    username = input("USERNAME : ".rjust(24))
    pwkey = prompt("PASSWORD : ".rjust(24),is_password=True)
    dbuser = open('buvs_userdb.txt','r')
    dbkey = open('buvs_keydb.txt','r')
    userline = dbuser.read().splitlines()
    for run in userline:
        pos = run.split()
        userlst.append(pos[0])
        print(userlst)
        if username in userlst:
            idx = userlst.index(username).
            if username == userlst[idx]


            print("yes in user list")
            sessionActive = 1
            #buverse_main(sessionActive)
        else:
            print("nah not in user list")
            print(userline,run,pos[0])
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


buverse_main(sessionActive)