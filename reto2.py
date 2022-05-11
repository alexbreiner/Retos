#------------------Aventuras extremas-------------------------#
def cliente(informacion:dict):
    # X-treme
    EDAD_X_TREME = int(18)
    PRECIO_BOLETA_X_TREME = int(20000)
    DESCUENTO_BOLETA_X_TREME = float(0.95)
    
    #Carros chocones
    EDAD_CARROS_CHOCONES = int(15)
    PRECIO_BOLETA_CARROS_CHOCONES = int(5000)
    DESCUENTO_BOLETA_CARROS_CHOCONES = float(0.93)
    
    #Sillas boladoras
    EDAD_SILLAS_VOLADORAS = int(7)
    PRECIO_BOLETA_SILLAS_VOLADORAS = int(10000)
    DESCUENTO_BOLETA_SILLAS_VOLADORAS = float(0.95)
    
    if informacion['edad'] > EDAD_X_TREME:
        atraccion = 'X-Treme'
        isApto = True
        if informacion['primer_ingreso'] == True:
            valorBoletas = PRECIO_BOLETA_X_TREME * DESCUENTO_BOLETA_X_TREME
        else: valorBoletas = PRECIO_BOLETA_X_TREME
    
    elif informacion['edad'] >= EDAD_CARROS_CHOCONES:
        atraccion = 'Carros chocones'
        isApto = True
        if informacion['primer_ingreso'] == True:
            valorBoletas = PRECIO_BOLETA_CARROS_CHOCONES * DESCUENTO_BOLETA_CARROS_CHOCONES
        else: valorBoletas = PRECIO_BOLETA_CARROS_CHOCONES
    
    elif informacion['edad'] >= EDAD_SILLAS_VOLADORAS:
        atraccion = 'Sillas voladoras'
        isApto = True
        if informacion['primer_ingreso'] == True:
            valorBoletas = PRECIO_BOLETA_SILLAS_VOLADORAS * DESCUENTO_BOLETA_SILLAS_VOLADORAS
        else: valorBoletas = PRECIO_BOLETA_SILLAS_VOLADORAS
    
    else: 
        atraccion = 'N/A'
        isApto = False
        valorBoletas = 'N/A' 
                    
    resultado = {
            'nombre': informacion['nombre'],
            'edad': informacion['edad'],
            'atraccion': atraccion,
            'apto': isApto, 
            'primer_ingreso': informacion['primer_ingreso'],
            'total_boleta': valorBoletas
        }
    return resultado
        
informacion = {}
informacion['id_cliente'] = int(input("Digite el ID del cliente: "))
informacion['nombre'] = str(input("Digite el nombre: "))
informacion['edad'] = int(input("Digite el edad: "))
informacion['primer_ingreso'] = bool(input("Es su primer ingreso (1 si, '' no): "))

mostrarInfomacion = cliente(informacion)

print(mostrarInfomacion)

