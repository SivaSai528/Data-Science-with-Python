S=int(input("Enter a Number :"))
V=int(input("Enter a Number :"))
def Coprime(S,V):
    A=S
    if S>V:
        A=V
    for i in range(1,A+1):
        if S%i==0 and V%i==0: 
            P=i
    if P==1:
        print("Both are in Coprime")
    else:
        print("Both are not in Coprime")
Coprime(S,V)