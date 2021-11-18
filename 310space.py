# CS310 127G Project310 Anupun Khumthong 1640705560
# BU-Verse  #nukaze-
from prompt_toolkit import prompt
import hashlib
import os
import time
import datetime
##############################################################################
#                           BU-Verse Variable-Phase                          #
##############################################################################
navlst = ["T", "M", "X"]                                                                # navlst
postfeedlst, postdisnamelst, posttimelst = [], [], []                                   # contentfeed
userlst, pwkeylst, idclst = [], [], []                                                  # LoginCheckSystem
devuserxlst, devpwxlst, devdislst = [], [],[]                                           # DevLoginCheck
namelst, snamelst,disnamelst, majorlst, facultylst, majorlst = [], [], [], [], [],[]    # Profile data
ssdisnamelst, ssunamelst = [],[]                                                        # session

timer,sessionActive = 0,0
uiclear = lambda: os.system('cls')
headsignup = ("+" * 64 + "\n" + "< [ BU-Verse Sign-up ] >".center(64) + "\n" + "+" * 64)
headlogin = ("|"*64 + "\n" + "< [ BU-Verse Login ] >".center(64) + "\n" + "|"*64)

##############################################################################
#                           BU-Verse Tools-Phase                             #
##############################################################################
def getfile(filecall):
    return os.stat(filecall).st_size

def loading_progress(timer,interval,delay):
    print("[",end="")
    for i in range(timer):
        time.sleep(interval)
        loadprogress = "■" * i * 4
        print("%s" % loadprogress, end="")
    print("]")
    time.sleep(delay)

def buvs_checklstclear():
    userlst.clear();pwkeylst.clear();idclst.clear();disnamelst.clear()
    devuserxlst.clear();devpwxlst.clear();devdislst.clear()

def buvs_navigate():
    print("\\" * 64)
    nav = input("( [M] back to Main menu )\n( [x] to exit. )\n> ")
    while True:
        if nav.upper() == "M":
            print("[ Going back to Main menu ]")
            time.sleep(1.5)
            buverse_main(sessionActive)
        elif nav.upper() == "X":
            buvs_exit()
        else: time.sleep(.1);buvs_navigate()

def buvs_exit():
    time.sleep(0.25)
    uiclear()
    time.sleep(0.20)
    print("." * 64)
    exit("[ Exiting the BU-Verse.. ]".center(64) + "\n" + "." * 64)

def buvs_txtlimitlenght(txtlimit,gettxt):
    newinsert = ""
    for i, letter in enumerate(gettxt):
        if i % txtlimit == 0:
            newinsert += '\n'
        newinsert += letter
    newinsert = newinsert[1:]
    return newinsert

##############################################################################
#                           BU-Verse 0-Phase                                 #
##############################################################################

def buverse_recallsession():
    buvs_checklstclear()
    if getfile('buvs_recallsession.txt'):
        with open('buvs_recallsession.txt','r')as dbrecallss:
            if dbrecallss !=[] :
                recalldata = dbrecallss.readline().split()
                sessionRecall = int(recalldata[0])
                recusername = recalldata[1]
                recpwkeylog = recalldata[2]
                with open('buvs_userdb.txt','r')as dbuser,open('buvs_keydb.txt','r')as dbkey:
                    while True:
                        userdata = dbuser.readline().split()
                        pwkeydata = dbkey.readline().split()
                        if userdata != [] and pwkeydata != []:
                            userlst.append(userdata[0])
                            disnamelst.append(userdata[1])
                            pwkeylst.append(pwkeydata[0])
                        else:
                            break
                    dbkey.close()
                with open('buvs_xlogindb.txt', 'r') as dbxlog:
                    while True:
                        xdata = dbxlog.readline().split()
                        if xdata != []:
                            devuserxlst.append(xdata[0])
                            devpwxlst.append(xdata[1])
                            devdislst.append(xdata[2])
                        else:
                            break
                if recusername in userlst:
                    global idx, ssdisname, ssuname
                    idx = userlst.index(recusername)
                    if recpwkeylog == pwkeylst[idx]:  # if session hash == hash True
                        ssunamelst.append(recusername)
                        ssuname = "".join(ssunamelst)
                        ssdisnamelst.append(disnamelst[idx])
                        ssdisname = "".join(ssdisnamelst)
                        print(" "*19,end="");loading_progress(4,0.05,0.2)
                        print("[ Recalling Profile logging-in.. ]".center(64))
                        time.sleep(0.4)
                        print(("[ Welcome back %s ]" % "".join(ssdisname)).center(64))
                        time.sleep(0.7)
                        uiclear()
                        buverse_main(sessionRecall)         #userrecall
                    elif recusername in devuserxlst:
                        idx = devuserxlst.index(recusername)
                        if recpwkeylog == devpwxlst[idx]:       #check old session
                            ssunamelst.append(recusername)
                            ssuname = "".join(ssunamelst)
                            ssdisnamelst.append(devdislst[idx])
                            ssdisname = "".join(ssdisnamelst)
                            print("[ Password Matched logging-in.. ]".center(64))
                            time.sleep(0.25)
                            print(("[ Welcome back Dev %s ]" % ssdisname).center(64))
                            print("|" * 64)
                            input("# Press Any key to continue  > ")
                            uiclear()
                            buverse_main(sessionRecall)     #devrecall
                        else: buverse_main(0)
                    else:
                        buverse_main(0)
                else:
                    buverse_main(0)
    else: buverse_main(0)

