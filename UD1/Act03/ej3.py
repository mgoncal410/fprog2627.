segundos = int(input("Introduce los segundos: "))
segundos_totales = segundos % 60
minutos_totales = (segundos // 60) % 60
horas_totales = (segundos // 3600) % 24

print(str(segundos) + "segundos son " + str(horas_totales) + " h " + str(minutos_totales) + " min " + str(segundos_totales) + " s")
