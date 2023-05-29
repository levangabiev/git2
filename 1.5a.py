def gsd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a%=b
        else:
            b%=a
    print('наибольший общий делитель: ',a+b)

a=int(input('Введите первое число: '))
b=int(input('Введите второе число: '))
gsd(a, 84)