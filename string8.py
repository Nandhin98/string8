  a=input()
  b=input()
  c="abcdefghijklmnopqrstuvwxyz"
  d=[]
  e=[]
  m=""
 for i in range(0,len(a)):
     for j in range(0,len(c)):
         if a[i]==c[j]:
             d.append(j+1)
         if b[i]==c[j]:
             e.append(j+1)
 for k in range(0,len(d)):
    tot=d[k]+e[k]
     if(tot<=26):
         m=m+c[tot-1]
     else:
         n=tot-26
         m=m+c[n-1]
 print(m)
