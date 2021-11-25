# CS310 127G Project310 Anupun Khumthong 1640705560
# BU-Verse  #nukaze-
from prompt_toolkit import prompt
import hashlib
import os
import time
import datetime
import sys
import fileinput
import pickle
##############################################################################
#                           BU-Verse Variable-Phase                          #
##############################################################################
navlst = ["T", "M", "X"]                                                                # navlst
postfeedlst, postdisnamelst, posttimelst = [], [], []                                   # contentfeed
userlst, pwkeylst, idclst = [], [], []                                                  # LoginCheckSystem
devuserxlst, devpwxlst, devdislst = [], [],[]                                           # DevLoginCheck
namelst, snamelst,disnamelst, majorlst, facultylst = [], [], [], [],[]    # Profile data
ssdisnamelst, ssunamelst = [],[]                                                        # session
timer,sessionActive,run,cnt = 0,0,0,0
uicls = lambda: os.system('cls')
headsignup = ("+" * 64 + "\n\n" + "< [ BU-Verse Sign-up ] >".center(64) + "\n\n" + "+" * 64)
headlogin = ("|"*64 + "\n\n" + "< [ BU-Verse Login ] >".center(64) + "\n\n" + "|"*64)

##############################################################################
#                           BU-Verse Tools-Phase                             #
##############################################################################
def getfile(filecall):
    return os.stat(filecall).st_size

def loading_progress(timer,interval,delay):
    print("[",end="")
    for i in range(timer):
        time.sleep(interval)
        loadder = "■" * i
        print("%s" %loadder, end="")
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
            print("[ Going back to Main menu ]".center(64))
            time.sleep(1.5)
            buverse_main(sessionActive)
        elif nav.upper() == "X":
            buvs_exit()
        else: time.sleep(.1);buvs_navigate()

def buvs_exit():
    time.sleep(0.25)
    uicls()
    time.sleep(0.20)
    print("." * 64)
    sys.exit("[ Exiting the BU-Verse.. ]".center(64) + "\n" + "." * 64)

def buvs_txtlimitlenght(txtlimit,gettxt):
    newinsert = ""
    for i, letter in enumerate(gettxt):
        if i % txtlimit == 0:
            newinsert += '\n'
        newinsert += letter
    newinsert = newinsert[1:]
    return newinsert

def buvs_versemenu(rpoint):
    print("*"*64)
    print()
    print("[1] Posting something? [2] Explore People [3] My Verse".center(64))
    print("[4] <<- Newfeed   [5] *Refresh feed    [6] Oldfeed ->> ".center(64))
    print("[0] Exit  [00] Log-out and Menu  [000] Log-out and Exit".center(64))
    print()
    print("*" * 64)
    vmenu = input("> ")
    if vmenu == "1":
        buverse_verseposting()
    elif vmenu == "2":
        buverse_verseexplore()
    elif vmenu == "3":
        buverse_verseprofile()
    elif vmenu == "4":
        if rpoint>=0:
            buverse_callfeedverse4(rpoint)
        else:
            print("[ No Latest Post Updated Any more. ]")
            time.sleep(1.25)
            buverse_callfeedverse0(0)
    elif vmenu == "5":
        print("[ Updating Verse.. ]")
        time.sleep(1)
        buverse_callfeedverse0(0)
    elif vmenu == "6":
        if rpoint > len(postfeedlst)-1:
            print("[ * This is oldest post in BU-Verse. ]")
            time.sleep(1.25)
            buverse_callfeedverse6(rpoint)
        else:
            buverse_callfeedverse6(rpoint)

    elif vmenu == "0":
        buvs_exit()
    elif vmenu == "00":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1)
        buverse_main(0)
    elif vmenu == "000":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1.5)
        buvs_exit()
    else: buverse_versemain()

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
                with open('buvs_userdb.txt','r',buffering=1)as dbuser,open('buvs_keydb.txt','r')as dbkey:
                    while True:
                        userdata = dbuser.readline().split()
                        pwkeydata = dbkey.readline().split()
                        if userdata != [] and pwkeydata != []:
                            userlst.append(userdata[0])
                            disnamelst.append(userdata[1])
                            pwkeylst.append(pwkeydata[0])
                        else:
                            break
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
                        print(" ".rjust(20),end="");loading_progress(7,0.01,0.1)
                        print("[ Recalling Profile logging-in.. ]".center(64))
                        time.sleep(0.4)
                        print(("[ Welcome back %s ]" % "".join(ssdisname)).center(64))
                        time.sleep(1)
                        uicls()
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
                        uicls()
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
        buverse_versemain()
        buverse_main(sessionActive)
    elif sessionActive == 9:#dev
        uicls()
        #print("sessionActive =", sessionActive)
        print("#"*64)
        print("< [ BU-Verse Developer mode ] >".center(64))
        print(("< [ Welcome Back %s ] >"%ssdisname).center(64))
        print("#" * 64)
        print("\n\n\n")
        input("Enter Main Bu-verse")
        buverse_main(sessionActive)
    else:
        uicls()
        buvs_checklstclear()
        #print("sessionActive =",sessionActive)
        print("#" * 64)
        print()
        print("< [ Welcome to BU-Verse ] >".center(64))
        print("* Please Login to continue! ".center(64))
        print()
        print("#" * 64)
        print()
        print(" "*19+"[1] Log-in")
        print(" "*19+"[2] Sign-up")
        print(" "*19+"[0] Exit the Program")
        print()
        print("-"*64)
        gout = input("Press select menu : ")
        if gout == "1":
            print("[ Going to Login.. ]".center(64))
            print(" ".rjust(20),end="");loading_progress(7,0.02,0.2)
            buverse_login()
        elif gout == "2":
            print("[ Going to Sign-up.. ]".center(64))
            print(" ".rjust(20),end="");loading_progress(7,0.05,0.2)
            buverse_signup()
        elif gout == "0":
            buvs_exit()
        else:
            print("!! Invalid Menu, Please try again.")
            time.sleep(1)
            buverse_main(sessionActive)

