saldo = 50
ingreso = 20
gasto = 15
factor_abuela = 2
reparto_entre = 2

saldo_inicial = saldo

saldo += ingreso
tras_ingreso = saldo

saldo -= gasto
tras_gasto = saldo

saldo *= factor_abuela
tras_regalo = saldo

saldo /= reparto_entre
tras_reparto = saldo 

print("Saldo inicial: ", saldo_inicial, " €",
      "\nTras ingreso: ", tras_ingreso, " €",
      "\nTras gasto: ", tras_gasto, " €",
      "\nTras regalo: ", tras_regalo, " €",
      "\nTras reparto: ", tras_reparto, " €", sep="")