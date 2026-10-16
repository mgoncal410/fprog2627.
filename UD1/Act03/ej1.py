# Ejercicio 1: Ficha personal
# Este programa esta hecho por Manuel González Calandria

nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu apellido: ")
edad = int(input("Introduce tu edad: "))
ciudad = input("Introduce tu ciudad: ")

print("=" * 30)
print("FICHA PERSONAL")
print("-" * 30)
print("Nombre:\t" + nombre + " " + apellido)
print("Edad:\t" + str(edad) + " años")
print("Ciudad:\t" + ciudad)
print("=" * 30)
print("El año que viene tendrás " + str(edad + 1) + " años.")