#--------------------Solución reto #1 --------------------------
VALOR_INTERES = 0.03
VALOR_PERDIDAS = 0.02
VALOR_ANIO = 12
def CDT(usuario: str, capital: int, tiempo: int):
    
    if tiempo > 2:
        valor_intereses = (capital * VALOR_INTERES * tiempo) / VALOR_ANIO
        valor_total = (valor_intereses + capital)
    else:
        valor_perdidas = (capital * VALOR_PERDIDAS)
        valor_total = (capital-valor_perdidas)  
    mensaje = 'Para el usuario ' + str(usuario) + ' La cantidad de dinero a recibir, según  el monto inicial ' + str(capital) + ' para un tiempo de ' + str(tiempo) + ' meses es: ' + str(round(valor_total))
    return mensaje 

user = input("Digite el usuario: ")
monto = int(input("Digite el capital: "))
time = int(input("Digite el tiempo: "))

cdt = CDT(user, monto, time)
print(cdt) 
