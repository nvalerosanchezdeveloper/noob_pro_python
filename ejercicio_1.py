# Ejercicio 1

# Crea un programa que haga lo siguiente:

# Define variables con tus datos personales: nombre, edad, ciudad, altura (en metros), y si tienes mascota (True/False).
# Convierte tu edad a float y tu altura a int.
# Imprime por pantalla una frase con todos los datos usando solo una línea de print.
# Averigua: ¿qué devuelve bool("") y bool("False")? ¿Te sorprende el resultado? Explícalo en un comentario.

name = "Nicolás"
age = 26
city = "Alcorcón"
height = 1.63
has_pet = True

age_cast_to_float = float(26)
height_cast_to_int = int(1.63)

print(f"Me llamo {name}, tengo {age_cast_to_float} años, soy de {city} (Madrid).Mido {height_cast_to_int}m. ¿Tengo mascotas? {has_pet}")

print(bool(""))       # False NOTA: Este boolean devuelve false porque está vacío, con lo cual, al decir que no tiene valores, el 1/0 está apagado.
print(bool("False"))  # True NOTA: Independientemente de si es true o false, el valor está encendido porque tiene valor, por eso da True.
