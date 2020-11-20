a=eval(input('Introduceti a='))
b=eval(input('Introduceti b='))
c=eval(input('Introduceti c='))
if (a+b>c) and (a+c>b) and (b+c>c):
    if (a==b) and (a==c) and (b==c):
        print('Echilateral')
    elif (a==b) or (a==c) or (b==c):
        print ('Isoscel')
    else:
        print('Scalen')
else:
    print('Asa triunghi nu exista')