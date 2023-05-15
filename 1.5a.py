def gsd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    print('наибольший общий делитель: ',a+b)

gsd(22, 84)