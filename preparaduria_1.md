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
    - [Ejercicio 2](#ejercicio-2)
    - [Ejercicio 3](#ejercicio-3)
    - [Ejercicio 4](#ejercicio-4)
    - [Ejercicio 5](#ejercicio-5)

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

### Ejercicio 2
Escribir un programa que le pida al usuario el *número de horas trabajadas*, y el *pago por hora*. Posteriormente, debe mostrar por pantalla la paga que le correspondria si el usuario fuera **100%** efectivo, pero como sabemos que la mitad del tiempo estuvo jugando *League of Legends*, tambien debe indicar cual seria su pago real si solo se le paga un **50%**.

**Output**
```shell
Numero de horas trabajadas: (número de horas trabajadas)
Pago por hora: (pago por hora)
¡Hola trabajador! Tu pago deberia ser (pago ideal)$, pero como no cumpliste con nuestras expectativas te daremos (pago real)$.
```

### Ejercicio 3
Escribir un programa que pida un numero positivo **n** al usuario, y después muestre por pantalla la *suma de todos los enteros desde 1 hasta **n***. Tenga en cuenta que los numeros decimales deben ser *de alguna forma* transformados a enteros.

**Output**
```shell
Numero: (n)
¡Hola usuario! La suma de todos los enteros desde 1 hasta (n) da como resultado (resultado).
```

### Ejercicio 4
Escribir un programa que pida al usuario su **peso** (en kg) y **estatura** (en metros), y que luego calcule el **índice de masa corporal** del usuario y que muestre por pantalla:

**Output**
```shell
Peso: (peso)kg
Estatura: (estatura)m
Tu índice de masa corporal es (índice de masa corporal).
```
El índice de masa corporal calculado debe ser redondeado a *dos decimales*.

### Ejercicio 5
Escribir un programa que le pida al usuario *dos números* y que imprima por pantalla:

**Output**
```shell
Numero 1: (numero 1)
Numero 2: (numero 2)
(numero1) entre (numero2) da un cociente (cociente) y un resto (resto).
```