x=[1,2,3]
i=0
a=[]
a.extend(x)
a.sort()
if a==x:
    print("monotonic")
else :
    print("not monotonic")
