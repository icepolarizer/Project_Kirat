#Made by unixforever
#Kirat!
#-*- coding: utf-8 -*-
data=list(raw_input("Enter PlainText: "))
binary=[]
for i in data:
    binary.append(bin(ord(i)))
for j in binary:
    for k in list(j[2:]):
        if k=='1':
            print "키랏",
        else:
            print "★",
