def _gcd_(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            gcd = i 
    return gcd

def _lcm_(x, y):
   lcm = (x*y)/_gcd_(x,y)
   return lcm

num1 = int(input("Enter a Number:"))
num2 = int(input("Enter a Number:"))
print(_lcm_(num1,num2))