def buverse_signup():       # 0000000000000
    uicls()
    buvs_checklstclear()
    print(headsignup)
    with open('buvs_userdb.txt', 'r',buffering=1) as dbuser, open('buvs_keydb.txt', 'r') as dbkey,open('buvs_idcdb.txt', 'r')as dbidc:
        while True:
            userdata = dbuser.readline().split()
            pwkeydata = dbkey.readline().split()
            idcdata = dbidc.readline().split()
            if userdata != [] and pwkeydata != []:
                userlst.append(userdata[0])
                disnamelst.append(userdata[1])
                pwkeylst.append(pwkeydata[0])
                idclst.append(idcdata[0])
            else:
                break
        uname = input("Enter Your Username \n> ")
        if uname not in userlst:
            userlst.append(uname)
            idx = userlst.index(uname)
            buverse_getpwkey(idx)
        else:
            print("")
            strx64 = "x"*64
            print(strx64.center(64))
            print("[ Sorry, this Username is already taken. ]".center(64))
            print("[ Please try again. ]".center(64))
            while True:
                print()
                print("\\" * 64)
                nav = input("( Choose [T] Try again or [M] back to Main menu )\n > ")
                if nav.upper() == "T":
                    buverse_signup()
                elif nav.upper() == "M":
                    buverse_main(0)
                else:
                    continue
        getidcard()
        getdisname()
        with open('buvs_userdb.txt', 'a')as dbuser, open('buvs_keydb.txt', 'a')as dbkey, open('buvs_idcdb.txt', 'a')as dbidc:
            dbuser.write(userlst[idx]+" "+disnamelst[idx]+" \n")
            dbkey.write(pwkeylst[idx]+" \n")
            dbidc.write(idclst[idx]+" \n")
        print("[ BU-Verse Sign-up Successfully. ]")
        time.sleep(0.5)
        while True:
            print("\\" * 64)
            nav = input("( Choose [L] Log-in or [M] back to Main menu )\n > ")
            if nav.upper() == "L":
                buverse_login()
            elif nav.upper() == "M":
                buverse_main(0)
            else:
                continue
    buverse_main(sessionActive)

def buverse_getpwkey(idx):
    pwkey1 = prompt("Enter Your Password (Must have more than 8 characters) \n> ",is_password = True)
    while len(pwkey1) < 8:
        uicls()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx],end="\n")
        print("!! Password Must have more than 8 characters.")
        pwkey1 = prompt("Enter Your Password (Must have more than 8 characters) \n> ",is_password = True)
    pwkey2 = prompt("Confirm Your Password (Must have more than 8 characters) \n> ",is_password=True)
    if pwkey1 == pwkey2:
        pwhashed = pwhash(pwkey1)
        pwkeylst.append(pwhashed)
    else:
        uicls()
        print(headsignup)
        print("Enter Your Username \n> " + userlst[idx])
        print("[ # Those passwords didn't match!! Please try again. ]")
        buverse_getpwkey(idx)

def getidcard():
    idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    while len(idc) != 13 or not idc.isdecimal():
        print("* ID card must have 13 characters and number only")
        idc = input("Enter Your ID card Number (Must be number and more equal 13 character) \n> ")
    idchashed = pwhash(idc)
    idclst.append(idchashed)

def pwhash(pwkey1):
    return hashlib.sha256(str.encode(pwkey1)).hexdigest()

def pwdehash(pwkeyi, dehash):
    return pwhash(pwkeyi) == dehash

