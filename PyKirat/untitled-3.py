plaintext=list(raw_input("Enter PlainText: "))
key=list(raw_input("Enter key: "))

binary=[]

for i in plaintext:
    binary.extend(list(bin(ord(i))[2:]))
print binary
    
full_key=[]

for j in range((len(binary)/len(key))+1):
    full_key.extend(key)
print full_key

code=[]

loc=0
for k in binary:
    if k==full_key[loc]:
        code.append('0')
    else:
        code.append('1')
    loc+=1
#-----------------------------    
mode=input("Choose Encryption mode:\n1.키랏-mode\n2.가루바나나-mode\n>")    
if mode==1:
    one="키랏"
    zero="★"
else:
    one="가루★"
    zero="바나나!"
#-------------------------------

print code

for l in code:
    if l=='1':
        print one,
    else:
        print zero,