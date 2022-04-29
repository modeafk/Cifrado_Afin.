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

 ![image](https://user-images.githubusercontent.com/90937895/165884683-969ec4b6-d7d7-479a-ae1c-872790fb9cc1.png)


Descifrado:

Es preciso invertir (mod 26) la formula de cifrado con el fin de expresar [x] en función de [y]
Y=ax + b, ecuación para cifrado. Restemos b
Y – b = ax. Para eliminar a, debemos multiplicarlo por su inversa ya que [a-1] . [a]=1

[a-1](y-b)=x

La ecuación de descifrado es pues x= [a-1](y-b) (mod 26). Si el paréntesis (y-b) resulta negativo basta con añadir 26 antes de multiplicarlo por [a-1]

Ejemplo de descifrado

Descifremos el mensaje que hemos calculado anteriormente. Como [a=9], [a-1]=3. La formula de descifrado es pues x=3(y-4) (mod 26)


![image](https://user-images.githubusercontent.com/90937895/165884737-9c9b97d4-d51f-4d1c-8cbd-aca64f042803.png)

 
INSTRUCCIONES:

-El programa pedira al usuario ingresar una cadena para luego ver que es lo que se desea hacer, si es encriptar o desencriptar.

-Una vez seleccionada la opcion se procedera a encriptar o desencriptar la cadena.

-Para la encriptacion o desencriptacion de la cadena se hara uso de una clave, los cuales seran los valores de a y b. Como bien sabemos el valor de "b" vendria a estar
en el anillo de 0 a 27 y el valor de "a" tendria que ser coprimo con 27.

-Despues de ello el mensaje ingresado quedará encriptado o desencriptado segun lo que indico el usuario.

-El programa retorna una cadena con un mensaje encriptado o desencriptado.
 
 
![image](https://user-images.githubusercontent.com/101947482/162352821-c8164f0f-0cc6-4253-9516-79360b465d9d.png)


