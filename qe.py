import math as m
a=int(input("a"))
b=int(input("b"))
c=int(input("c"))
d=b*b-4*a*c
r1=(-b+m.sqrt (d))/(2*a)
r2=(-b-m.sqrt (d))/(2*a)
print(r1)
print(r2)