def getdisname():
    disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
    disnamecntlst = disname.count(" ")
    while not disname or disnamecntlst != 0:
        print(disname)
        print("** Display Name \"BlankSpace\" not allowed.")
        disname = input("Enter Your Name to display on profile (Can edit after) \n> ")
        disnamecntlst = disname.count(" ")
    disnamelst.append(disname)

def buverse_login():
    uicls()
    buvs_checklstclear()
    ssunamelst.clear();ssdisnamelst.clear()
    with open('buvs_userdb.txt','r',buffering=1)as dbuser,open('buvs_keydb.txt','r')as dbkey:
        while True:
            userdata = dbuser.readline().split()
            pwkeydata = dbkey.readline().split()
            if userdata != [] and pwkeydata != []:
                userlst.append(userdata[0])
                disnamelst.append(userdata[1])
                pwkeylst.append(pwkeydata[0])
            else: break
    with open('buvs_xlogindb.txt','r')as dbxlog:
        while True:
            xdata = dbxlog.readline().split()
            if xdata != []:
                devuserxlst.append(xdata[0])
                devpwxlst.append(xdata[1])
                devdislst.append(xdata[2])
            else:break
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
            time.sleep(2)
            uicls()
            buverse_main(1)
        else:
            print("[ Logging-in Failed. ]".center(64))
            print("[ Wrong Password, Please try again.. ]".center(64))
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
            uicls()
            buverse_main(9)
        else:
            print("[ Logging-in Failed. ]".center(64))
            print("[ Wrong Password, Please try again.. ]".center(64))
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
        while True:
            print("\\" * 64)
            nav = input("( Choose [T] Try again or [M] back to Main menu )\n > ")
            if nav.upper() == "T":
                buverse_login()
            elif nav.upper() == "M":
                buverse_main(0)
            else:
                continue
