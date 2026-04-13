# 🐍 Noob → Pro en Python
### Tu hoja de ruta completa: desde cero absoluto hasta nivel senior

> **Cómo usar esta guía**
> Cada sección tiene teoría + ejercicio práctico. Hazlos en orden. Si pides ayuda, te guiaré con el **método socrático** — espera preguntas, no soluciones directas. El dolor de pensar es parte del proceso.

---

## ÍNDICE

### 🟢 NIVEL NOVATO
1. [Variables y Tipos de Datos](#1-variables-y-tipos-de-datos)
2. [Operadores](#2-operadores)
3. [Strings en profundidad](#3-strings-en-profundidad)
4. [Control de flujo: if / elif / else](#4-control-de-flujo-if--elif--else)
5. [Bucles: for y while](#5-bucles-for-y-while)
6. [Listas](#6-listas)
7. [Tuplas](#7-tuplas)
8. [Diccionarios](#8-diccionarios)
9. [Conjuntos (Sets)](#9-conjuntos-sets)
10. [Funciones básicas](#10-funciones-básicas)

### 🟡 NIVEL INTERMEDIO
11. [Funciones avanzadas: *args, **kwargs, closures](#11-funciones-avanzadas-args-kwargs-closures)
12. [Comprehensions](#12-comprehensions)
13. [Manejo de excepciones](#13-manejo-de-excepciones)
14. [Módulos y paquetes](#14-módulos-y-paquetes)
15. [Lectura y escritura de ficheros](#15-lectura-y-escritura-de-ficheros)
16. [Programación Orientada a Objetos (OOP)](#16-programación-orientada-a-objetos-oop)
17. [Herencia y Polimorfismo](#17-herencia-y-polimorfismo)
18. [Iteradores y Generadores](#18-iteradores-y-generadores)
19. [Decoradores](#19-decoradores)
20. [Context Managers](#20-context-managers)

### 🔴 NIVEL AVANZADO
21. [Programación Funcional](#21-programación-funcional)
22. [Metaclases y Descriptores](#22-metaclases-y-descriptores)
23. [Concurrencia: Threading y Multiprocessing](#23-concurrencia-threading-y-multiprocessing)
24. [Programación Asíncrona: asyncio](#24-programación-asíncrona-asyncio)
25. [Gestión de memoria e internals de CPython](#25-gestión-de-memoria-e-internals-de-cpython)
26. [Testing profesional: pytest](#26-testing-profesional-pytest)
27. [Type Hints y mypy](#27-type-hints-y-mypy)
28. [Protocolos y Abstract Base Classes](#28-protocolos-y-abstract-base-classes)
29. [Dataclasses y attrs](#29-dataclasses-y-attrs)
30. [Patrones de diseño en Python](#30-patrones-de-diseño-en-python)

### ⚫ NIVEL EXPERTO / PRO ABSOLUTO
31. [El Data Model de Python (Dunder Methods)](#31-el-data-model-de-python-dunder-methods)
32. [Extensiones en C y Cython](#32-extensiones-en-c-y-cython)
33. [Profiling y Optimización](#33-profiling-y-optimización)
34. [Packaging y distribución profesional](#34-packaging-y-distribución-profesional)
35. [Arquitectura y Clean Code en Python](#35-arquitectura-y-clean-code-en-python)

---

---

# 🟢 NIVEL NOVATO

---

## 1. Variables y Tipos de Datos

### Teoría

En Python, las variables son **referencias a objetos en memoria**. No necesitas declarar el tipo: Python lo infiere.

```python
# Tipos básicos
nombre = "Ada Lovelace"      # str
edad = 36                    # int
altura = 1.68                # float
es_programadora = True       # bool
sin_valor = None             # NoneType

# Ver el tipo de una variable
print(type(nombre))          # <class 'str'>
print(type(edad))            # <class 'int'>
```

**Todo en Python es un objeto.** Incluso un entero tiene métodos:
```python
x = -42
print(x.bit_length())   # 6 — número de bits necesarios para representarlo
print(abs(x))           # 42
```

**Conversión de tipos (casting):**
```python
numero_texto = "123"
numero = int(numero_texto)    # 123
precio = float("19.99")      # 19.99
booleano = bool(0)            # False — cualquier valor "vacío" es False
texto = str(42)               # "42"
```

**Valores falsy en Python:**
```python
# Estos evalúan a False en un contexto booleano:
False, None, 0, 0.0, "", [], {}, set(), ()
```

**Múltiple asignación:**
```python
a, b, c = 1, 2, 3
x = y = z = 0
a, b = b, a    # intercambio sin variable temporal ← idiomático en Python
```

---

### 🏋️ Ejercicio 1

Crea un programa que haga lo siguiente:

1. Define variables con tus datos personales: nombre, edad, ciudad, altura (en metros), y si tienes mascota (`True`/`False`).
2. Convierte tu edad a `float` y tu altura a `int`.
3. Imprime por pantalla una frase con todos los datos usando solo **una línea** de `print`.
4. Averigua: ¿qué devuelve `bool("")` y `bool("False")`? ¿Te sorprende el resultado? Explícalo en un comentario.

---

## 2. Operadores

### Teoría

**Aritméticos:**
```python
10 + 3    # 13   — suma
10 - 3    # 7    — resta
10 * 3    # 30   — multiplicación
10 / 3    # 3.333... — división (siempre devuelve float)
10 // 3   # 3    — división entera (floor division)
10 % 3    # 1    — módulo (resto)
10 ** 3   # 1000 — potencia
```

**Comparación:**
```python
==  !=  >  <  >=  <=
```
> ⚠️ `==` compara **valor**. `is` compara **identidad** (misma dirección de memoria).

```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True  — mismo valor
a is b   # False — son objetos distintos en memoria

# Excepción: Python "cachea" enteros pequeños (-5 a 256) y strings cortos
x = 256
y = 256
x is y   # True  — Python los reutiliza
```

**Lógicos:**
```python
and   # True si AMBOS son True
or    # True si AL MENOS UNO es True
not   # invierte el booleano
```

**Short-circuit evaluation:**
```python
# Python para de evaluar en cuanto conoce el resultado
True or error_que_lanzaria_excepcion()   # Devuelve True sin evaluar el lado derecho
False and error_que_lanzaria_excepcion() # Devuelve False sin evaluar el lado derecho
```

**Operadores de asignación aumentada:**
```python
x = 10
x += 5   # x = x + 5 → 15
x -= 3   # x = x - 3 → 12
x *= 2   # x = x * 2 → 24
x //= 5  # x = x // 5 → 4
x **= 3  # x = x ** 3 → 64
```

**Operador Walrus (`:=`) — Python 3.8+:**
```python
# Asigna y evalúa en una sola expresión
import random
if (n := random.randint(1, 100)) > 50:
    print(f"El número {n} es mayor que 50")
```

---

### 🏋️ Ejercicio 2

1. Escribe un programa que pida al usuario dos números (usa `input()` y conviértelos a `int`).
2. Muestra todos los resultados aritméticos: suma, resta, multiplicación, división, división entera, módulo y potencia.
3. Indica si el primer número es par o impar (pista: usa `%`).
4. Sin ejecutar el código, predice el resultado de `bool(0.0)`, `bool(-1)`, `bool([])`, `bool([0])`. Luego verifica.

---

## 3. Strings en Profundidad

### Teoría

Los strings son **secuencias inmutables** de caracteres Unicode.

**Creación:**
```python
s1 = "Hola"
s2 = 'Mundo'
s3 = """Texto
en varias
líneas"""
s4 = r"C:\nueva\ruta"   # raw string — ignora escapes
s5 = b"bytes"           # bytes, no str
```

**f-strings (Python 3.6+) — la forma moderna:**
```python
nombre = "Python"
version = 3.12
print(f"Hola, {nombre} {version}!")
print(f"El cuadrado de 7 es {7**2}")
print(f"Pi es {3.14159:.2f}")            # formateo: 2 decimales → 3.14
print(f"{'centrado':^20}")               # alineación centrada en 20 chars
print(f"{1_000_000:,}")                  # separador de miles → 1,000,000
```

**Métodos esenciales:**
```python
texto = "  Hola, Mundo!  "

texto.strip()           # "Hola, Mundo!"  — elimina espacios extremos
texto.upper()           # "  HOLA, MUNDO!  "
texto.lower()           # "  hola, mundo!  "
texto.replace("Mundo", "Python")
texto.split(",")        # ["  Hola", " Mundo!  "]
",".join(["a", "b", "c"])  # "a,b,c"
texto.startswith("  Hola")   # True
texto.find("Mundo")     # 7  (índice), -1 si no encuentra
"abc".count("a")        # 1
"  ".isspace()          # True
"123".isdigit()         # True
```

**Indexing y Slicing:**
```python
s = "Python"
s[0]      # "P"
s[-1]     # "n"
s[1:4]    # "yth"
s[::2]    # "Pto"  — cada 2 pasos
s[::-1]   # "nohtyP"  — invertir un string
```

**Strings son inmutables:**
```python
s = "Hola"
s[0] = "h"   # ❌ TypeError — no puedes modificar un string
s = "h" + s[1:]  # ✅ creas uno nuevo
```

---

### 🏋️ Ejercicio 3

1. Pide al usuario que introduzca una frase.
2. Muestra:
   - La frase en mayúsculas y en minúsculas.
   - El número de caracteres (incluyendo espacios) y el número de palabras.
   - La frase invertida.
   - Si la frase es un palíndromo (se lee igual al derecho que al revés, ignorando espacios y mayúsculas). Ejemplo: "Anita lava la tina".
3. Reemplaza todas las vocales por `*`.
4. Formatea la salida con f-strings para que quede limpia y legible.

---

## 4. Control de Flujo: if / elif / else

### Teoría

```python
edad = 20

if edad < 18:
    print("Menor de edad")
elif edad < 65:
    print("Adulto")
else:
    print("Tercera edad")
```

**Expresión ternaria (operador condicional inline):**
```python
resultado = "par" if edad % 2 == 0 else "impar"
```

**match / case — Pattern Matching (Python 3.10+):**
```python
comando = "salir"

match comando:
    case "ayuda":
        print("Mostrando ayuda...")
    case "salir" | "exit" | "quit":
        print("Hasta luego!")
    case _:
        print(f"Comando desconocido: {comando}")
```

**Match con tipos y condiciones:**
```python
punto = (1, 0)

match punto:
    case (0, 0):
        print("Origen")
    case (x, 0):
        print(f"Eje X en {x}")
    case (0, y):
        print(f"Eje Y en {y}")
    case (x, y) if x == y:
        print(f"Diagonal en {x}")
    case (x, y):
        print(f"Punto ({x}, {y})")
```

---

### 🏋️ Ejercicio 4

Crea una calculadora de notas:

1. Pide al usuario una nota numérica entre 0 y 10.
2. Valida que la nota esté en el rango correcto; si no, muestra un error.
3. Usando `if/elif/else`, clasifica la nota:
   - 0-4: Suspenso
   - 5: Aprobado
   - 6-7: Bien
   - 8-9: Notable
   - 10: Sobresaliente / Matrícula de Honor
4. Reescribe la clasificación usando `match/case`.
5. **Bonus:** ¿Qué pasa si el usuario introduce `"ocho"` en vez de `8`? Contrólalo.

---

## 5. Bucles: for y while

### Teoría

**for — para iterar sobre secuencias:**
```python
frutas = ["manzana", "pera", "uva"]
for fruta in frutas:
    print(fruta)

# range()
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2): # 2, 4, 6, 8
    print(i)
```

**enumerate() — cuando necesitas índice + valor:**
```python
for i, fruta in enumerate(frutas, start=1):
    print(f"{i}. {fruta}")
```

**zip() — iterar varios iterables a la vez:**
```python
nombres = ["Ana", "Luis", "Eva"]
edades = [25, 30, 28]
for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")
```

**while:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
```

**Control de bucles:**
```python
for i in range(10):
    if i == 3:
        continue   # salta esta iteración
    if i == 7:
        break      # termina el bucle
    print(i)
else:
    # Se ejecuta si el bucle terminó SIN break
    print("Bucle completado sin interrupciones")
```

> 💡 El bloque `else` en bucles es una característica muy Python que pocos conocen.

---

### 🏋️ Ejercicio 5

1. Usa un bucle `while` para crear un juego de adivinar un número. El programa elige un número aleatorio del 1 al 100 (usa `import random; random.randint(1, 100)`). El usuario tiene **7 intentos**. En cada intento, di si el número secreto es mayor o menor.
2. Al terminar, indica cuántos intentos usó el usuario.
3. Usa el bloque `else` del `while` para distinguir entre "ganaste" y "perdiste".
4. Con un `for` y `range`, imprime la tabla de multiplicar del número secreto (del 1 al 10).

---

## 6. Listas

### Teoría

Las listas son **secuencias mutables y ordenadas**. Pueden contener cualquier tipo de objeto.

```python
mi_lista = [1, "dos", 3.0, True, None, [4, 5]]
```

**Operaciones fundamentales:**
```python
lista = [3, 1, 4, 1, 5, 9, 2, 6]

lista.append(7)        # añade al final
lista.insert(0, 0)     # inserta en posición
lista.extend([8, 9])   # añade múltiples elementos
lista.remove(1)        # elimina PRIMERA ocurrencia del valor
lista.pop()            # elimina y retorna el último elemento
lista.pop(0)           # elimina y retorna el elemento en índice 0
lista.sort()           # ordena in-place (modifica la lista)
lista.reverse()        # invierte in-place
sorted(lista)          # retorna nueva lista ordenada sin modificar la original
lista.index(5)         # índice de la primera ocurrencia de 5
lista.count(1)         # cuántas veces aparece 1
lista.copy()           # copia superficial
lista.clear()          # vacía la lista
```

**Slicing:**
```python
lista = [0, 1, 2, 3, 4, 5]
lista[1:4]     # [1, 2, 3]
lista[:3]      # [0, 1, 2]
lista[3:]      # [3, 4, 5]
lista[::2]     # [0, 2, 4]
lista[::-1]    # [5, 4, 3, 2, 1, 0]

# Modificar con slicing
lista[1:3] = [10, 20]   # reemplaza elementos
```

**Copia superficial vs profunda:**
```python
import copy

original = [[1, 2], [3, 4]]
superficial = original.copy()       # o original[:]
profunda = copy.deepcopy(original)

original[0][0] = 99
print(superficial[0][0])  # 99 — ¡comparte la sublista!
print(profunda[0][0])     # 1  — independiente
```

---

### 🏋️ Ejercicio 6

1. Crea una lista con los nombres de 5 compañeros.
2. Añade 2 más al final y 1 al principio.
3. Ordena la lista alfabéticamente y muéstrala.
4. Elimina al que esté en la posición central.
5. Comprueba si un nombre específico está en la lista usando `in`.
6. **Desafío:** Dada la lista `[1, [2, 3], [4, [5, 6]]]`, aplana completamente la lista (sin usar bibliotecas, con un bucle). Resultado esperado: `[1, 2, 3, 4, 5, 6]`.

---

## 7. Tuplas

### Teoría

Las tuplas son **secuencias inmutables**. Una vez creadas, no se pueden modificar.

```python
coordenadas = (40.4168, -3.7038)   # Madrid
punto = 1, 2, 3                    # los paréntesis son opcionales
solo_uno = (42,)                   # ⚠️ coma obligatoria para tupla de 1 elemento
vacia = ()

# Unpacking
x, y = coordenadas
a, b, *resto = (1, 2, 3, 4, 5)   # a=1, b=2, resto=[3,4,5]
_, segundo, *_ = (10, 20, 30, 40) # solo nos interesa el segundo
```

**¿Cuándo usar tuplas vs listas?**
- **Tupla:** datos que no deben cambiar (coordenadas, RGB, fechas, retorno de funciones), pueden usarse como claves de diccionario.
- **Lista:** colecciones que se modifican.

```python
# Las tuplas son hashables si sus elementos lo son
d = {(0, 0): "origen", (1, 0): "derecha"}  # ✅
d = {[0, 0]: "origen"}                      # ❌ lista no es hashable
```

**Named tuples — tuplas con nombres de campo:**
```python
from collections import namedtuple

Punto = namedtuple("Punto", ["x", "y"])
p = Punto(3, 4)
print(p.x, p.y)     # 3 4
print(p[0], p[1])   # 3 4 — también funciona como tupla normal
```

---

### 🏋️ Ejercicio 7

1. Crea una tupla con las 5 capitales de los países que más te gusten y sus países.
2. Usa unpacking para extraer la primera y la última capital.
3. Usa `namedtuple` para representar una carta de una baraja (palo y número). Crea 3 cartas y almacénalas en una lista.
4. Intenta modificar un elemento de la tupla. ¿Qué error obtienes y por qué?

---

## 8. Diccionarios

### Teoría

Los diccionarios son colecciones de pares **clave → valor**. Son **mutables**, **ordenados** (desde Python 3.7) y **no permiten claves duplicadas**.

```python
persona = {
    "nombre": "Ada",
    "edad": 36,
    "lenguajes": ["Python", "C++"]
}

# Acceso
persona["nombre"]              # "Ada"
persona.get("email", "N/A")    # "N/A" — no lanza KeyError

# Modificar
persona["edad"] = 37
persona["email"] = "ada@example.com"

# Eliminar
del persona["email"]
persona.pop("edad")            # elimina y retorna el valor

# Iterar
for clave in persona:           # itera claves
    print(clave)

for clave, valor in persona.items():
    print(f"{clave}: {valor}")

persona.keys()     # dict_keys
persona.values()   # dict_values
persona.items()    # dict_items
```

**Métodos útiles:**
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}

d1.update(d2)               # fusiona d2 en d1
merged = {**d1, **d2}       # merge con desempaquetado (Python 3.5+)
merged = d1 | d2            # merge con operador | (Python 3.9+)

d1.setdefault("z", 0)       # inserta "z": 0 solo si "z" no existe

from collections import defaultdict
dd = defaultdict(list)      # valor por defecto es una lista vacía
dd["nueva_clave"].append(1) # no lanza KeyError
```

**Dict comprehension:**
```python
cuadrados = {x: x**2 for x in range(1, 6)}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### 🏋️ Ejercicio 8

1. Crea un diccionario que represente el inventario de una tienda: `{"manzana": 50, "pera": 30, "uva": 80}`.
2. Añade 3 productos más.
3. Actualiza la cantidad de manzanas a 45.
4. Escribe una función que reciba el inventario y devuelva el producto con mayor stock.
5. **Desafío:** Dado un texto (string largo), cuenta la frecuencia de cada palabra. Muestra las 5 palabras más frecuentes. (Pista: `str.split()` y `dict` o `collections.Counter`).

---

## 9. Conjuntos (Sets)

### Teoría

Los sets son **colecciones desordenadas de elementos únicos y hashables**.

```python
numeros = {1, 2, 3, 3, 2}   # {1, 2, 3} — duplicados eliminados
vacio = set()                # ⚠️ {} crea un dict, NO un set

# Operaciones de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b      # unión: {1, 2, 3, 4, 5, 6}
a & b      # intersección: {3, 4}
a - b      # diferencia: {1, 2}
a ^ b      # diferencia simétrica: {1, 2, 5, 6}
a <= b     # ¿a es subconjunto de b?

# Mutación
a.add(5)
a.discard(10)    # elimina si existe, sin error
a.remove(10)     # lanza KeyError si no existe
```

**frozenset — set inmutable (hashable):**
```python
fs = frozenset([1, 2, 3])
# Puede usarse como clave de diccionario o elemento de otro set
```

**Caso de uso típico — eliminar duplicados preservando orden (Python 3.7+):**
```python
lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sin_duplicados = list(dict.fromkeys(lista))  # [3, 1, 4, 5, 9, 2, 6]
```

---

### 🏋️ Ejercicio 9

1. Tienes dos listas de estudiantes: los que aprobaron matemáticas y los que aprobaron lengua. Conviértelas a sets.
2. Encuentra: quién aprobó ambas, quién aprobó solo matemáticas, quién aprobó solo lengua, y quién aprobó al menos una.
3. Crea una función que reciba una lista y devuelva `True` si tiene duplicados.
4. **Desafío:** Dado un string, devuelve `True` si es un anagrama de otro (mismas letras, diferente orden). Usa sets y algo más para contemplar las frecuencias.

---

## 10. Funciones Básicas

### Teoría

```python
def saludar(nombre, saludo="Hola"):
    """
    Docstring: describe qué hace la función.
    
    Args:
        nombre: El nombre a saludar.
        saludo: El tipo de saludo (por defecto "Hola").
    
    Returns:
        Un string con el saludo.
    """
    return f"{saludo}, {nombre}!"

print(saludar("Ana"))            # "Hola, Ana!"
print(saludar("Luis", "Buenos días"))   # "Buenos días, Luis!"
print(saludar(saludo="Hey", nombre="Eva"))  # argumentos por nombre
```

**Scope — LEGB rule:**
```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)    # "local"
    
    inner()
    print(x)        # "enclosing"

outer()
print(x)            # "global"
```

**Funciones como objetos de primera clase:**
```python
def doble(x):
    return x * 2

mi_funcion = doble           # referencia a la función
mi_funcion(5)                # 10

funciones = [doble, abs, str]  # lista de funciones
for f in funciones:
    print(f(-3))
```

**Lambda — funciones anónimas:**
```python
cuadrado = lambda x: x ** 2
suma = lambda a, b: a + b

# Uso típico: como argumento
nums = [3, 1, 4, 1, 5, 9]
nums.sort(key=lambda x: -x)   # orden descendente
```

---

### 🏋️ Ejercicio 10

1. Escribe una función `es_primo(n)` que devuelva `True` si `n` es primo.
2. Usa esa función para generar una lista de todos los primos menores de 100.
3. Escribe una función `fibonacci(n)` que devuelva los primeros `n` números de Fibonacci.
4. **Desafío:** Escribe una función `memoize(f)` que reciba una función y devuelva una versión de ella que recuerde resultados anteriores (caché manual). Pruébala con `fibonacci`.

---

---

# 🟡 NIVEL INTERMEDIO

---

## 11. Funciones Avanzadas: *args, **kwargs, closures

### Teoría

**`*args` — argumentos posicionales variables:**
```python
def sumar(*args):
    return sum(args)

sumar(1, 2, 3)       # 6
sumar(1, 2, 3, 4, 5) # 15
```

**`**kwargs` — argumentos nominales variables:**
```python
def perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

perfil(nombre="Ana", edad=30, ciudad="Madrid")
```

**Combinados y orden obligatorio:**
```python
def funcion(pos1, pos2, *args, kwonly, **kwargs):
    pass
# pos1, pos2: posicionales obligatorios
# *args: posicionales extra
# kwonly: argumento que SOLO puede pasarse por nombre
# **kwargs: nominales extra
```

**Desempaquetado al llamar:**
```python
def suma(a, b, c):
    return a + b + c

nums = [1, 2, 3]
suma(*nums)          # desempaqueta lista como posicionales

config = {"a": 1, "b": 2, "c": 3}
suma(**config)       # desempaqueta dict como kwargs
```

**Closures — funciones que "recuerdan" su entorno:**
```python
def crear_multiplicador(factor):
    def multiplicar(x):
        return x * factor    # `factor` es capturado del scope externo
    return multiplicar

doble = crear_multiplicador(2)
triple = crear_multiplicador(3)

doble(10)    # 20
triple(10)   # 30
```

**`nonlocal` — modificar variable del scope externo:**
```python
def contador():
    cuenta = 0
    def incrementar():
        nonlocal cuenta
        cuenta += 1
        return cuenta
    return incrementar

c = contador()
c()    # 1
c()    # 2
c()    # 3
```

---

### 🏋️ Ejercicio 11

1. Escribe una función `estadisticas(*numeros)` que calcule y devuelva (como diccionario) la media, mediana, mínimo, máximo y desviación estándar de los números recibidos. Sin usar `statistics` ni `numpy`.
2. Escribe una función `logger(nivel="INFO", **datos)` que imprima un log con el nivel y todos los datos extra formateados.
3. Crea un closure `crear_acumulador(inicio=0)` que devuelva una función. Cada vez que la llames con un número, lo suma al acumulador interno y devuelve el total.

---

## 12. Comprehensions

### Teoría

Las comprehensions son una forma **Pythónica, legible y eficiente** de crear colecciones.

**List comprehension:**
```python
# Forma larga
cuadrados = []
for x in range(10):
    if x % 2 == 0:
        cuadrados.append(x**2)

# Comprehension
cuadrados = [x**2 for x in range(10) if x % 2 == 0]
```

**Dict comprehension:**
```python
inventario = {"manzana": 50, "pera": 30, "uva": 80}
caro = {k: v for k, v in inventario.items() if v > 40}
invertido = {v: k for k, v in inventario.items()}
```

**Set comprehension:**
```python
letras_unicas = {letra.lower() for letra in "Hola Mundo" if letra != " "}
```

**Generator expression (no crea lista en memoria):**
```python
suma = sum(x**2 for x in range(1_000_000))   # eficiente en memoria
```

**Comprehensions anidadas:**
```python
# Aplanar matriz
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [n for fila in matriz for n in fila]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transponer matriz
transpuesta = [[fila[i] for fila in matriz] for i in range(3)]
```

---

### 🏋️ Ejercicio 12

Resuelve todo usando comprehensions (sin bucles `for` explícitos):

1. Dado `range(1, 101)`, crea una lista con los números que sean divisibles por 3 o por 5, pero no por ambos.
2. Dado un texto, crea un diccionario `{palabra: longitud}` para palabras de más de 4 letras.
3. Crea una lista de todas las combinaciones posibles `(i, j)` donde `i` va de 1 a 4 y `j` de 1 a 4, excluyendo cuando `i == j`.
4. **Desafío:** Implementa el **Criba de Eratóstenes** para obtener primos hasta N usando una sola comprehension (o las mínimas posibles).

---

## 13. Manejo de Excepciones

### Teoría

```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    print(f"Error de tipo o valor: {e}")
except Exception as e:
    print(f"Error inesperado: {type(e).__name__}: {e}")
else:
    # Se ejecuta si NO hubo excepción
    print(f"Resultado: {resultado}")
finally:
    # Se ejecuta SIEMPRE
    print("Bloque finally ejecutado")
```

**Jerarquía de excepciones:**
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── AttributeError
    ├── IndexError
    ├── KeyError
    ├── FileNotFoundError
    ├── OSError
    ├── RuntimeError
    └── ...
```

**Crear excepciones personalizadas:**
```python
class EdadInvalidaError(ValueError):
    """Excepción lanzada cuando la edad es inválida."""
    def __init__(self, edad, mensaje="La edad debe ser entre 0 y 150"):
        self.edad = edad
        super().__init__(f"{mensaje}. Recibido: {edad}")

def validar_edad(edad):
    if not 0 <= edad <= 150:
        raise EdadInvalidaError(edad)
    return edad
```

**Re-lanzar excepciones:**
```python
try:
    operacion_riesgosa()
except Exception as e:
    log_error(e)
    raise   # re-lanza la misma excepción
```

**Exception chaining (Python 3):**
```python
try:
    datos = cargar_datos()
except FileNotFoundError as e:
    raise RuntimeError("No se pudo inicializar el sistema") from e
```

---

### 🏋️ Ejercicio 13

1. Escribe una función `dividir_seguro(a, b)` que maneje `ZeroDivisionError` y `TypeError`.
2. Crea una excepción personalizada `SaldoInsuficienteError` con atributos `saldo_actual` y `monto_solicitado`.
3. Implementa una clase `CuentaBancaria` con métodos `depositar(monto)` y `retirar(monto)` que use esa excepción.
4. **Desafío:** Escribe un decorador `reintentar(veces=3, excepciones=(Exception,))` que reintente la función hasta `veces` veces si lanza alguna de las excepciones especificadas.

---

## 14. Módulos y Paquetes

### Teoría

**Módulo** = un archivo `.py`.
**Paquete** = un directorio con `__init__.py`.

```python
# Importar todo el módulo
import math
math.sqrt(16)

# Importar nombres específicos
from math import sqrt, pi
sqrt(16)

# Alias
import numpy as np
from datetime import datetime as dt

# Importar todo (evitar en producción)
from math import *
```

**Estructura de un paquete:**
```
mi_proyecto/
├── __init__.py
├── modulo_a.py
├── modulo_b.py
└── subpaquete/
    ├── __init__.py
    └── modulo_c.py
```

**`__init__.py`** controla qué se expone del paquete:
```python
# mi_proyecto/__init__.py
from .modulo_a import ClaseA
from .modulo_b import funcion_b

__all__ = ["ClaseA", "funcion_b"]  # lo que se exporta con `import *`
```

**`if __name__ == "__main__"`:**
```python
# El código aquí solo se ejecuta si el archivo es el punto de entrada
# No cuando es importado como módulo
if __name__ == "__main__":
    main()
```

**Módulos estándar esenciales:**
```python
import os           # operaciones del sistema
import sys          # información del intérprete
import pathlib      # manejo de rutas (moderno)
import json         # serialización JSON
import datetime     # fechas y tiempos
import collections  # estructuras de datos avanzadas
import itertools    # iteradores
import functools    # herramientas para funciones
import re           # expresiones regulares
import random       # aleatoriedad
import time         # tiempos y pausas
import logging      # sistema de logs
```

---

### 🏋️ Ejercicio 14

1. Crea un paquete `calculadora/` con módulos `basica.py` (suma, resta, multiplicación, división) y `avanzada.py` (potencia, raíz, logaritmo).
2. En `__init__.py`, importa todo para que el usuario pueda hacer `from calculadora import suma, potencia`.
3. Añade un módulo `historial.py` que guarde en una lista las últimas 10 operaciones realizadas.
4. Crea un `main.py` que use el paquete con el bloque `if __name__ == "__main__"`.

---

## 15. Lectura y Escritura de Ficheros

### Teoría

```python
# Escritura
with open("archivo.txt", "w", encoding="utf-8") as f:
    f.write("Primera línea\n")
    f.writelines(["Segunda\n", "Tercera\n"])

# Lectura
with open("archivo.txt", "r", encoding="utf-8") as f:
    contenido = f.read()           # todo el archivo como string
    # f.readline()                 # una línea
    # f.readlines()                # lista de líneas
    # for linea in f:              # iterar línea a línea (eficiente)

# Modos: "r" leer, "w" escribir (sobreescribe), "a" añadir, "x" crear (error si existe)
# "rb", "wb" para binario
```

**Pathlib — la forma moderna de manejar rutas:**
```python
from pathlib import Path

ruta = Path("datos") / "archivo.txt"   # construye rutas cross-platform
ruta.exists()
ruta.is_file()
ruta.suffix       # ".txt"
ruta.stem         # "archivo"
ruta.parent       # Path("datos")

ruta.write_text("contenido", encoding="utf-8")
texto = ruta.read_text(encoding="utf-8")

for p in Path(".").glob("**/*.py"):    # buscar recursivamente
    print(p)
```

**JSON:**
```python
import json

data = {"nombre": "Ana", "edad": 30, "lenguajes": ["Python", "Go"]}

# Serializar (Python → JSON string)
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Deserializar (JSON string → Python)
data2 = json.loads(json_str)

# Con ficheros
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

with open("data.json") as f:
    data3 = json.load(f)
```

---

### 🏋️ Ejercicio 15

1. Escribe un programa que lea un archivo de texto, cuente las líneas, palabras y caracteres, y guarde las estadísticas en un archivo JSON.
2. Implementa una agenda de contactos simple que guarde y cargue los datos desde un JSON.
3. **Desafío:** Implementa un sistema de logs que escriba en un archivo con timestamp, nivel (INFO/WARN/ERROR) y mensaje. Usa `logging` de la biblioteca estándar con un `FileHandler` y un `StreamHandler` simultáneos.

---

## 16. Programación Orientada a Objetos (OOP)

### Teoría

```python
class Vehiculo:
    # Atributo de clase (compartido por todas las instancias)
    ruedas = 4
    
    def __init__(self, marca, modelo, año):
        # Atributos de instancia
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self._velocidad = 0      # convenio: "privado" (no forzado)
        self.__serial = "XYZ"    # name mangling: _Vehiculo__serial
    
    def acelerar(self, incremento):
        """Método de instancia."""
        self._velocidad += incremento
    
    @property
    def velocidad(self):
        """Getter: accede como atributo."""
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self, valor):
        if valor < 0:
            raise ValueError("La velocidad no puede ser negativa")
        self._velocidad = valor
    
    @classmethod
    def desde_cadena(cls, cadena):
        """Constructor alternativo: método de clase."""
        marca, modelo, año = cadena.split(",")
        return cls(marca, modelo, int(año))
    
    @staticmethod
    def es_año_valido(año):
        """Método estático: no necesita self ni cls."""
        return 1886 <= año <= 2030
    
    def __repr__(self):
        return f"Vehiculo(marca={self.marca!r}, modelo={self.modelo!r})"
    
    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
    
    def __eq__(self, other):
        if not isinstance(other, Vehiculo):
            return NotImplemented
        return self.marca == other.marca and self.modelo == other.modelo


v = Vehiculo("Toyota", "Corolla", 2020)
print(v)           # Toyota Corolla (2020)
print(repr(v))     # Vehiculo(marca='Toyota', modelo='Corolla')
v.velocidad = 90
print(v.velocidad) # 90

v2 = Vehiculo.desde_cadena("Honda,Civic,2021")
```

---

### 🏋️ Ejercicio 16

Diseña una clase `Fraccion` que represente fracciones matemáticas:

1. Atributos: `numerador` y `denominador`. Simplifica automáticamente en `__init__` usando `math.gcd`.
2. Valida que el denominador no sea cero.
3. Implementa: `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__eq__`, `__lt__`, `__repr__`, `__str__`.
4. Añade un `@classmethod desde_float(valor, precision=6)` que convierta un float a fracción.
5. **Bonus:** Haz que la clase sea iterable (devuelva numerador y denominador con `__iter__`).

---

## 17. Herencia y Polimorfismo

### Teoría

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        raise NotImplementedError("Subclases deben implementar hablar()")
    
    def __str__(self):
        return f"{type(self).__name__}({self.nombre})"


class Perro(Animal):
    def hablar(self):
        return "¡Guau!"
    
    def buscar(self, objeto):
        return f"{self.nombre} busca {objeto}"


class Gato(Animal):
    def hablar(self):
        return "¡Miau!"


class AnimalCantante(Animal):
    """Mixin — añade comportamiento sin ser una clase base principal."""
    def cantar(self):
        return f"{self.nombre} canta: {self.hablar()} 🎵"


class PerroCantante(AnimalCantante, Perro):
    pass


# MRO (Method Resolution Order)
print(PerroCantante.__mro__)
# PerroCantante → AnimalCantante → Perro → Animal → object

# super()
class Labrador(Perro):
    def __init__(self, nombre, color):
        super().__init__(nombre)   # llama a Perro.__init__
        self.color = color
    
    def hablar(self):
        return super().hablar() + " (amistoso)"


# Polimorfismo
animales = [Perro("Rex"), Gato("Misi"), Labrador("Buddy", "dorado")]
for a in animales:
    print(f"{a}: {a.hablar()}")   # cada uno usa su propia implementación
```

**`isinstance` y `issubclass`:**
```python
isinstance(Rex, Perro)     # True
isinstance(Rex, Animal)    # True
issubclass(Labrador, Perro) # True
```

---

### 🏋️ Ejercicio 17

Diseña un sistema de formas geométricas:

1. Clase base `Forma` con método abstracto `area()` y `perimetro()`, y un `__str__` que muestre nombre, área y perímetro.
2. Clases: `Circulo(radio)`, `Rectangulo(ancho, alto)`, `Triangulo(a, b, c)`.
3. Clase `Cuadrado(lado)` que herede de `Rectangulo`.
4. Función `figura_mayor(lista_formas)` que devuelva la forma con mayor área.
5. **Bonus:** Crea un mixin `Dibujable` con un método `dibujar()` que imprima la forma en ASCII art.

---

## 18. Iteradores y Generadores

### Teoría

**Protocolo iterador:**
```python
# Un iterable tiene __iter__()
# Un iterador tiene __iter__() Y __next__()

class Rango:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin
    
    def __iter__(self):
        return self   # el propio objeto es el iterador
    
    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

for n in Rango(1, 5):
    print(n)   # 1 2 3 4
```

**Generadores — la forma fácil de crear iteradores:**
```python
def fibonacci():
    a, b = 0, 1
    while True:       # generador infinito
        yield a
        a, b = b, a + b

gen = fibonacci()
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 1

# Tomar los primeros 10
from itertools import islice
list(islice(fibonacci(), 10))
```

**`yield from` — delegar en otro generador:**
```python
def aplanar(iterable):
    for elemento in iterable:
        if hasattr(elemento, '__iter__') and not isinstance(elemento, str):
            yield from aplanar(elemento)
        else:
            yield elemento

list(aplanar([1, [2, [3, 4]], 5]))   # [1, 2, 3, 4, 5]
```

**`send()` — comunicación bidireccional con generadores:**
```python
def acumulador():
    total = 0
    while True:
        valor = yield total
        if valor is None:
            break
        total += valor

gen = acumulador()
next(gen)          # inicializar
gen.send(10)       # 10
gen.send(20)       # 30
gen.send(5)        # 35
```

---

### 🏋️ Ejercicio 18

1. Implementa un generador `primos()` que genere primos indefinidamente.
2. Implementa un generador `ventana_deslizante(iterable, n)` que genere tuplas de `n` elementos consecutivos: `ventana_deslizante([1,2,3,4,5], 3)` → `(1,2,3), (2,3,4), (3,4,5)`.
3. Implementa un iterador de clase `ArbolBinario` que recorra el árbol en orden (in-order).
4. **Desafío:** Crea un pipeline de generadores: uno que lea líneas de un archivo, otro que las filtre, otro que las transforme. Compón los tres y procesa el resultado sin cargar el archivo en memoria.

---

## 19. Decoradores

### Teoría

Un decorador es una función que **envuelve a otra función** para modificar su comportamiento.

```python
import functools
import time

def temporizador(func):
    @functools.wraps(func)   # preserva __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"{func.__name__} tardó {fin - inicio:.4f}s")
        return resultado
    return wrapper

@temporizador
def operacion_lenta():
    time.sleep(0.1)
    return 42
```

**Decoradores con argumentos:**
```python
def repetir(veces):
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def saludar():
    print("Hola!")
```

**Decoradores apilados:**
```python
@decorador_a
@decorador_b
def mi_funcion():
    pass

# Equivale a:
mi_funcion = decorador_a(decorador_b(mi_funcion))
```

**Decoradores de clase:**
```python
def singleton(cls):
    instancias = {}
    @functools.wraps(cls)
    def obtener_instancia(*args, **kwargs):
        if cls not in instancias:
            instancias[cls] = cls(*args, **kwargs)
        return instancias[cls]
    return obtener_instancia

@singleton
class Config:
    def __init__(self):
        self.debug = False
```

---

### 🏋️ Ejercicio 19

1. Implementa un decorador `@cache` que memorice resultados (sin usar `functools.lru_cache`).
2. Implementa un decorador `@validar_tipos(**tipos)` que valide los tipos de los argumentos. Ejemplo: `@validar_tipos(x=int, y=float)`.
3. Implementa un decorador `@reintentar(max_intentos=3, espera=1.0)` que reintente la función si lanza una excepción.
4. **Desafío:** Implementa un decorador `@registro` que sea a la vez decorador de funciones y de clases: para funciones, loguea llamadas y resultados; para clases, loguea la creación de instancias.

---

## 20. Context Managers

### Teoría

Los context managers garantizan que los recursos se liberen correctamente.

```python
# Con clase
class GestorConexion:
    def __init__(self, host):
        self.host = host
        self.conexion = None
    
    def __enter__(self):
        print(f"Conectando a {self.host}...")
        self.conexion = {"host": self.host, "activa": True}
        return self.conexion
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Cerrando conexión...")
        self.conexion["activa"] = False
        # Retornar True suprime la excepción
        return False   # propagamos cualquier excepción

with GestorConexion("localhost") as conn:
    print(conn)
```

**Con `contextlib.contextmanager`:**
```python
from contextlib import contextmanager

@contextmanager
def tempfile_manager(sufijo=".tmp"):
    import tempfile, os
    fd, ruta = tempfile.mkstemp(suffix=sufijo)
    try:
        yield ruta           # punto del `as`
    finally:
        os.close(fd)
        os.unlink(ruta)      # limpieza garantizada

with tempfile_manager(".txt") as ruta:
    with open(ruta, "w") as f:
        f.write("datos temporales")
```

**`contextlib.suppress` — ignorar excepciones específicas:**
```python
from contextlib import suppress

with suppress(FileNotFoundError):
    os.remove("archivo_que_puede_no_existir.txt")
```

**`contextlib.ExitStack` — contextos dinámicos:**
```python
from contextlib import ExitStack

archivos = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as stack:
    manejadores = [stack.enter_context(open(f)) for f in archivos]
    # Todos se cierran al salir, aunque fallen
```

---

### 🏋️ Ejercicio 20

1. Implementa un context manager `Temporizador` (clase) que mida el tiempo de ejecución del bloque `with` e imprima los ms transcurridos al salir.
2. Con `@contextmanager`, implementa `directorio_temporal()` que cree un directorio temporal, haga `yield` de la ruta, y lo elimine al salir.
3. **Desafío:** Implementa `transaccion_bd(conexion)`, un context manager que haga `BEGIN` al entrar, `COMMIT` si el bloque termina bien, y `ROLLBACK` si lanza una excepción.

---

---

# 🔴 NIVEL AVANZADO

---

## 21. Programación Funcional

### Teoría

Python soporta programación funcional con herramientas de `functools` e `itertools`.

```python
from functools import reduce, partial, lru_cache
import itertools

# map, filter, reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
suma_total = reduce(lambda a, b: a + b, numeros)

# lru_cache — memoización estándar
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

# partial — aplicación parcial de funciones
def potencia(base, exponente):
    return base ** exponente

cuadrado = partial(potencia, exponente=2)
cubo = partial(potencia, exponente=3)

# itertools — arsenal de iteradores
list(itertools.chain([1,2], [3,4], [5,6]))        # [1,2,3,4,5,6]
list(itertools.product("AB", repeat=2))            # AA, AB, BA, BB
list(itertools.combinations([1,2,3], 2))           # (1,2),(1,3),(2,3)
list(itertools.permutations([1,2,3], 2))           # (1,2),(1,3),(2,1)...
list(itertools.groupby([1,1,2,2,3], key=lambda x: x))
list(itertools.accumulate([1,2,3,4,5]))            # [1,3,6,10,15]
list(itertools.takewhile(lambda x: x < 5, numeros))
list(itertools.dropwhile(lambda x: x < 5, numeros))
```

**Composición de funciones:**
```python
def componer(*funciones):
    def aplicar(x):
        for f in reversed(funciones):
            x = f(x)
        return x
    return aplicar

pipeline = componer(str, abs, lambda x: x - 10)
pipeline(3)   # str(abs(3 - 10)) = "7"
```

---

### 🏋️ Ejercicio 21

1. Usando solo `map`, `filter`, `reduce` y `lambda` (sin bucles), calcula la suma de los cuadrados de los números impares del 1 al 50.
2. Usa `itertools.groupby` para agrupar una lista de palabras por su primera letra.
3. Implementa `componer(*funciones)` y úsala para crear un pipeline que: normalice un string, elimine puntuación, tokenice en palabras, y cuente la frecuencia.
4. **Desafío:** Implementa un `lru_cache` propio usando solo closures y un diccionario `OrderedDict`.

---

## 22. Metaclases y Descriptores

### Teoría

**Descriptores — controlan el acceso a atributos:**
```python
class TipadoDescriptor:
    def __init__(self, tipo):
        self.tipo = tipo
        self.nombre = None
    
    def __set_name__(self, owner, name):
        self.nombre = name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.nombre)
    
    def __set__(self, obj, valor):
        if not isinstance(valor, self.tipo):
            raise TypeError(
                f"{self.nombre} debe ser {self.tipo.__name__}, "
                f"recibido {type(valor).__name__}"
            )
        obj.__dict__[self.nombre] = valor


class Persona:
    nombre = TipadoDescriptor(str)
    edad = TipadoDescriptor(int)
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ana", 30)
p.edad = "treinta"   # ❌ TypeError
```

**Metaclases — la clase de una clase:**
```python
# type es la metaclase por defecto
# type(nombre, bases, namespace)
MiClase = type("MiClase", (object,), {"saludo": lambda self: "Hola"})

# Metaclase personalizada
class Singleton(type):
    _instancias = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]


class Config(metaclass=Singleton):
    def __init__(self):
        self.debug = False

a = Config()
b = Config()
assert a is b   # True — misma instancia
```

**`__init_subclass__` — registrar subclases automáticamente:**
```python
class Plugin:
    _registro = {}
    
    def __init_subclass__(cls, nombre=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if nombre:
            Plugin._registro[nombre] = cls

class PluginA(Plugin, nombre="a"):
    pass

class PluginB(Plugin, nombre="b"):
    pass

print(Plugin._registro)   # {"a": PluginA, "b": PluginB}
```

---

### 🏋️ Ejercicio 22

1. Implementa un descriptor `Validado` que acepte una función de validación como argumento: `edad = Validado(int, lambda x: 0 <= x <= 150)`.
2. Crea una metaclase `ABCEstricto` que lance `TypeError` si se instancia una clase que tenga métodos abstractos sin implementar.
3. **Desafío:** Implementa una metaclase `Auditado` que registre automáticamente cada llamada a cada método de la clase, con timestamp y argumentos.

---

## 23. Concurrencia: Threading y Multiprocessing

### Teoría

**El GIL (Global Interpreter Lock):**
CPython permite un solo hilo ejecutando bytecode a la vez. Por esto:
- **Threading** → útil para I/O-bound (esperas de red, disco)
- **Multiprocessing** → útil para CPU-bound (cálculos intensivos)

```python
import threading
import time

def tarea(nombre, segundos):
    print(f"[{nombre}] Iniciando...")
    time.sleep(segundos)
    print(f"[{nombre}] Terminado")

# Threads
hilo1 = threading.Thread(target=tarea, args=("A", 2))
hilo2 = threading.Thread(target=tarea, args=("B", 1))
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

# Thread-safe con Lock
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100_000):
        with lock:
            contador += 1

# Multiprocessing — procesos reales
from multiprocessing import Pool

def calcular(n):
    return sum(i * i for i in range(n))

with Pool() as pool:
    resultados = pool.map(calcular, [10**6, 10**6, 10**6, 10**6])

# concurrent.futures — interfaz unificada (recomendado)
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    futuros = [executor.submit(tarea, f"T{i}", 1) for i in range(4)]
    resultados = [f.result() for f in futuros]
```

---

### 🏋️ Ejercicio 23

1. Descarga concurrentemente 5 URLs (puedes simularlas con `time.sleep`) usando `ThreadPoolExecutor`. Mide el tiempo vs secuencial.
2. Calcula los primeros 10 números de la secuencia de Collatz de forma paralela con `ProcessPoolExecutor`.
3. **Desafío:** Implementa un `Pool` de workers propio usando `threading.Thread` y `queue.Queue`, con soporte para cancelación.

---

## 24. Programación Asíncrona: asyncio

### Teoría

`asyncio` permite concurrencia cooperativa en un solo hilo mediante el event loop.

```python
import asyncio
import aiohttp   # pip install aiohttp

async def fetch(session, url):
    async with session.get(url) as respuesta:
        return await respuesta.text()

async def main():
    urls = [
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
        "https://httpbin.org/delay/1",
    ]
    async with aiohttp.ClientSession() as session:
        tareas = [fetch(session, url) for url in urls]
        resultados = await asyncio.gather(*tareas)
    return resultados

asyncio.run(main())
```

**Conceptos clave:**
```python
# coroutine — función async def
async def mi_coroutine():
    await asyncio.sleep(1)   # await suspende y devuelve control al event loop
    return 42

# Task — coroutine ejecutándose concurrentemente
task = asyncio.create_task(mi_coroutine())

# gather — ejecutar múltiples coroutines concurrentemente
resultados = await asyncio.gather(coro1(), coro2(), coro3())

# timeout
try:
    resultado = await asyncio.wait_for(operacion_lenta(), timeout=5.0)
except asyncio.TimeoutError:
    print("Tiempo agotado")

# asyncio.Queue para productor/consumidor
queue = asyncio.Queue()

async def productor():
    for i in range(10):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumidor():
    while True:
        item = await queue.get()
        print(f"Procesando {item}")
        queue.task_done()
```

---

### 🏋️ Ejercicio 24

1. Implementa un scraper asíncrono que descargue 10 páginas concurrentemente (simula con `asyncio.sleep` de duración variable).
2. Implementa el patrón productor/consumidor con `asyncio.Queue`: el productor genera 20 tareas numéricas, y hay 3 consumidores que las procesan.
3. **Desafío:** Implementa un servidor TCP echo asíncrono usando `asyncio.start_server` que maneje múltiples conexiones simultáneas.

---

## 25. Gestión de Memoria e Internals de CPython

### Teoría

**Conteo de referencias:**
```python
import sys

x = [1, 2, 3]
print(sys.getrefcount(x))   # al menos 2 (x + argumento de getrefcount)

y = x                        # +1 referencia
del y                        # -1 referencia
```

**Garbage collector para ciclos:**
```python
import gc

# Crear ciclo de referencias
a = []
b = [a]
a.append(b)

del a, b
gc.collect()   # fuerza recolección de ciclos
```

**`__slots__` — reducir uso de memoria:**
```python
class PuntoNormal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Cada instancia tiene __dict__ → overhead de ~200 bytes

class PuntoSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # Sin __dict__ → ahorro de ~40-60% en instancias masivas

import sys
p1 = PuntoNormal(1, 2)
p2 = PuntoSlots(1, 2)
print(sys.getsizeof(p1))    # mayor
print(sys.getsizeof(p2))    # menor
```

**Interning y caché de objetos:**
```python
# CPython cachea enteros de -5 a 256
a, b = 256, 256
a is b   # True
a, b = 257, 257
a is b   # False (puede variar)

# String interning
s1 = sys.intern("hola mundo")
s2 = sys.intern("hola mundo")
s1 is s2   # True
```

**Profiling de memoria:**
```python
# pip install memory_profiler
from memory_profiler import profile

@profile
def proceso_intensivo():
    datos = [i for i in range(10**6)]
    return sum(datos)
```

---

### 🏋️ Ejercicio 25

1. Crea una clase `Nodo` y construye un árbol que cree un ciclo de referencias. Verifica con `gc` que se recolecta correctamente.
2. Compara el uso de memoria entre 1.000.000 de instancias de una clase con y sin `__slots__`.
3. **Desafío:** Implementa un pool de objetos reutilizables (`ObjectPool`) que evite la creación constante de nuevos objetos en código crítico.

---

## 26. Testing Profesional: pytest

### Teoría

```python
# archivo: test_calculadora.py
import pytest
from calculadora import suma, dividir

# Test básico
def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0

# Test de excepciones
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)

# Parametrización
@pytest.mark.parametrize("a, b, esperado", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (100, -50, 50),
])
def test_suma_parametrizado(a, b, esperado):
    assert suma(a, b) == esperado

# Fixtures
@pytest.fixture
def datos_usuario():
    return {"nombre": "Ana", "edad": 30}

def test_nombre(datos_usuario):
    assert datos_usuario["nombre"] == "Ana"

# Fixtures con scope
@pytest.fixture(scope="module")
def conexion_bd():
    conn = crear_conexion()
    yield conn
    conn.close()

# Mocking
from unittest.mock import patch, MagicMock

def test_llamada_externa():
    with patch("modulo.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"data": 42}
        
        resultado = mi_funcion_que_usa_requests()
        assert resultado == 42
        mock_get.assert_called_once()
```

**Estructura recomendada:**
```
proyecto/
├── src/
│   └── mi_paquete/
├── tests/
│   ├── conftest.py      # fixtures compartidas
│   ├── unit/
│   └── integration/
├── pyproject.toml
└── pytest.ini
```

---

### 🏋️ Ejercicio 26

Para la clase `CuentaBancaria` del ejercicio 13:

1. Escribe tests para todos los casos: depósito normal, retiro exitoso, retiro con saldo insuficiente, depósito de monto negativo.
2. Usa `@pytest.mark.parametrize` para probar múltiples escenarios.
3. Crea un fixture `cuenta_con_saldo` que proporcione una cuenta con 1000€.
4. **Desafío:** Añade cobertura de código con `pytest-cov`. Alcanza 100% de cobertura en la clase.

---

## 27. Type Hints y mypy

### Teoría

Los type hints no cambian el comportamiento en runtime, pero permiten análisis estático y mejor documentación.

```python
from typing import Optional, Union, List, Dict, Tuple, Callable, Any
from typing import TypeVar, Generic, Protocol
from collections.abc import Sequence, Iterable, Iterator

# Básico
def saludar(nombre: str, veces: int = 1) -> str:
    return f"Hola, {nombre}! " * veces

# Colecciones (Python 3.9+: usar built-ins directamente)
def procesar(datos: list[int]) -> dict[str, float]:
    return {"media": sum(datos) / len(datos)}

# Optional — puede ser None
def buscar(nombre: str) -> Optional[int]:
    ...

# Union — varios tipos (Python 3.10+: usar |)
def parsear(valor: int | str) -> int:
    return int(valor)

# TypeVar — genéricos
T = TypeVar("T")

def primero(secuencia: list[T]) -> T:
    return secuencia[0]

# Callable
def aplicar(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

# Protocol — duck typing tipado
class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

def maximo(a: Comparable, b: Comparable) -> Comparable:
    return a if b < a else b

# Dataclass con tipos
from dataclasses import dataclass, field

@dataclass
class Punto:
    x: float
    y: float
    etiqueta: str = ""
    tags: list[str] = field(default_factory=list)
    
    def distancia(self, otro: "Punto") -> float:
        return ((self.x - otro.x)**2 + (self.y - otro.y)**2) ** 0.5
```

**Ejecutar mypy:**
```bash
mypy --strict mi_modulo.py
```

---

### 🏋️ Ejercicio 27

1. Anota completamente con tipos el sistema de formas del ejercicio 17.
2. Crea una clase genérica `Pila[T]` con métodos `push`, `pop`, `peek` y `esta_vacia`.
3. Define un `Protocol` llamado `Serializable` con métodos `to_dict` y `from_dict`.
4. **Desafío:** Pasa `mypy --strict` en un módulo de al menos 100 líneas sin errores.

---

## 28. Protocolos y Abstract Base Classes

### Teoría

```python
from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable

# ABC — herencia obligatoria
class Repositorio(ABC):
    @abstractmethod
    def guardar(self, entidad) -> None: ...
    
    @abstractmethod
    def buscar(self, id: int): ...
    
    @abstractmethod
    def eliminar(self, id: int) -> None: ...
    
    def existe(self, id: int) -> bool:
        """Método concreto que usa métodos abstractos."""
        return self.buscar(id) is not None


# Protocol — duck typing estructural (NO requiere herencia)
@runtime_checkable
class Dibujable(Protocol):
    def dibujar(self) -> None: ...
    def area(self) -> float: ...

class Circulo:
    # No hereda de Dibujable, pero implementa su interfaz
    def dibujar(self) -> None: print("⭕")
    def area(self) -> float: return 3.14 * self.radio ** 2

c = Circulo()
isinstance(c, Dibujable)   # True — gracias a @runtime_checkable

# ABCs de collections
from collections.abc import Mapping, MutableMapping, Sequence

class MiDict(MutableMapping):
    def __init__(self):
        self._data = {}
    
    def __getitem__(self, key): return self._data[key]
    def __setitem__(self, key, value): self._data[key] = value
    def __delitem__(self, key): del self._data[key]
    def __iter__(self): return iter(self._data)
    def __len__(self): return len(self._data)
    # get(), keys(), values(), items(), update(), pop() → ¡gratis por herencia!
```

---

### 🏋️ Ejercicio 28

1. Diseña un sistema de notificaciones: ABC `Notificador` con método abstracto `enviar(mensaje: str, destinatario: str)`. Implementa `NotificadorEmail` y `NotificadorSMS`.
2. Define un `Protocol` `Persistible` y asegúrate de que diferentes clases sin herencia común cumplan el protocolo.
3. **Desafío:** Implementa `MiOrdenado`, una clase que herede de `collections.abc.MutableSequence` implementando solo los métodos abstractos, y verifica que hereda `sort()`, `reverse()`, `index()` de forma gratuita.

---

## 29. Dataclasses y attrs

### Teoría

```python
from dataclasses import dataclass, field, KW_ONLY, InitVar
from typing import ClassVar

@dataclass(order=True, frozen=True)
class Punto:
    # frozen=True → inmutable (como NamedTuple pero con herencia)
    # order=True → genera __lt__, __le__, etc.
    x: float
    y: float
    
    def distancia_origen(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5


@dataclass
class Empleado:
    nombre: str
    departamento: str
    _: KW_ONLY         # todo lo que sigue es keyword-only
    salario: float = 0.0
    tags: list[str] = field(default_factory=list)
    
    # Variable de clase (no es campo del dataclass)
    empresa: ClassVar[str] = "Acme Corp"
    
    # Campo que no va al __repr__ ni al __init__
    _cache: dict = field(default_factory=dict, repr=False, init=False)
    
    # Argumento de init que no se convierte en atributo
    verbose: InitVar[bool] = False
    
    def __post_init__(self, verbose: bool):
        if verbose:
            print(f"Creando empleado: {self.nombre}")
        self.nombre = self.nombre.strip().title()


# Heredar de dataclass
@dataclass
class Manager(Empleado):
    equipo: list[str] = field(default_factory=list)


# Serialización
from dataclasses import asdict, astuple, replace

e = Empleado("ana garcía", "Ingeniería", salario=60000)
asdict(e)       # {'nombre': 'Ana García', 'departamento': 'Ingeniería', ...}
e2 = replace(e, salario=70000)   # crea copia con campo modificado
```

---

### 🏋️ Ejercicio 29

1. Modela un sistema de pedidos con dataclasses: `Producto`, `LineaPedido` (producto + cantidad), `Pedido` (lista de líneas + cliente + fecha). El pedido debe calcular su total automáticamente en `__post_init__`.
2. Haz `Producto` inmutable (`frozen=True`) y orderable por precio.
3. **Desafío:** Implementa serialización y deserialización completa a JSON del sistema de pedidos, manejando tipos no serializables por defecto (como `datetime`).

---

## 30. Patrones de Diseño en Python

### Teoría

**Creacionales:**

```python
# Factory Method
class Animal:
    @staticmethod
    def crear(tipo: str) -> "Animal":
        clases = {"perro": Perro, "gato": Gato}
        if tipo not in clases:
            raise ValueError(f"Tipo desconocido: {tipo}")
        return clases[tipo]()

# Builder
class QueryBuilder:
    def __init__(self):
        self._tabla = ""
        self._condiciones = []
        self._limite = None
    
    def tabla(self, nombre: str) -> "QueryBuilder":
        self._tabla = nombre
        return self   # devuelve self para encadenamiento
    
    def donde(self, condicion: str) -> "QueryBuilder":
        self._condiciones.append(condicion)
        return self
    
    def limite(self, n: int) -> "QueryBuilder":
        self._limite = n
        return self
    
    def construir(self) -> str:
        sql = f"SELECT * FROM {self._tabla}"
        if self._condiciones:
            sql += " WHERE " + " AND ".join(self._condiciones)
        if self._limite:
            sql += f" LIMIT {self._limite}"
        return sql

query = (QueryBuilder()
         .tabla("usuarios")
         .donde("edad > 18")
         .donde("activo = 1")
         .limite(10)
         .construir())
```

**Estructurales:**

```python
# Decorator (patrón, no el decorador de Python)
class Cafe:
    def coste(self): return 1.0
    def descripcion(self): return "Café"

class ConLeche:
    def __init__(self, cafe): self._cafe = cafe
    def coste(self): return self._cafe.coste() + 0.5
    def descripcion(self): return self._cafe.descripcion() + " con leche"

# Observer
class Evento:
    def __init__(self):
        self._observadores: list = []
    
    def suscribir(self, observador):
        self._observadores.append(observador)
    
    def notificar(self, *args, **kwargs):
        for obs in self._observadores:
            obs(*args, **kwargs)

on_usuario_creado = Evento()
on_usuario_creado.suscribir(lambda u: print(f"Email de bienvenida a {u}"))
on_usuario_creado.suscribir(lambda u: print(f"Log: nuevo usuario {u}"))
on_usuario_creado.notificar("Ana")
```

---

### 🏋️ Ejercicio 30

1. Implementa el patrón **Strategy** para un sistema de ordenación: la clase `Ordenador` acepta diferentes estrategias (`BubbleSort`, `QuickSort`, `MergeSort`) intercambiables en runtime.
2. Implementa el patrón **Chain of Responsibility** para validar un formulario: cada validador en la cadena valida una cosa diferente y pasa al siguiente si pasa.
3. **Desafío:** Implementa el patrón **Command** con soporte de `undo/redo` para un editor de texto simple.

---

---

# ⚫ NIVEL EXPERTO / PRO ABSOLUTO

---

## 31. El Data Model de Python (Dunder Methods)

### Teoría

El data model define cómo los objetos interactúan con el lenguaje. Implementando dunders, tus clases se comportan como tipos nativos.

```python
class Vector:
    def __init__(self, *componentes):
        self._v = list(componentes)
    
    # Representación
    def __repr__(self): return f"Vector({', '.join(map(str, self._v))})"
    def __str__(self): return f"({', '.join(map(str, self._v))})"
    def __format__(self, spec): return format(str(self), spec)
    
    # Contenedor
    def __len__(self): return len(self._v)
    def __getitem__(self, idx): return self._v[idx]
    def __setitem__(self, idx, val): self._v[idx] = val
    def __contains__(self, val): return val in self._v
    def __iter__(self): return iter(self._v)
    
    # Aritmética
    def __add__(self, other): return Vector(*(a+b for a,b in zip(self._v, other._v)))
    def __radd__(self, other): return self.__add__(other)  # other + self
    def __iadd__(self, other): self._v = [a+b for a,b in zip(self._v, other._v)]; return self
    def __neg__(self): return Vector(*(-x for x in self._v))
    def __mul__(self, escalar): return Vector(*(x*escalar for x in self._v))
    def __rmul__(self, escalar): return self.__mul__(escalar)
    def __abs__(self): return sum(x**2 for x in self._v) ** 0.5
    
    # Comparación
    def __eq__(self, other): return self._v == other._v
    def __lt__(self, other): return abs(self) < abs(other)
    def __hash__(self): return hash(tuple(self._v))
    
    # Contexto booleano
    def __bool__(self): return any(self._v)
    
    # Callable
    def __call__(self, escalar): return self.__mul__(escalar)
    
    # Context manager
    def __enter__(self): return self
    def __exit__(self, *args): self._v = [0] * len(self._v)

v = Vector(1, 2, 3)
print(abs(v))         # módulo
print(v * 2)          # Vector(2, 4, 6)
print(2 * v)          # Vector(2, 4, 6) — __rmul__
print(v[1])           # 2
print(list(v))        # [1, 2, 3]
```

---

### 🏋️ Ejercicio 31

Implementa una clase `Matriz` completa:

1. Representación, indexado con `[i][j]` y con `[i, j]`.
2. Suma, resta, multiplicación de matrices (como `@` usando `__matmul__`).
3. Transposición con `~matriz` (usando `__invert__`).
4. Determinante y traza como propiedades.
5. Que sea iterable (filas) y que funcione con `len()`.
6. **Bonus:** Haz que `Matriz` sea un context manager que restaure su estado original si falla alguna operación.

---

## 32. Extensiones en C y Cython

### Teoría

Cuando Python no es suficientemente rápido, puedes escribir extensiones en C o usar Cython.

**ctypes — llamar a librerías C sin compilar:**
```python
import ctypes
import ctypes.util

# Cargar librería del sistema
libc = ctypes.CDLL(ctypes.util.find_library("c"))
libc.printf(b"Hola desde C!\n")

# Definir tipos
libc.strlen.argtypes = [ctypes.c_char_p]
libc.strlen.restype = ctypes.c_size_t
print(libc.strlen(b"Python"))   # 6
```

**cffi — más pythónico:**
```python
from cffi import FFI
ffi = FFI()

ffi.cdef("int suma(int a, int b);")
lib = ffi.verify("int suma(int a, int b) { return a + b; }")
print(lib.suma(3, 4))   # 7
```

**Cython — compilar Python a C:**
```python
# archivo: rapido.pyx
def suma_rapida(int n):
    cdef int i, total = 0
    for i in range(n):
        total += i
    return total
```

```bash
# setup.py
from setuptools import setup
from Cython.Build import cythonize
setup(ext_modules=cythonize("rapido.pyx"))

# Compilar
python setup.py build_ext --inplace
```

---

### 🏋️ Ejercicio 32

1. Usa `ctypes` para llamar a `qsort` de la librería C estándar y ordenar un array de enteros.
2. Escribe un módulo Cython simple que calcule el n-ésimo número de Fibonacci con tipado estático. Compáralo con la versión Python pura en velocidad.
3. **Desafío:** Envuelve con `ctypes` una librería matemática (como `libm`) y usa sus funciones trigonométricas directamente.

---

## 33. Profiling y Optimización

### Teoría

**Regla número 1: mide antes de optimizar.**

```python
# cProfile — profiling completo
import cProfile
import pstats

with cProfile.Profile() as pr:
    mi_funcion_lenta()

stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.CUMULATIVE)
stats.print_stats(10)   # top 10 funciones

# timeit — medir pequeños fragmentos
import timeit

resultado = timeit.timeit(
    "sorted(lista)",
    setup="lista = list(range(1000, 0, -1))",
    number=10000
)
print(f"{resultado:.3f}s para 10000 ejecuciones")

# line_profiler — profiling línea a línea
# pip install line_profiler
# @profile (se activa con kernprof -l -v script.py)

# memory_profiler — profiling de memoria
# pip install memory_profiler
# @profile
```

**Técnicas de optimización:**
```python
# 1. Usar estructuras adecuadas
# list → O(n) para búsqueda; set → O(1)
# deque para colas; array para datos numéricos homogéneos

# 2. Evitar atributos globales (costoso en lookup)
# 3. Operaciones in-place cuando sea posible
# 4. Usar builtins (implementados en C)
# 5. NumPy para operaciones vectoriales masivas
# 6. slots en clases con muchas instancias
# 7. Generadores en vez de listas cuando sea posible

# Ejemplo: suma de cuadrados
import numpy as np

n = 10_000_000
# Python puro: ~5s
resultado = sum(x*x for x in range(n))

# NumPy: ~0.05s (100x más rápido)
resultado = np.arange(n, dtype=np.int64)
resultado = (resultado ** 2).sum()
```

---

### 🏋️ Ejercicio 33

1. Toma la función `fibonacci` recursiva sin cache. Perfila con `cProfile`. Luego optimízala progresivamente: con `@lru_cache`, con iteración, con Cython. Compara tiempos.
2. Implementa la multiplicación de dos matrices de 500x500: en Python puro vs NumPy. Mide la diferencia.
3. **Desafío:** Usa `line_profiler` para encontrar el cuello de botella en una función que procese un CSV de 1M de filas y optimízala.

---

## 34. Packaging y Distribución Profesional

### Teoría

**Estructura moderna de proyecto:**
```
mi_proyecto/
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       └── modulo.py
├── tests/
├── docs/
├── pyproject.toml     ← configuración central (PEP 517/518)
├── README.md
├── LICENSE
└── .gitignore
```

**`pyproject.toml` (estándar moderno):**
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mi-paquete"
version = "1.0.0"
description = "Un paquete de ejemplo"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "pydantic>=2.0",
]

[project.optional-dependencies]
dev = ["pytest", "mypy", "black", "ruff"]

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.mypy]
strict = true

[tool.ruff]
line-length = 88
```

**Publicar en PyPI:**
```bash
python -m build         # genera dist/
twine upload dist/*     # sube a PyPI
```

**Entornos virtuales modernos:**
```bash
# uv — el gestor moderno (10-100x más rápido que pip)
uv venv
uv pip install -r requirements.txt
uv add requests            # añadir dependencia
uv run pytest              # ejecutar en el entorno
```

---

### 🏋️ Ejercicio 34

1. Empaqueta la calculadora del ejercicio 14 siguiendo la estructura moderna con `pyproject.toml`.
2. Configura `mypy`, `ruff` (linter) y `pytest` en el `pyproject.toml`.
3. Crea un `Makefile` o script de CI con comandos: `lint`, `test`, `build`, `docs`.
4. **Desafío:** Publica en `TestPyPI` (el entorno de pruebas de PyPI) e instala tu propio paquete con `pip install`.

---

## 35. Arquitectura y Clean Code en Python

### Teoría

**Principios SOLID en Python:**

```python
# S — Single Responsibility
# Una clase, una responsabilidad
class RepositorioUsuario:
    def guardar(self, usuario): ...
    def buscar(self, id): ...

class ServicioEmail:
    def enviar_bienvenida(self, usuario): ...

# O — Open/Closed
# Abierto a extensión, cerrado a modificación
class Exportador(Protocol):
    def exportar(self, datos: list) -> bytes: ...

class ExportadorCSV:
    def exportar(self, datos): ...

class ExportadorJSON:
    def exportar(self, datos): ...

# L — Liskov Substitution
# Las subclases deben poder usarse donde se usa la clase base

# I — Interface Segregation (Protocols pequeños y específicos)
class Readable(Protocol):
    def read(self) -> bytes: ...

class Writable(Protocol):
    def write(self, data: bytes) -> None: ...

# D — Dependency Inversion
# Depender de abstracciones, no de implementaciones concretas
class ServicioUsuario:
    def __init__(self, repo: RepositorioUsuario, emailer: ServicioEmail):
        self._repo = repo
        self._emailer = emailer
```

**Arquitectura hexagonal (Ports & Adapters):**
```
mi_app/
├── domain/          # Entidades, Value Objects, lógica de negocio PURA
│   ├── models.py
│   └── services.py
├── application/     # Casos de uso (orquestan el dominio)
│   └── use_cases.py
├── infrastructure/  # Adaptadores concretos (BD, APIs, etc.)
│   ├── repositories.py
│   └── external_apis.py
└── interfaces/      # Entradas (CLI, REST, WebSocket)
    └── api.py
```

---

### 🏋️ Ejercicio 35 — Proyecto Final

Construye un sistema de gestión de biblioteca siguiendo arquitectura hexagonal:

**Dominio:**
- Entidades: `Libro`, `Socio`, `Prestamo`
- Reglas: un socio no puede tener más de 3 préstamos activos, un libro no puede prestarse si está prestado

**Aplicación (casos de uso):**
- `PrestarLibro(libro_id, socio_id)`
- `DevolverLibro(prestamo_id)`
- `BuscarLibrosPorAutor(autor)`

**Infraestructura:**
- `RepositorioLibrosEnMemoria` y `RepositorioLibrosJSON`
- Intercambiables sin cambiar el dominio

**Interfaces:**
- CLI interactiva
- Tests completos con pytest (mocking del repositorio)

**Requisitos de calidad:**
- Type hints completos (mypy --strict pasa)
- Cobertura de tests > 90%
- Sin dependencias externas en el dominio
- Manejo de excepciones de dominio personalizadas

---

---

## 🎯 Checklist del Desarrollador Pro Python

Marca cada ítem cuando lo domines genuinamente:

### Fundamentos
- [ ] Variables, tipos, operadores
- [ ] Strings y f-strings
- [ ] Estructuras de control
- [ ] Listas, tuplas, dicts, sets con fluidez
- [ ] Funciones: scope, closures, lambdas

### Intermedio
- [ ] Comprehensions en todas sus formas
- [ ] OOP: herencia, polimorfismo, dunder methods
- [ ] Generadores e iteradores propios
- [ ] Decoradores con argumentos
- [ ] Context managers propios
- [ ] Manejo de excepciones profesional
- [ ] Testing con pytest y mocks

### Avanzado
- [ ] asyncio y programación concurrente
- [ ] Type hints y mypy --strict
- [ ] Descriptores y metaclases
- [ ] Dataclasses avanzadas
- [ ] Profiling y optimización
- [ ] El data model completo

### Pro
- [ ] Packaging y distribución en PyPI
- [ ] Arquitectura hexagonal
- [ ] Extensiones C / Cython
- [ ] SOLID y patrones de diseño idiomáticos
- [ ] Gestión de memoria y GIL

---

> **"Simple is better than complex. Complex is better than complicated."**
> — Tim Peters, *El Zen de Python* (`import this`)

---

*Guía creada para el camino Noob → Pro. Versión Python 3.12+*
