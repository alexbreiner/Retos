from functools import reduce

def ordenes(rutinaContable):
    rutinasContables = rutinaContable
    accesoContables = lambda acumulador = 0, elemento = 0:acumulador + elemento
    COMPRA_PRECIO_INCREMENTO = 25000
    COMPRA_TOTAL = 600000
    mensaje = ''
    opcion1 = lambda valor1 = 0:valor1[1:]
    opcion2 = lambda valor1 = 0:list(map(lambda valor2 = 0:valor2[1] * valor2[2], valor1))
    opcion3 = lambda valor1 = 0:reduce(accesoContables, valor1)
    opcion4 = lambda valor1 = 0:round(valor1 + COMPRA_PRECIO_INCREMENTO, 2) if valor1 < COMPRA_TOTAL else round(valor1, 2)
    opcion5 = lambda valor1 = 0:valor1[0]
    #Quitar el número de factura
    resultado1 = list(map(opcion1, rutinasContables))
    #multiplicar cantidad por el precio unitario
    resultado2 = list(map(opcion2, resultado1))
    # Sumar todos los valores de cada fila 
    resultado3 = list(map(opcion3, resultado2))
    #Sumar 25.000 en caso de que la compra sea menor a 600.000 y redonder a 2 cifras
    resultado4 = list(map(opcion4, resultado3))
    #obtener los numeros de factura
    numerosDeFactura = list(map(opcion5, rutinasContables))
    #numerosDeFactura = list()
    resultadoTotal = list(zip(resultado4, numerosDeFactura))
    

    print('----------------- Fin Registro diario -----------------------------')
    #print('La factura {} tiene un total en pesos de {:,.2f}'.format(resultadoTotal[0], resultadoTotal[1][0]))
    for i in resultadoTotal:
        print('La factura {} tiene un total en pesos de {:,.2f}'.format(numerosDeFactura[0], resultadoTotal[0][0]))

        #print (f'La factura {numerosDeFactura[0]} tiene un total en pesos de {resultadoTotal[0][0]:,.2f}')

        #mensaje2 = 'La factura {} tiene un total en pesos de {:,.2f}'.format(numerosDeFactura[1], resultadoTotal[1][0])
        #mensaje3 = 'La factura {} tiene un total en pesos de {:,.2f}'.format(numerosDeFactura[2], resultadoTotal[2][0])
        #mensaje4 = 'La factura {} tiene un total en pesos de {:,.2f}'.format(numerosDeFactura[3], resultadoTotal[3][0])
    print('----------------- Inicio Registro diario --------------------------')

ordenes([
        [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
        [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
        [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
        [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
       ## [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)],
       # [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
        ])


