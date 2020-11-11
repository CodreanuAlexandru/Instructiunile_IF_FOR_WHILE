n=int(input('Introduceti n='))
b=1
s=0
for a in range(1,n+1):
    b*=a
    s+=b
print(s)