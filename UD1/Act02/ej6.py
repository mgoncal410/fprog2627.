total_segundos = 100000
segundos_minutos = 60
segundos_horas = 3600
segundos_dias = 86400

dias = total_segundos // segundos_dias
resto = total_segundos % segundos_dias

horas = resto // segundos_horas
resto = resto % segundos_horas

minutos = resto // segundos_minutos
segundos = resto % segundos_minutos

print(total_segundos, "segundos son"
      , dias, "dias,"
      , horas, "horas,"
      , minutos, "minutos y"
      , segundos, "segundos")
