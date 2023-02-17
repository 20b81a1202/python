n=int(input("enter a no"))
digits=0
temp=n
while temp != 0 :
    digits = digits+1
    temp = temp//10
t=n
num = 0
while t!=0 :
    rem = t%10
    num += rem**digits
    t=t//10
if num==n :
    print("amstrong")
else :
    print("not amstrong")


