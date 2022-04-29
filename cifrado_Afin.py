def e_euclides(a,b): 
    if (b == 0):
      return a,1,0
    d,x1,y1 = e_euclides(b, a % b)
    x = y1
    y = x1 - y1 * int(a / b)
    return d,x,y

def euclides(a, b):
 if b == 0:
  return a
 else:
  return euclides(b, a % b)

def inverso(a,n):
  if (euclides(a,n)==1):
    d,x,y=e_euclides(a,n)
    return(x%n)
  else:
    return "no tiene inverso por la ptmre:"
    
def cifrar(a,b,cadena):
  
  cadena2=""
  abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  
  for i in cadena:
    n=0
    for j in abc:
      if i==j:
        break
      n=n+1 
    y=(a * n + b )% 27
    cadena2=cadena2+abc[y]
  
  return cadena2

def decifrar(a,b,cadena):
  cadena2=""
  abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
  
  for i in cadena:
    n=0
    for j in abc:
      if i==j:
        break
      n=n+1 
    x=(inverso(a,27)*(n-b)) % 27
    cadena2=cadena2+abc[x]
  
  return cadena2

a=(int(input("ingrese 'a': ")))
n=(int(input("ingrese 'n': ")))
print(inverso(a,n))
print("\n")
dr="ELEMENTALMIQUERIDOWATSON"
fr="WXWBWFGHXBMUKWYMSNRHGCNF"
print(cifrar(4,7,dr))
print(decifrar(4,7,fr))