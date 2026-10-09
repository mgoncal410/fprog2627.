examen1 = 6.5
examen2 = 4.0
proyecto = 7.2
teoria = 0.4
practico = 0.6
nota_para_aprobar = 5

media_teoria = (examen1+examen2)/2
nota_final = (media_teoria * teoria + proyecto * practico)
aprobado = nota_final >= nota_para_aprobar
print("Media de teoria", media_teoria,
      "\nNota final", nota_final,
      "\n¿Aprobado?", aprobado )