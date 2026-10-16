# Ejercicio 3 - Conversor de segundos
# Este programa esta hecho por Manuel González Calandria

segundos = int(input("Introduce los segundos: "))
segundos_totales = segundos % 60
minutos_totales = (segundos // 60) % 60
horas_totales = (segundos // 3600)

print(str(segundos) + " segundos son " + str(horas_totales) + " h " + str(minutos_totales) + " min " + str(segundos_totales) + " s")
print("Formato reloj: "+ str(horas_totales) + ":"+ str(minutos_totales) + ":" + str(segundos_totales))