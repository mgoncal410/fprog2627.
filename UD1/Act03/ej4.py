# Ejercicio 4 - Dibujar un marco
# Este programa esta hecho por Manuel González Calandria

Caracter = input("Caracter para el borde: ")
Ancho = int(input("Ancho interior: "))
Alto = int(input("Alto interior: "))

print(Caracter + Caracter * Ancho + Caracter)

print((Caracter + " "*Ancho + Caracter +"\n") *Alto , end=(""))
print(Caracter + Caracter * Ancho + Caracter)