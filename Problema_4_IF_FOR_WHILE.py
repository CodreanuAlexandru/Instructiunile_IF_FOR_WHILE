n1=eval(input('Introduceti numaratorul primei fractii:'))
m1=eval(input('Introduceti numitorul primei fractii:'))
n2=eval(input('Introduceti numaratorul al doile fractii:'))
m2=eval(input('Introduceti numitorul al doile fractii:'))
a=n1*m2+n2*m1
b=m1*m2
if a>b:
    for z in range(a,1,-1):
        if (a%z==0 and b%z==0):
            print(int(a/z),'/',int(b/z))
if a<b:
    for z in range(b,1,-1):
        if (a%z==0 and b%z==0):
            print(int(a/z),'/',int(b/z))
if a==b:
    print(a,'/',b,'=1')