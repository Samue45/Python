import datetime

fecha_actual = datetime.datetime.now()

formato = fecha_actual.strftime("%d-%m-%Y %H:%M:%S")

print(f"Fecha y hora actual {formato}")

fecha1_str = input("Ingresa la 1º fecha = ")
fecha2_str= input("Ingresa la 2º fecha = ")

fecha1 = datetime.datetime.strptime(fecha1_str,"%d-%m-%Y")
fecha2 = datetime.datetime.strptime(fecha2_str,"%d-%m-%Y")

diferencia_fechas = fecha2 - fecha1

print(f"La diferencia entre las fechas es de {abs(diferencia_fechas)}")
