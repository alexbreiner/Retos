
def AutoPartes(ventas: list):
    registroVentas = {}
    for i in range(len(ventas)):
        registroVentas[i] = [ventas[i]]
    return registroVentas

def consultaRegistro(ventas, idProducto):
    informacionVenta = ''
    informacionVentas = {}
    SIN_PRODUCTOS = 0
    for j in range(len(ventas)):
        if idProducto == ventas[j][0][0]:
            informacionVentas[j] = ventas[j]
    
    if len(informacionVentas) == SIN_PRODUCTOS:
        informacionVenta = 'No hay registro de venta de ese producto' 
        
    for y in informacionVentas.values():
        informacionVenta += "Producto consultado : {}  Descripción  {}  #Parte  {}  Cantidad  vendida  {}  Stock  {}  Comprador  {}  Documento  {}  Fecha Venta  {}\n".format(
        y[0][0], y[0][1] , y[0][2], y[0][3], y[0][4], y[0][5], y[0][6], y[0][7])    
    return print(informacionVenta)

consultaRegistro(AutoPartes([
(2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
(2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
(2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
(3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
(9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)

    #informacionVenta = 'Producto consultado ' + str(informacionVentas[y][0][0]) + ' Descripción ' + str(informacionVentas[y][0][1] + ' #Parte ' + str(informacionVentas[y][0][2]) + ' Cantidad vendida ' + str(informacionVentas[y][0][3]) + ' Stock ' + str(informacionVentas[y][0][4]) + ' Comprador # ' + str(informacionVentas[y][0][5]) + ' Documento ' + str(informacionVentas[y][0][6]) + ' Fecha Venta ' + str(informacionVentas[y][0][7]))
    #informacionVenta =  Producto consultado : {} Descripción {} #Parte {} Cantidad vendida {} Stock {} Comprador {} Documento {} Fecha Venta {} 
    