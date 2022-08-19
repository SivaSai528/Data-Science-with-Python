'''def factorial():
    n=int(input("Enter a Number"))
    s=1
    if n==0:
        print("1")
    else:
        for i in range(1,n+1):
            s*=i
        print(s)
factorial()'''
def powerr(x,y):
    if y==0:
        return 1
    else:
        return x*powerr(x,y-1)
print(powerr(2,3))