##############################################################################
#                           BU-Verse Verse-Phase                             #
##############################################################################
def buverse_versemain():
    while True:
        uicls()
        buvs_checklstclear()
        postfulltime = datetime.datetime.now()
        postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
        print("#" * 64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print(("[ %s ]" % ssdisname).center(64))
        if getfile('buvs_postingversedb.txt'):
            with open('buvs_postingversedb.txt','r',buffering=1)as dbposting:
                postdisnamelst.clear();postfeedlst.clear();posttimelst.clear()
                while True:
                    getrawpost = dbposting.readline().split("|*|")
                    if getrawpost != ['']:
                        postdisnamelst.append(getrawpost[0])
                        posttimelst.append(getrawpost[1])
                        getpostfeed = getrawpost[2].replace("\n","")
                        postfeedlst.append(getpostfeed)
                    else:break
                postdisnamelst.reverse();posttimelst.reverse();postfeedlst.reverse()
            time.sleep(0.2)
            buverse_callfeedverse0(rpoint=0)
        else:
            print("\n")
            print("[ No one posts in verse ]".center(64))
            print("\n"*2)
        buvs_versemenu(run)

def buvs_maintitle(headtitle):
    uicls()
    postfulltime = datetime.datetime.now()
    postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
    print("#" * 64)
    print(("[ %s ]"%headtitle).center(64))
    print(postlocaltime.center(64))
    print(("------------------[ %s ]-------------------" % ssdisname).center(64))

def buverse_callfeedverse0(rpoint):
    while True:
        uicls()
        postfulltime = datetime.datetime.now()
        postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
        print("#" * 64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print(("[ %s ]" % ssdisname).center(64))
        for i in range(1):
            print("* Latest Post Updated.",end="\r")
            time.sleep(0.8)
        lenfeed = len(postfeedlst)
        cnt = 0
        time.sleep(0.02)
        for run in range(0, lenfeed):             #default runpost
            print("_" * 64)
            print("[ From", postdisnamelst[run], "At", posttimelst[run] + " ]")
            print(">", buvs_txtlimitlenght(58, postfeedlst[run]))
            print()
            cnt += 1
            rpoint = run
            if cnt == 3:break
        buvs_versemenu(rpoint)

def buverse_callfeedverse4(rpoint):
    while True:
        uicls()
        postfulltime = datetime.datetime.now()
        postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
        print("#" * 64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print(("[ %s ]" % ssdisname).center(64))
        cnt = 0
        time.sleep(0.1)
        for run in range(rpoint-5,rpoint, 1):           #back runpost
            if run < 0:
                print("[ * No Latest Post Updated Any more. ]")
                time.sleep(1)
                buverse_callfeedverse0(0)
            print("_" * 64)
            print("[ From", postdisnamelst[run], "At", posttimelst[run] + " ]")
            print(">", buvs_txtlimitlenght(58, postfeedlst[run]))
            print()
            cnt += 1
            rpoint = run
            if cnt == 3:break
        buvs_versemenu(rpoint)

def buverse_callfeedverse6(rpoint):
    while True:
        uicls()
        postfulltime = datetime.datetime.now()
        postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
        print("#" * 64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print(("[ %s ]" % ssdisname).center(64))
        lenfeed = len(postfeedlst)
        cnt = 0
        time.sleep(0.1)
        if rpoint >= lenfeed-1:
            print("if6")
            rpoint = lenfeed-2
            for run in range(rpoint, lenfeed,1):  # next runpost
                print("_" * 64)
                print("[ From", postdisnamelst[run], "At", posttimelst[run] + " ]")
                print(">", buvs_txtlimitlenght(58, postfeedlst[run]))
                print()
                cnt += 1
                if cnt == 3:
                    break
            rpoint = lenfeed
        else:
            for run in range(rpoint+1, lenfeed):           #next runpost
                print("_" * 64)
                print("[ From", postdisnamelst[run], "At", posttimelst[run] + " ]")
                print(">", buvs_txtlimitlenght(58, postfeedlst[run]))
                print()
                cnt += 1
                rpoint = run
                if cnt == 3:
                    break
        buvs_versemenu(rpoint)

def buverse_verseposting():
    uicls()
    postfulltime = datetime.datetime.now()
    postlocaltime = postfulltime.strftime("%d-%b-%Y") + " " + postfulltime.strftime("( %H:%M:%S )")
    with open('buvs_postingversedb.txt','a+',buffering=1)as dbpostingverse:
        print("#"*64)
        print("[ BU-Verse ]".center(64))
        print(postlocaltime.center(64))
        print("="*64)
        print((">>>> %s Posting in Verse? >>>>>>>>>>>>>>>>>>>" %ssdisname).center(64))
        getpostverse = input("> ")
        recheckgetpostverse = input("Press [Any Key] Post or [0] Cancel\n> ")
        if recheckgetpostverse == "0":
            uicls()
            buverse_versemain()
        else:
            dbpostingverse.write(ssdisname + "|*|" + postlocaltime + "|*|" + getpostverse + "\n")
            uicls()
            buverse_versemain()

def buvs_navpro():
    while True:
        print()

def buvs_callprofile():
    buvs_checklstclear()
    with open('buvs_userdb.txt','r',buffering=1)as dbuser:
        while True:
            udata = dbuser.readline().split()
            if udata != []:
                userlst.append(udata[0])
                disnamelst.append(udata[1])
            else:break

def buverse_verseexplore():
    uicls()
    buvs_maintitle("Explore-Verse")
    buvs_callprofile()
    input()
    pass

def buverse_verseprofile():
    uicls()
    buvs_maintitle("My-Verse")
    buvs_callprofile()
    print("\n| Username : "+userlst[idx])
    print("| Display name : "+disnamelst[idx])
    print("\n\n")
    print("[1] Edit Display name? [2] Explore People [3] Back to Verse".center(64))
    print("[0] Exit  [00] Log-out and Menu  [000] Log-out and Exit".center(64))
    gpro = input()
    if gpro == "1":
        while True:
            uicls()
            buvs_maintitle("My-Verse")
            buvs_callprofile()
            print("\n| Username : " + userlst[idx])
            print("| Display name : " + disnamelst[idx])
            print("\n")
            print("[1] Edit Display name? [2] Explore People [3] Back to Verse".center(64))
            print("[0] Exit  [00] Log-out and Menu  [000] Log-out and Exit".center(64))
            disname = input("Edit Your Display Name (* Display Name \"BlankSpace\" not allowed.)\n> ")
            disnamecntlst = disname.count(" ")
            while not disname or disnamecntlst != 0:
                print(disname)
                disname = input("Edit Your Display Name (* Display Name \"BlankSpace\" not allowed.)\n> ")
                disnamecntlst = disname.count(" ")
            disnamelst[idx] = disname
            cfdisname = input("Press [Any Key] to confirm or [0] Cancel")
            if cfdisname == "0":
                buverse_verseprofile()
            else:
                with open('buvs_userdb.txt','w')as dbuser:
                    for i in range(len(disnamelst)):
                        dbuser.write(userlst[i] + " " + disnamelst[i] + " \n")
                    print("[ Your Display Name has been Change. ]".center(64))
                break
        time.sleep(1)
    elif gpro == "2":
        buverse_verseexplore()
    elif gpro == "3":
        buverse_versemain()
    elif gpro == "0":
        buvs_exit()
    elif gpro == "00":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1)
        buverse_main(0)
    elif gpro == "000":
        with open('buvs_recallsession.txt', 'w') as dbrecallss:
            dbrecallss.flush()
        print("[ Log-out successflly. ]".center(64))
        time.sleep(1.25)
        buvs_exit()
    else:buverse_verseprofile()

##############################################################################
#                           BU-Verse initiate                                #
##############################################################################
buverse_recallsession()
buverse_main(sessionActive)