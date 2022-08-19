file=open("siva.txt","w")
file.write("Hello")
file.close()
file=open("siva.txt","r")
text=file.read()
print(text)
file.close()


file1=open("sai.txt","w")
file1.write("Hai")
file1.close()
file1=open("sai.txt","r")
text1=file1.read()
print(text1)
file1.close()

