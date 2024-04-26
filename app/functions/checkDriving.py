def checkDriving(temp, rpm, velocidad, posicion_acelerador):
    msg = "Todo esta correcto."

    #AVISOS DE TEMPERATURA
    if temp <= 65:
        msg = "El motor se encuentra frio, procure no exigirlo demasiado."
        if rpm >= 3500:
            msg = "El motor no llegó a su temperatura óptima, procure disminuir el acelerador."

    if (temp >= 90 and temp <= 100):
        msg = "Temperatura del motor óptima alcanzada."

    if(temp >= 120):
        msg = "Atención!. La temperatura del motor es muy elevada, disminuya su velocidad o estacione el vehiculo sin apagar el motor."

    #AVISOS DE REVOLUCION Y VELOCIDAD
    if rpm >= 6000:
        msg = "Cuidado!. Esta exigiendo muchas revoluciones al motor, se recomienda disminuir el acelerador."

    if velocidad > 120:
        msg = "Precaución, mantener esa velocidad podría ser peligroso y elevar el consumo de combustible."

    
    #POSICION DE ACELERADOR
    if posicion_acelerador >= 80:
        msg = "Advertencia, utilizar el acelerador a fondo llevará a un alto consumo de combustible"

    
    return msg
