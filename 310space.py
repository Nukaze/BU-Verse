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

def busociety_main():
    if uname in userlst:
        print("#"*64)
        print("< [ Welcome to BU-Society ] >".center(64))
        print("< [ %s ] >".center(64) %uname)
        print("#"*64)
        print("/" * 64)
        print("/" * 64)
        print("\\" * 64)
        print("\\" * 64)
    else:
        print("#" * 64)
        print("< [ Welcome to BU-Society ] >".center(64))
        print("* Please Login to continue ".center(64))

        print("#" * 64)
        input("Press any key to Login.. ")
        busociety_login()



def busociety_login():
    print("|"*64)
    print("<[ BU-Society Login ]>".center(64))
    print("|"*64)





busociety_main()