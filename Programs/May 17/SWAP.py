print("Before Swapping")

file=open("siva.txt","r")
A=file.read()
print(A)
file.close()

file1=open("sai.txt","r")
B=file1.read()
print(B)
file1.close()

file=open("siva.txt","w")
file.write(B)
file.close()

file1=open("sai.txt","w")
file1.write(A)
file1.close()

print("After Swapping")

file=open("siva.txt","r")
print(file.read())
file.close()

file1=open("sai.txt","r")
print(file1.read())
file1.close()
