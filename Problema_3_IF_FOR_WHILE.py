import math
m=int(input('Introduceti baza:'))
n=int(input('Introduceti numarul:'))
a=math.log(n,m)
b=int(a)
if a==b:
    print(n,'este o putere a lui',m)
else:
    print(n,'nu este o putere a lui',m)