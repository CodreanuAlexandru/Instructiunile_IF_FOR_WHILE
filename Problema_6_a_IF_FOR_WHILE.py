s1=0
s2=0
n=eval(input('Introduceti n='))
for a in range(1,n+1):
    s1+=a**3
    s2+=a
if s1>(s2**2):
    print(s1,' este mai mare ca', s2)
if s1<(s2**2):
    print(s2, 'este mai mare ca', s1)  
if s1==(s2**2):
    print(s1,' este egal cu', s2**2)  