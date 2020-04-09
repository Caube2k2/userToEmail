from random import *
author = "[HCSACC - NXH]"    #Please dont remove it
ex = ["gmail.com", "yahoo.com.vn", "yahoo.com", "outlook.com"]


input = open('user.txt', 'r')
input = input.read()
arr = input.splitlines()
for i in arr:
  sp = i.split(":")
  rs = sp[0] + "@" + ex[randint(0, len(ex)-1)] + ":" + sp[1];
  print(rs)
  f2 = open(author + "rs.txt", "a")
  f2.write(rs + "\n")

