def CDT(usuario: str, capital: int, tiempo: int):
    
    if tiempo > 2:
        valor_intereses = (capital * 0.03 * tiempo)/12
        valor_total = (valor_intereses + capital)
    else:
        valor_perdidas = (capital * 0.02)
        valor_total = (capital-valor_perdidas)  
    mensaje = 'Para el usuario ' + str(usuario) + ' La cantidad de dinero a recibir, según  el monto inicial ' + str(capital) + ' para un tiempo de ' + str(tiempo) + ' meses es: ' + str(round(valor_total))
    return mensaje 

user = input("Digite el usuario: ")
monto = int(input("Digite el capital: "))
time = int(input("Digite el tiempo: "))

cdt = CDT(user, monto, time)
print(cdt) 