##############################################################################
#                           BU-Verse Portal-Phase                            #
##############################################################################
def buverse_main(sessionActive):
    if sessionActive == 1:#user
        buverse_versemain(sessionActive)
        buverse_main(sessionActive)
    elif sessionActive == 9:#dev
        uiclear()
        print("sessionActive =", sessionActive)
        print("#"*64)
        print("< [ BU-Verse Developer mode ] >".center(64))
        print(("< [ Welcome Back %s ] >"%ssdisname).center(64))
        print("#" * 64)
        print("/" * 64)
        print("/" * 64)
        print("\\" * 64)
        print("\\" * 64)
        input("Enter Main Bu-verse")
        buverse_main(sessionActive)
    else:
        uiclear()
        buvs_checklstclear()
        print("sessionActive =",sessionActive)
        print("#" * 64)
        print("< [ Welcome to BU-Verse ] >".center(64))
        print("* Please Login to continue! ".center(64))
        print("#" * 64)
        print("[1] Log-in")
        print("[2] Sign-up")
        print("[0] Exit the Program")
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
            buverse_main(sessionActive)

def buverse_signup():       # 0000000000000
    uiclear()
    buvs_checklstclear()
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
        getidcard()
        getdisname()
        print(userlst, pwkeylst, idclst, disnamelst)
        input("wait")
        dbuser = open('buvs_userdb.txt', 'a');dbkey = open('buvs_keydb.txt', 'a');dbidc = open('buvs_idcdb.txt', 'a')
        dbuser.write(userlst[idx]+" "+disnamelst[idx]+"\n")
        dbkey.write(pwkeylst[idx]+"\n")
        dbidc.write(idclst[idx]+"\n")
        dbuser.close();dbkey.close();dbidc.close()
    print("[ BU-Verse Sign-up Successfully. ]")
    time.sleep(0.5)
    input("Please Any key to Back to menu")
    buverse_main(sessionActive)

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

def getidcard():
    idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    while len(idc) != 13 or idc.isalpha():
        print("ID card must have 13 characters and number only")
        idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    idclst.append(idc)

def getdisname():
    disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
    disnamecntlst = disname.count(" ")
    print(disnamecntlst)
    while not disname or disnamecntlst != 0:
        print(disname)
        print("** Display Name \"BlankSpace\" not allowed.")
        disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
        disnamecntlst = disname.count(" ")
        print(disnamecntlst)
    disnamelst.append(disname)

def pwhash(pwkey1):
    return hashlib.sha256(str.encode(pwkey1)).hexdigest()

def pwdehash(pwkeyi, dehash):
    return pwhash(pwkeyi) == dehash

