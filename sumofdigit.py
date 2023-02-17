x=int(input("enter a no"))
sum=0
while x>0 :
    sum+=x%10
    x=x//10
print("sum of digits",sum)