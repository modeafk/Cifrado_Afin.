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


![image](https://user-images.githubusercontent.com/90937895/165884683-969ec4b6-d7d7-479a-ae1c-872790fb9cc1.png)


Cifrado:

- Para cifrar haremos uso de la cadena ingresada, haremos uso de una clave de ("a","b" y una cadena predefinida por 27 caracteres que serian los las letras del abecedario(De la letra A a la Z)
-Luego haremos uso de la siguiente ecuacion:


![image](https://user-images.githubusercontent.com/90937895/165886369-fed73f15-176d-4cdc-bd39-1259ffb90cd3.png)


 En donde "y" esta definido por el inverso de a,27 multiplicado por y-b y al final aplicaremos modulo de 27

Descifrado:
- Para descifrar haremos uso de la cadena ingresada, haremos uso de una clave de ("a","b" y una cadena predefinida por 27 caracteres que serian los las letras del abecedario(De la letra A a la Z)
-Luego haremos uso de la siguiente ecuacion:

![image](https://user-images.githubusercontent.com/90937895/165885818-21ae22ec-ac84-43e3-80ee-04d72ca756cb.png)

 En donde "x" esta definido por el inverso de a,27 multiplicado por y-b y al final aplicaremos modulo de 27
 Ademas, a' es el inverso y el par {a,b} seria la llave


![image](https://user-images.githubusercontent.com/90937895/165884737-9c9b97d4-d51f-4d1c-8cbd-aca64f042803.png)

 
INSTRUCCIONES:

-El programa pedira al usuario ingresar una cadena para luego ver que es lo que se desea hacer, si es encriptar o desencriptar.

-Una vez seleccionada la opcion se procedera a encriptar o desencriptar la cadena.

-Para la encriptacion o desencriptacion de la cadena se hara uso de una clave, los cuales seran los valores de a y b. Como bien sabemos el valor de "b" vendria a estar
en el anillo de 0 a 27 y el valor de "a" tendria que ser coprimo con 27.

-Despues de ello el mensaje ingresado quedará encriptado o desencriptado segun lo que indico el usuario.

-El programa retorna una cadena con un mensaje encriptado o desencriptado.

SALIDA:

 ![image](https://user-images.githubusercontent.com/90937895/165886800-684b462f-90c7-4afb-9dfc-c50ac77f6405.png)

 ![image](https://user-images.githubusercontent.com/90937895/165886830-5504f77e-334b-4812-8f8d-a49ee0f74a5e.png)



