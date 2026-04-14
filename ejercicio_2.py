# Ejercicio 2


# Escribe un programa que pida al usuario dos números (usa input() y conviértelos a int).
# Muestra todos los resultados aritméticos: suma, resta, multiplicación, división, división entera, módulo y potencia.
# Indica si el primer número es par o impar (pista: usa %).


number_1 = input("Introduzca el primer número: ")
number_2 = input("Introduzca el segundo número: ")

number_1_to_int = int(number_1)
number_2_to_int = int(number_2)

if number_1_to_int %2 == 0:
    print("El número es par")
else: print("El número es impar")