def buverse_login():
    uiclear()
    buvs_checklstclear()
    ssunamelst.clear();ssdisnamelst.clear()
    with open('buvs_userdb.txt','r')as dbuser,open('buvs_keydb.txt','r')as dbkey:
        while True:
            userdata = dbuser.readline().split()
            pwkeydata = dbkey.readline().split()
            if userdata != [] and pwkeydata != []:
                userlst.append(userdata[0])
                disnamelst.append(userdata[1])
                pwkeylst.append(pwkeydata[0])
            else: break
        print(userlst)
        #print(pwkeylst)
    with open('buvs_xlogindb.txt','r')as dbxlog:
        while True:
            xdata = dbxlog.readline().split()
            if xdata != []:
                devuserxlst.append(xdata[0])
                devpwxlst.append(xdata[1])
                devdislst.append(xdata[2])
            else:break
        print(devuserxlst)
        #print(devpwxlst)
    print(headlogin)
    print('')
    username = input("USERNAME : ".rjust(24))
    pwkeylog = prompt("PASSWORD : ".rjust(24),is_password=True)
    print('\n\n')
    print("|" * 64)
    if username in userlst:
        global idx,ssdisname,ssuname
        idx = userlst.index(username)
        if pwdehash(pwkeylog, pwkeylst[idx]):                       # if pwdehash True
            ssunamelst.append(username)
            ssuname = "".join(ssunamelst)
            ssdisnamelst.append(disnamelst[idx])
            ssdisname = "".join(ssdisnamelst)
            dbrecallss = open('buvs_recallsession.txt','w')
            dbrecallss.write("1"+" "+username+" "+pwkeylst[idx])
            print("[ Password Matched logging-in.. ]".center(64))
            time.sleep(0.5)
            print(("[ Welcome back %s ]" % "".join(ssdisname)).center(64))
            print("|"*64)
            time.sleep(2.5)
            uiclear()
            buverse_main(1)
        else:
            print("[ Logging-in Failed. ]".center(64))
            print("[ Wrong Password, Please try again.. ]".center(64))
            print("|" * 64)
            time.sleep(0.5)
            while True:
                print("\\" * 64)
                nav = input("( Choose [T] Try again or [M] back to Main menu )\n > ")
                if nav.upper() == "T":
                    buverse_login()
                elif nav.upper() == "M":
                    buverse_main(0)
                else:
                    continue
    elif username in devuserxlst:
        idx = devuserxlst.index(username)
        if pwdehash(pwkeylog, devpwxlst[idx]):
            ssunamelst.append(username)
            ssuname = "".join(ssunamelst)
            ssdisnamelst.append(devdislst[idx])
            ssdisname = "".join(ssdisnamelst)
            dbrecallss = open('buvs_recallsession.txt', 'w')
            dbrecallss.write("1"+" "+username+" "+devpwxlst[idx])
            print("[ Password Matched logging-in.. ]".center(64))
            time.sleep(0.25)
            print(("[ Welcome back Dev %s ]"%ssdisname).center(64))
            print("|" * 64)
            input("# Press Any key to continue  > ")
            uiclear()
            buverse_main(9)
        else:
            print("[ Logging-in Failed. ]".center(64))
            print("[ Wrong Password, Please try again.. ]".center(64))
            print("|" * 64)
            while True:
                print("\\" * 64)
                nav = input("( Choose [T] Try again or [M] back to Main menu )\n > ")
                if nav.upper() == "T":
                    buverse_login()
                elif nav.upper() == "M":
                    buverse_main(0)
                else:continue
    else:
        print("[ Sorry, Username not found. ]".center(64))
        time.sleep(.5)
        buvs_navigate()
##############################################################################
#                           BU-Verse Verse-Phase                             #
##############################################################################

def buvs_versemenu():
    print("*"*64)
    print("[1] Posting something? [2] Explore People [3] My Verse".center(64))
    print("[0] Exit  [00] Log-out and Menu  [000] Log-out and Exit".center(64))
    print("*" * 64)
    vmenu = input("> ")
    if vmenu == "1":
        buverse_verseposting()
    elif vmenu == "2":
        buverse_verseexplore()
    elif vmenu == "3":
        buverse_verseprofile()
    elif vmenu == "0":
        buvs_exit()
    elif vmenu == "00":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1.5)
        buverse_main(0)
    elif vmenu == "000":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1.5)
        buvs_exit()

def buverse_versemain(sessionActive):
    while True:
        uiclear()
        buvs_checklstclear()
        #print("session =", sessionActive)   #sessioncheck
        postfulltime = datetime.datetime.now()
        postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
        print("#" * 64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print(("[ %s ]" % ssdisname).center(64))
        if getfile('buvs_postingversedb.txt'):
            with open('buvs_postingversedb.txt','r')as dbposting:
                postdisnamelst.clear();postfeedlst.clear();posttimelst.clear()
                while True:
                    getrawpost = dbposting.readline().split("|*|")
                    if getrawpost != ['']:
                        #print(getrawpost)
                        postdisnamelst.append(getrawpost[0])
                        posttimelst.append(getrawpost[1])
                        getpostfeed = getrawpost[2].replace("\n","")
                        postfeedlst.append(getpostfeed)
                    else:break
                postdisnamelst.reverse();posttimelst.reverse();postfeedlst.reverse()
            for run in range(len(postfeedlst)):
                print("_"*64)
                print("[ From",postdisnamelst[run],"At",posttimelst[run]+" ]")
                print(">",buvs_txtlimitlenght(58,postfeedlst[run]))
        else:
            print("\n")
            print("[ No one posts in verse ]".center(64))
            print("\n"*2)
        buvs_versemenu()

def buverse_verseposting():
    uiclear()
    postfulltime = datetime.datetime.now()
    postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
    with open('buvs_postingversedb.txt','a+')as dbpostingverse:
        print("#"*64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print("="*64)
        print((">>>> %s Posting in Verse? >>>>>>>>>>>>>>>>>>>>>>>>" %ssdisname).center(64))
        getpostverse = input("> ")
        recheckgetpostverse = input("Press [1] Post or [Any key] Cancel\n> ")
        if recheckgetpostverse == "1":
            dbpostingverse.write(ssdisname+"|*|"+postlocaltime+"|*|"+getpostverse+"\n")
            uiclear()
            buverse_versemain(1)
        else:
            uiclear()
            buverse_versemain(1)

def buverse_verseexplore():
    input()
    pass

def buverse_verseprofile():
    input()
    pass

##############################################################################
#                           BU-Verse initiate                                #
##############################################################################
buverse_recallsession()
buverse_main(sessionActive)