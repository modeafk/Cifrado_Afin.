##ALGEBRA ABSTRACTA

**Integrantes**

-Marcelo Torres Acuña

-Jhon Berly Taype Alccaccahua 

-Brian Bermudez Navarro

------------

#### **El Cifrado Afín**


 Este se realizo mediante el lenguaje de programacion python.  
  
 
 DESCRIPCIÓN:
 
- Es un tipo de cifrado por sustitución en el que cada símbolo del alfabeto en claro (el alfabeto del texto en claro) es sustituido por un símbolo 
del alfabeto cifrado (el alfabeto del texto cifrado) siendo el número de símbolos del alfabeto en claro igual que el número de símbolos del alfabeto cifrado. 
Para hallar el símbolo del alfabeto cifrado que sustituye a un determinado símbolo del alfabeto en claro, se usa una función matemática afín en aritmética modular. 
Para poder aplicar la función matemática lo primero que hay que hacer es asignar un orden que a cada símbolo de cada uno de los alfabeto le asocie un número de orden.

Cifrado:
La idea consiste en usar como función de cifrado una función afín del tipo y=ax+b en las que [a] y [b] son constantes, y en las que [x] e [y] son números 
correspondientes a las letras del alfabeto en base a esta tabla

Descifrado:

Es preciso invertir (mod 26) la formula de cifrado con el fin de expresar [x] en función de [y]
Y=ax + b, ecuación para cifrado. Restemos b
Y – b = ax. Para eliminar a, debemos multiplicarlo por su inversa ya que [a-1] . [a]=1

[a-1](y-b)=x

La ecuación de descifrado es pues x= [a-1](y-b) (mod 26). Si el paréntesis (y-b) resulta negativo basta con añadir 26 antes de multiplicarlo por [a-1]

Ejemplo de descifrado

Descifremos el mensaje que hemos calculado anteriormente. Como [a=9], [a-1]=3. La formula de descifrado es pues x=3(y-4) (mod 26)

 
 ![image](https://user-images.githubusercontent.com/101947482/162351477-c0b936fa-b1de-4e40-b042-76424b6db7a2.png)


 
INSTRUCCIONES:

-El programa pedira al usuario ingresar 2 numeros, el primer para darle el valor de "a", el segundo para darle el valor de "b"

-Una vez ingresado los numeros, el pograma hallara el m.c.d de esos numeros y los imprimira en pantalla.

-El programa se encargara de botar los resultados en pantalla tanto el mcd como los valores respectivos de "x" y "y"
 
 
![image](https://user-images.githubusercontent.com/101947482/162352821-c8164f0f-0cc6-4253-9516-79360b465d9d.png)


