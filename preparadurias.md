# Preparadurías Algoritmos y Programacion

**Preparadora:** Stefani Perez

# Contenido

- [Preparadurías Algoritmos y Programacion](#preparadurías-algoritmos-y-programacion)
- [Contenido](#contenido)
- [Introducción a la materia](#introducción-a-la-materia)
  - [Notion](#notion)
  - [Instalaciones](#instalaciones)
    - [Guías de Instalación de Python Visual Studio Code y Git](#guías-de-instalación-de-python-visual-studio-code-y-git)
  - [Slack](#slack)
  - [Visual Studio Code](#visual-studio-code)
    - [Extensiones](#extensiones)
  - [Replit](#replit)
- [Preparaduría 1](#preparaduría-1)
  - [Comandos Basicos de la Terminal](#comandos-basicos-de-la-terminal)
  - [Indentacion](#indentacion)
  - [Escritura de Informacion](#escritura-de-informacion)
  - [Comentarios](#comentarios)
  - [Variables](#variables)
  - [Tipos de Datos](#tipos-de-datos)
  - [Operadores](#operadores)
    - [Operadores Aritmeticos](#operadores-aritmeticos)
    - [Operadores de Asignacion](#operadores-de-asignacion)
    - [Operadores de Comparacion](#operadores-de-comparacion)
    - [Operadores Logicos](#operadores-logicos)
    - [Operadores de Identidad](#operadores-de-identidad)
    - [Operadores de Membresia](#operadores-de-membresia)
  - [Lectura de Informacion](#lectura-de-informacion)
  - [Formato de Cadenas](#formato-de-cadenas)
  - [Ejercicios](#ejercicios)
    - [Ejercicio 1](#ejercicio-1)
    - [Ejercicio 2 (Tarea)](#ejercicio-2-tarea)
    - [Ejercicio 3 (Tarea)](#ejercicio-3-tarea)
    - [Ejercicio 4 (Tarea)](#ejercicio-4-tarea)
    - [Ejercicio 5 (Tarea)](#ejercicio-5-tarea)
- [Preparaduría 2](#preparaduría-2)
  - [If, elif y else](#if-elif-y-else)
  - [While](#while)
  - [Listas](#listas)
    - [Caracteristicas de las listas](#caracteristicas-de-las-listas)
    - [Metodos de listas](#metodos-de-listas)
    - [Matriz (Lista de listas)](#matriz-lista-de-listas)
  - [For](#for)
    - [Rango](#rango)
  - [Funciones](#funciones)
  - [Metodos de cadenas](#metodos-de-cadenas)
  - [Ejercicios](#ejercicios-1)
    - [Ejercicio 8](#ejercicio-8)
    - [Ejercicio 9 (Tarea)](#ejercicio-9-tarea)
    - [Ejercicio 10](#ejercicio-10)
    - [Ejercicio 14](#ejercicio-14)
    - [Ejercicio 15 (Tarea)](#ejercicio-15-tarea)
    - [Ejercicio 16 (Tarea)](#ejercicio-16-tarea)
    - [Ejercicio 17](#ejercicio-17)
    - [Ejercicio 18](#ejercicio-18)
    - [Ejercicio 19 (Tarea)](#ejercicio-19-tarea)
    - [Ejercicio 21 (Tarea)](#ejercicio-21-tarea)
    - [Ejercicio 23](#ejercicio-23)
    - [Ejercicio 24 (Tarea)](#ejercicio-24-tarea)
    - [Ejercicio 25 (Tarea)](#ejercicio-25-tarea)
    - [Ejercicio 26](#ejercicio-26)
    - [Ejercicio 27 (Tarea)](#ejercicio-27-tarea)

# Introducción a la materia

## Notion
https://algoritmos-y-programacion-unimet.notion.site/Preparadur-as-Algoritmos-y-Programaci-n-ebc3b9f0602242afa1818402ac091597

## Instalaciones

### Guías de Instalación de Python Visual Studio Code y Git
https://www.notion.so/algoritmos-y-programacion-unimet/Preparadur-as-Algoritmos-y-Programaci-n-ebc3b9f0602242afa1818402ac091597#08f5e74dfa4345548a35eca9d310d874

## Slack
https://slack.com/intl/es-ve/

## Visual Studio Code
https://code.visualstudio.com/

### Extensiones
https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode
https://marketplace.visualstudio.com/items?itemName=ms-python.python

## Replit
https://replit.com/



# Preparaduría 1

## Comandos Basicos de la Terminal

| Comando     | Funcion                                                 |
| ----------- | ------------------------------------------------------- |
| dir         | Muestra carpetas y archivos del directorio actual       |
| cd          | Permite cambiar de directorio                           |
| cls         | Vacia la consola                                        |
| cd ../      | Permite regresar al directorio anterior                 |
| cd /        | Permite ir al directorio *raiz*                         |
| del         | Borra el archivo indicado                               |
| mkdir       | Crea una carpeta                                        |
| rmdir       | Borra una carpeta                                       |

## Indentacion
Son los espacios al comienzo de cada línea de nuestro código, de esta manera python indica bloques de codigo.

**Input**
```python
if True:
	print("Hello world")
```
**Output**
```shell
Hello world
```
En el codigo anterior python entiende que si se cumple la condicion del *if*, entonces debe ejecutar el bloque de codigo que esta **dentro** de este *if*. Tienes que usar la misma cantidad de espacios en el mismo bloque de código, de lo contrario tu codigo puede fallar.

**Input**
```python
if True:
print("Hello world")
```
**Output**
```shell
File "main.py", line 2
    print("Hello world")
    ^
IndentationError: expected an indented block
```
Mientras que este ultimo codigo nos daria un error de indentacion porque no encuentra un bloque de codigo dentro del *if*

## Escritura de Informacion
Podemos *imprimir* en la consola con **print()** y podemos concatenar cadenas con **+**

**Input**
```python
print("Hello world")
print("Hello" + "world")
```
**Output**
```shell
Hello world
Helloworld
```

Sin embargo, si intentamos concatenar una cadena con un numero mediante **+** tendremos un error. Para estos casos podemos cambiar el tipo de dato del numero o usar **,**

**Input**
```python
print(1 , " es un numero")
```
**Output**
```shell
1  es un numero
```

## Comentarios
Los comentarios nos ayudan a explicar de forma resumida nuestro codigo, de esta forma nuestro codigo llega a ser mas *legible*. Aunque, tambien llegamos a usarlos para evitar que python ejecute partes de nuestro codigo.

**Input**
```python
# Esto es un comentario de una linea
"""
Esto es
un comentario
multilinea
"""
print("Hello world") # Se imprimira por consola
#print ("Algoritmos") # No se imprimira por consola
```
**Output**
```shell
Hello world
```

## Variables
Utilizaremos las variables para guardar informacion. A diferencia de otros lenguajes, python no tiene ningún comando para declarar una variable, y no requiere indicar el tipo de dato que se guardara. Ademas, permite cambiar el tipo de dato de la variable en cualquier momento

```python
numero_1 = 10 #Tipo entero (int)
numero_1 = ' 10 ' #Tipo cadena (str)
numero_1 = " 10 " #Tipo cadena (str)
```
Los nombres de variables:

- Son sensibles a mayusculas y minusculas.
- Deben comenzar con a-z o _
- Solo deben contener letras, numeros y _

Podemos crear mas de una variable en una misma linea de codigo

**Input**
```python
x, y = 1, 2
print(y)
```
**Output**
```shell
2
```

Igualmente, le podemos asignar el mismo valor a distintas variables
```python
x = y = 1
print(x)
```
**Output**
```shell
1
```

## Tipos de Datos
Las variables pueden almacenar diferentes tipos de datos, como por ejemplo:
| Tipo        | Clase       | Ejemplo                                           |
| ----------- | ----------- | ------------------------------------------------- |
| str         | Cadena      | "Hello", 'Hello'                                  |
| int         | Entero      | 11                                                |
| long        | Entero      | 11                                                |
| float       | Decimal     | 11.5                                              |
| complex     | Complejo    | 1j                                                |
| bool        | Booleano    | True, False                                       |
| list        | Secuencia   | ["1", "2", "3"]                                   |
| tuple       | Secuencia   | ("1", "2", "3")                                   |
| dict        | Diccionario | {"nombre" : "Stefani", "apellido" : "Perez"}      |
| set         | Conjunto    | {"1", "2", "3"}                                   |

Si deseamos conocer el tipo de dato de alguna variable podemos usar **type()**

**Input**
```python
numero_2 = 50 #Tipo entero (int)
print(type(numero_2))

```
**Output**
```shell
<class 'int'>
```
Pueden leer un poco mas sobre los tipos de datos en python en este link: https://eiposgrados.com/blog-python/tipos-de-datos-de-python/

## Operadores

Utilizaremos los operadores para realizar diferentes operaciones sobre la informacion

### Operadores Aritmeticos

| Operador    | Operacion           | Ejemplo                                           |
| ----------- | ------------------- | ------------------------------------------------- |
| +           | Suma                | x + y                                             |
| -           | Resta               | x - y                                             |
| *           | Multiplicacion      | x * y                                             |
| /           | Division            | x / y                                             |
| %           | Resto               | x % y                                             |
| **          | Exponenciación      | x ** y                                            |
| //          | Division redondeada | x // y                                            |

### Operadores de Asignacion

| Operador    | Ejemplo             | Lo mismo que...                                   |
| ----------- | ------------------- | ------------------------------------------------- |
| =           | x = 1               | x = 1                                             |
| +=          | x += 1              | x = x + 1                                         |
| -=          | x -= 1              | x = x - 1                                         |
| *=          | x *= 1              | x = x * 1                                         |
| /=          | x /= 1              | x = x / 1                                         |
| %=          | x %= 1              | x = x % 1                                         |
| **=         | x **= 1             | x = x ** 1                                        |
| //=         | x //= 1             | x = x // 1                                        |

### Operadores de Comparacion

| Operador    | Comparacion         | Ejemplo                                           |
| ----------- | ------------------- | ------------------------------------------------- |
| ==          | Igual               | x == y                                            |
| !=          | No igual            | x != y                                            |
| >           | Mayor que           | x > y                                             |
| <           | Menor que           | x < y                                             |
| >=          | Mayor o igual que   | x >= y                                            |
| <=          | Menor o igual que   | x <= y                                            |

### Operadores Logicos

| Operador    | Explicacion                                         | Ejemplo                                           |
| ----------- | --------------------------------------------------- | ------------------------------------------------- |
| and         | Verdadero si ambas condiciones son verdaderas       | x == y and x == z                                 |
| or          | Verdadero si una o ambas condiciones son verdaderas | x == y or x == z                                  |
| not         | Verdadero si la condicion es falsa                  | not(x == y)                                       |

### Operadores de Identidad

| Operador    | Explicacion                                             | Ejemplo                                           |
| ----------- | ------------------------------------------------------- | ------------------------------------------------- |
| is          | Verdadero si ambas variables son el mismo objeto        | x is y                                            |
| is not      | Verdadero si ambas variables **no** son el mismo objeto | x is not y                                        |

### Operadores de Membresia

| Operador    | Explicacion                                             | Ejemplo                                           |
| ----------- | ------------------------------------------------------- | ------------------------------------------------- |
| in          | Verdadero si esta presente en el objeto                 | x in y                                            |
| not in      | Verdadero si no esta presente en el objeto              | x not in y                                        |

## Lectura de Informacion

Utilizaremos **input()** para solicitarle informacion al usuario

**Input**
```python
numero = input("Ingrese un numero por favor") #Imaginemos que el usuario ingresa 73
print(numero)

```
**Output**
```shell
73
```

## Formato de Cadenas

Podemos usar **format()** para *editar* una cadena

**Input**
```python
nombre = "Stefani"
apellido = "Perez"
cargo = "preparadora"
nro_prepa = 1
saludo = "Hola soy su {}, mi nombre es {} {} y esta es nuestra prepa nro {:.2f}."
print(saludo.format(cargo, nombre, apellido, nro_prepa))

```
**Output**
```shell
Hola soy su preparadora, mi nombre es Stefani Perez y esta es nuestra prepa nro 1.00.
```
Les recomiendo leer un poco mas sobre **format()** en este link: https://www.w3schools.com/python/python_string_formatting.asp

## Ejercicios

### Ejercicio 1
Escribir un programa que le pida al usuario la siguiente informacion: *nombre*, *apellido*, *edad*, y *nro de trimestre actual* (cada dato debe estar en una variable distinta). Luego, muestre por pantalla:

**Output**
```shell
¡Hola soy (nombre) (apellido)! Tengo (edad) y este es mi trimestre nro (nro de trimestre actual)
```
Cada dato debe ser el que haya sido introducido por el usuario.

### Ejercicio 2 (Tarea)
Escribir un programa que le pida al usuario el *número de horas trabajadas*, y el *pago por hora*. Posteriormente, debe mostrar por pantalla la paga que le correspondria si el usuario fuera **100%** efectivo, pero como sabemos que la mitad del tiempo estuvo jugando *League of Legends*, tambien debe indicar cual seria su pago real si solo se le paga un **50%**.

**Output**
```shell
Numero de horas trabajadas: (número de horas trabajadas)
Pago por hora: (pago por hora)
¡Hola trabajador! Tu pago deberia ser (pago ideal)$, pero como no cumpliste con nuestras expectativas te daremos (pago real)$.
```

### Ejercicio 3 (Tarea)
Escribir un programa que pida un numero positivo **n** al usuario, y después muestre por pantalla la *suma de todos los enteros desde 1 hasta **n***. Tenga en cuenta que los numeros decimales deben ser *de alguna forma* transformados a enteros.

**Output**
```shell
Numero: (n)
¡Hola usuario! La suma de todos los enteros desde 1 hasta (n) da como resultado (resultado).
```

### Ejercicio 4 (Tarea)
Escribir un programa que pida al usuario su **peso** (en kg) y **estatura** (en metros), y que luego calcule el **índice de masa corporal** del usuario y que muestre por pantalla:

**Output**
```shell
Peso: (peso)kg
Estatura: (estatura)m
Tu índice de masa corporal es (índice de masa corporal).
```
El índice de masa corporal calculado debe ser redondeado a *dos decimales*.

### Ejercicio 5 (Tarea)
Escribir un programa que le pida al usuario *dos números* y que imprima por pantalla:

**Output**
```shell
Numero 1: (numero 1)
Numero 2: (numero 2)
(numero1) entre (numero2) da un cociente (cociente) y un resto (resto).
```



# Preparaduría 2

## If, elif y else
Las sentencias *If* nos permiten ejecutar bloques de codigo de acuerdo a si una condicion es **verdadera**. Mientras que con las sentencias *elif* podemos tener en cuenta mas casos. Si **ningun caso** se cumple, entonces se ejecutara lo que este dentro de la sentencia *else* (en caso de existir). 

```python
cadena = input("Ingrese una palabra")
if (cadena[0] == "A"):
  print("La primera letra de la palabra es A.")
elif (cadena[0] == "B"):
    print("La primera letra de la palabra es B.")
elif (cadena[0] == "C"):
    print("La primera letra de la palabra es C.")
else:
  print("La primera letra de la palabra no es A, B ni C.")
```

## While
Con while podemos ejecutar el mismo bloque de codigo *una y otra vez*, siempre que una condición sea **verdadera**. 

```python
print('Inicia el programa')
cadena = ''
while (cadena != '10'):
    cadena = input("Ingrese el numero 10: ")
print('Termina el programa')
```

Tenemos que tener cuidado al usar los while ya que podemos generar un **bucle infinito**. Si corren el siguiente codigo, veran que el programa nunca saldra del bucle.

```python
print('Inicia el programa')
num = 0
while (num >= 0):
    print(num)
    num += 1
print('Termina el programa')
```

Tambien tenemos otra forma de finalizar un while,podemos usar *break* para esto:

```python
print('Inicia el programa')
num = 0
while (num >= 0):
    print(num)
    num += 1
    if (num == 10):
      break
print('Termina el programa')
```

Ademas, si queremos saltar una ejecucion del while podemos usar *continue*. Si corren el siguiente codigo podran ver que el numero 5 no se va a imprimir:

```python
print('Inicia el programa')
num = 0
while (num < 10):
    num += 1
    if(num == 5):
      continue
    print(num)
print('Termina el programa')
```

## Listas
Las listas nos permiten almacenar varios elementos en una misma variable y se crean usando **corchetes**.

**Input**
```python
listaDeNombres = ["Andres", "Laura", "Luis"]
print(listaDeNombres)
```

**Output**
```shell
['Andres', 'Laura', 'Luis']
```

Tambien  podemos crear una lista usando **list()**:

```python
listaDeNombres = list(("Andres", "Laura", "Luis"))
print(listaDeNombres)
print(listaDeNombres[1]) #Laura
print(listaDeNombres[-1]) #Luis
```

Podemos generar otra lista con un **rango de indices** indicando dónde comenzar y dónde terminar. El valor devuelto será una *nueva lista* con los elementos especificados.

**Input**
```python
listaDeNombres = ["Andres", "Laura", "Luis", "Rommel", "Andrea"] # Indices: 0 1 2 3 4
print(listaDeNombres[1:4]) # 1 2 3
print(listaDeNombres[:4]) # 0 1 2 3
print(listaDeNombres[-3:-1]) # -3 -2
```

**Output**
```shell
['Laura', 'Luis', 'Rommel']
['Andres','Laura', 'Luis', 'Rommel']
['Luis', 'Rommel']
```

Podemos usar **in** para saber si un elemento esta en la lista.

```python
listaDeNombres = ["Andres", "Laura", "Luis", "Rommel", "Andrea"] # Indices: 0 1 2 3 4
if "Luis" in listaDeNombres:
  print("Luis esta en la lista de nombres")
else:
  print("Luis no esta en la lista de nombres")
```

Si queremos cambiar un elemento de la lista podemos hacerlo mediante los indices:

**Input**
```python
listaDeNombres = ["Andres", "Laura", "Luis", "Rommel", "Andrea"] # Indices: 0 1 2 3 4
listaDeNombres[1] = "Sofia"
print(listaDeNombres)
```

**Output**
```shell
['Andres', 'Sofia', 'Luis', 'Rommel', 'Andrea']
```

### Caracteristicas de las listas
- Las listas permiten valores repetidos.
- Los elementos de la lista están ordenados (los elementos tienen un orden definido y ese orden "no" cambiará.).
- Los elementos de la lista pueden ser cambiados (podemos cambiar, agregar y eliminar elementos de la lista).
- Los elementos de la lista están indexados, esto quiere decir que el primer elemento tiene índice [0], el segundo elemento tiene índice [1]...
- Los elementos de la lista pueden ser de cualquier tipo de dato.

### Metodos de listas

| Metodo      | Explicacion                                                                           |
| ----------- | ------------------------------------------------------------------------------------- |
| len()       | Indica el tamaño de la lista                                                          |
| append()    | Agrega un elemento al final de la lista                                               |
| clear()     | Vacia la lista (elimina todos los elementos)                                          |
| copy()      | Crea una copia de la lista                                                            |
| count()     | Indica el numero de elementos en la lista con el valor indicado                       |
| extend()    | Agrega los elementos de una lista(o cualquier iterable) al final de la lista actual   |
| index()     | Devuelve el índice del primer elemento con el valor especificado                      |
| insert()    | Agrega un elemento a la lista en la posición indicada                                 |
| pop()       | Elimina el elemento de la posición indicada (por defecto es el ultimo elemento)       |
| remove()    | Elimina el elemento con el valor indicado                                             |
| reverse()   | Invierte el orden de la lista                                                         |
| sort()      | Ordena la lista                                                                       |

Si quieren investigar un poco mas sobre estos metodos: 
['List Methods'](https://www.w3schools.com/python/python_lists_methods.asp)

### Matriz (Lista de listas)
Con las listas podemos crear matrices, que en verdad serian listas de listas.

**Input**
```python
matriz = [[1,2,3], [4,5,6], [7,8,9]]
print(matriz)
print(matriz[2][1])
```
**Output**
```shell
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
8
```

## For
Usamos **for** para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena). De esta forma podemos ejecutar un bloque de codigo una vez por cada elemento de la secuencia o de acuerdo a un rango.

**Input**
```python
listaDeNumeros = [1, 70, 3, 7, 6]
for numero in listaDeNumeros:
  print(numero)
```

**Output**
```shell
1
70
3
7
6
```

Podemos recorrer cadenas con **for**:

**Input**
```python
cadena = "Hello"
for letra in cadena:
  print(letra)
```

**Output**
```shell
H
e
l
l
o
```

Al igual que con while, podemos usar **break** para detener el bucle for, y podemos tambien usar **continue** como se indico con while.

**Input**
```python
cadena = "Hello"
for letra in cadena:
  if(letra == "l"):
    break
  else:
    print(letra)
```

**Output**
```shell
H
e
```

### Rango
Para ejecutar un bloque de codigo un número específico de veces, podemos usar **range()**. La función **range()** devuelve una secuencia de números, comenzando desde 0 (por defecto), se incrementa en 1 (por defecto) y termina en un número específico (requerido).

**Input**
```python
contador = 0
for x in range(10):
  contador += x
  print(x)
print('El resultado es: ', contador)
```

**Output**
```shell
0
1
2
3
4
5
6
7
8
9
El resultado es:  45
```
Podemos indicarle a **range()** el inicio del rango:

**Input**
```python
contador = 0
for x in range(5,10):
  contador += x
  print(x)
print('El resultado es: ', contador)
```

**Output**
```shell
5
6
7
8
9
El resultado es:  35
```

Ademas, tambien podemos indicarle a **range()** el incremento o decremento del valor inicio:

**Input**
```python
contador = 0
for x in range(5,10,2):
  contador += x
  print(x)
print('El resultado es: ', contador)
```

**Output**
```shell
5
7
9
El resultado es:  21
```

## Funciones
Una función es un bloque de código que solo se ejecuta cuando se le llama. Las funciones pueden recibir datos (*parametros*) y tambien  pueden *retornar* datos como resultado de su llamada. Para crear una funcion debemos usar **def**:

**Input**
```python
def imprimir(cadena):
  print(cadena)

imprimir("Holaa") #Llamada de la funcion enviandole un parametro string
```

**Output**
```shell
Holaa
```

## Metodos de cadenas

| Metodo         | Explicacion                                                                           |
| -------------- | ------------------------------------------------------------------------------------- |
| capitalize()   | Convierte el primer caracter en mayúscula                                             |
| lower()        | Convierte toda la cadena en minusculas                                                |
| upper()        | Convierte toda la cadena en mayusculas                                                |
| center()       | Devuelve una cadena centrada (requiere indicar el numero de espacios)                 |
| count()        | Devuelve la cantidad de veces que aparece en la cadena el valor indicado              |
| endswith()     | Devuelve verdadero si la cadena termina con el valor indicado                         |
| find()         | Busca en la cadena un valor específico y devuelve la posición donde se encontró       |
| format()       | Nos permite agregar variables a una cadena                                            |
| index()        | Busca en la cadena un valor específico y devuelve la posición donde se encontró       |
| isalnum()      | Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos             |
| isalpha()      | Devuelve verdadero si todos los caracteres de la cadena están en el alfabeto          |
| isidentifier() | Devuelve verdadero si la cadena es un identificador valido                            |
| islower()      | Devuelve verdadero si todos los caracteres de la cadena están en minúscula            |
| isupper()      | Devuelve verdadero si todos los caracteres de la cadena están en mayusculas           |
| isspace()      | Devuelve verdadero si todos los caracteres de la cadena son espacios en blanco        |
| replace()      | Convierte un valor especificado en otro segun lo que se le indique                    |
| split()        | Divide la cadena segun el separador indicado y devuelve una lista                     |
| title()        | Convierte la primera letra de cada palabra en mayúscula                               |
| strip()        | Elimina los espacios en blanco al principio y al final de la cadena                   |

Si quieren investigar un poco mas sobre estos metodos: 
['String Methods'](https://www.w3schools.com/python/python_strings_methods.asp)

## Ejercicios

### Ejercicio 8 

Realizar un programa donde se reciba un **número entero** por teclado e imprima un mensaje diciendo si el número es *par o impar* y evaluar si es *positivo o negativo*.

**Output**
```shell
El número: X es par/impar y positivo/negativo
```
Donde **X** es el número ingresado por teclado.

### Ejercicio 9 (Tarea)

Una famosa cadena de cines en Venezuela te contrató para hacerles un programa de descuento basado en la *edad del cliente*, para ello tendrás que recibir por teclado la *edad* y *nombre* del cliente y verificar los siguientes casos:

    Si su edad es menor o igual a 4 años el precio de su entrada es gratis.
    Si su edad es menor o igual a 18 años el precio de su entrada es de $1.50.
    Si su edad es mayor o igual a los 60 años su entrada tendrá un valor de $1.00.
    La entrada para un adulto promedio es de $2.00.

Deberás imprimir un mensaje dependiendo de la edad del cliente para saber el precio de su entrada.

**Output**
```shell
El cliente: {nombre} tiene: {edad} años y su entrada de cine cuesta: ${precio_entrada}.
```

### Ejercicio 10

Te contrataron para realizar un programa que calcule el **premio** de un juego.

Los premios estan basados en puntos:

|  Puntos |     Premio    |
|:-------:|:-------------:|
| 1-50    | No hay premio |
| 51-150  | Bronce        |
| 151-180 | Plata         |
| 181-200 | Oro           |

Todos los límites inferiores y superiores son *inclusivos*, y los puntos solo pueden tomar *valores enteros positivos hasta 200*.

En su declaración *if*, asigne la variable resultado a una cadena que contenga el mensaje *apropiado* según el valor de los puntos.

Si ganaron un premio, el mensaje debería decir:

**Output**
```shell
 "¡Felicitaciones, ganaste la medalla de {nombre del premio} por haber tenido {puntos} pts!"
```
Si no hay premio, el mensaje debe decir:

**Output**
```
 "Ay, lo sentimos pero no hay premios para {puntos} pts."
```

### Ejercicio 14

Escribir un programa que pida al usuario un **número entero positivo** y muestre por pantalla *todos los números impares desde 1 hasta ese número separados por comas*.

### Ejercicio 15 (Tarea)

Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

**Nota**: La cuenta atras debe ser impresa en una sola linea.

### Ejercicio 16 (Tarea)

Escribir un programa que pida al usuario un **número entero positivo** y muestre por pantalla un triángulo rectángulo (como el que se indica a continuacion), que tenga de **altura** el número ingresado.

```shell
*
**
***
****
*****
```

### Ejercicio 17

Escribir un programa que pida al usuario un **número entero** y que muestre por pantalla si es un **número primo** o no.

**Nota:** Si el numero dado es negativo debe transformarlo en positivo.

### Ejercicio 18

Las palabras o números **palíndromos** son aquellas que *se leen igual de izquierda a derecha*. Por ejemplo: 101 es un número palíndromo, y 236 no lo es. Ana es una palabra palíndroma y pan no lo es.

Sabiendo esto, diseñe un programa que determine si un número o palabra ingresada por el usuario, es palíndroma o no.

### Ejercicio 19 (Tarea)

Escribir un programa que le pida al usuario una **frase** y una **letra**. Luego, muestre por pantalla el *número de veces que aparece la letra en la frase*.

### Ejercicio 21 (Tarea)

Realice un programa que dada una **lista** de nombres, pida al usuario introducir un **nombre** y *verificar si este está o no en la lista*.

### Ejercicio 23

Elabore un algoritmo que le pida al usuario un **número de partida** y un **número final**, para luego imprimir por pantalla los números de la **sucesión de Fibonacci** contenidos dentro de ese rango de números. Los numeros de la sucesion deben guardarse en una lista, y los numeros dentro del rango deben guardarse en otra lista. Luego, debe indicar por pantalla esta ultima lista de los numeros dentro del rango.

### Ejercicio 24 (Tarea)

Escribir un programa que almacene los vectores *(1,2,3)* y *(-1,0,2)* en dos listas y muestre por pantalla su **producto escalar**.

### Ejercicio 25 (Tarea)

Realizar un algoritmo que dado un número **N** cualquiera, busque todos los **numeros primos** menores a **N** y que los guarde en una **lista**. Luego, debe buscar en la lista *dos numeros primos cuya multiplicación de como resultado N*, en caso de no existir se le debe mostrar al usuario un mensaje de error.

### Ejercicio 26

Realice un algoritmo que realice las operaciones de **suma** y **resta** entre las siguientes **matrices**:

|   | Matriz | A |
|---|--------|---|
| 1 |   4    | 6 |
| 4 |   2    | 5 |
| 6 |   5    | 3 |

|     | Matriz |  B  |
|-----|--------|-----|
| 1.3 |   20   | 12  |
| 1.8 |   28   | 15  |
| 2.5 |   40   | 18  |

El programa debera imprimir *dos matrices resultantes*, una correspondiente a cada operación.

**Pista**: Una matriz puede ser modelada como una *lista de listas*. 

### Ejercicio 27 (Tarea)

Realice un algoritmo que dado un **número** ingresado por el usuario realice la operación de *multiplicación por la matriz A* del ejercicio anterior. El programa deberá
mostrar como respuesta la *matriz resultante* de la misma.


