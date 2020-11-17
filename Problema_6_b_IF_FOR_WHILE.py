s1=0
s2=0
n=eval(input('Introduceti n='))
for a in range(1,n+1):
    s1+=a**2
    s2+=a
s2+=n**2
s2+=n**3
s1*=3
if s1>s2:
    print(s1,' este mai mare ca', s2)
if s1<s2:
    print(s2, 'este mai mare ca', s1)  
if s1==s2:
    print(s1,' este egal cu', s2) 