#!/bin/python
'''
By:Ahmed
Whatsapp: https://wa.me/+201150119895
Website:https://ahmedc00.tech
Email:Ahmed@ahmedc00.tech
GitHub:https://github.com/ahmedMahmed8a
This is a very simple code using sympy for getting the eigenvalues and the quadratic form of the matrix
'''
import subprocess
import sympy as sp
def readint():
 n="-1234567890"
 x=subprocess.check_output("read -n 1 x;echo -n $x",shell=True,executable="/bin/bash").decode().replace("\n","")
 y=""
 ooo=True
 while(ooo):
  if(not(x in n)):
   if(x=="\x1b"):
    print("\x08\x08",end="",flush=True)
    if(y):
     break;
     ooo=False
   else:
    print("\x08",end="",flush=True)
  else:
   y=y+x
  x=subprocess.check_output("read -n 1 x;echo -n $x",shell=True,executable="/bin/bash").decode().replace("\n","")
 return y
def main():
 print("\n\x1b[0;92mMatrix A \x1b[0;94m[must be n*n]\x1b[0;93m(ESC to move to other element): ",end="",flush=True)
 rows=readint()
 print("\x20x\x20",end="",flush=True);
 cols=readint()
 if(int(cols)!= int(rows)):
  print("\x1b[05;91m Matrix must be n*n",flush=True,end="")
  main()
  exit()
 row=[]
 o=[]
 print("\x1b[92m\n",flush=True,end="")
 for i in range(int(rows)):
  print("[",end=" ",flush=True)
  col=[]
  o.append(sp.var("x"+str(i+1)))
  for j in range(int(cols)):
   s=readint()
   col.append(int(s))
   print("\x20",end="",flush=True)
  print("]\n",end="",flush=True)
  row.append(col)
 mat=sp.Matrix(row)
 a=sp.Matrix(o)
 at=a.transpose()
 atmat=at*mat
 matform=atmat*a
 print("\x1b[92mThe quadratic form is:\x1b[95m",matform[0])
 print("\x1b[92mThe eigenvalues of the matrix are\x1b[95m:",mat.eigenvals())
main()
