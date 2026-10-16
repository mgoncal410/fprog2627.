# Ejercicio 2 - Calculadora de IVA
# Este programa esta hecho por Manuel González Calandria

sin_iva = int(input("Precio del producto sin IVA: "))
iva = int(input("Procentage de IVA: "))

cuota = sin_iva * iva /100
total_producto = cuota + sin_iva

print("Base disponible: " + str(sin_iva) + " €")
print("IVA (" + str(iva) + "%) :" + str(cuota) , " €")
print("Total a pagar: " + str(total_producto) , " €")

#El usuario escribe 50 , pero se muestra 50.0 . ¿Por qué? ¿Qué pasaría si usaras int() en lugar de float() y el usuario escribiera 19.99 ? Contesta en un comentario.
 #Se muestra 50.0 porque float() convierte el número en decimal.
# Si usamos int() con 19.99, se perderían los decimales y quedaría 19.