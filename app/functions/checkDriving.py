import pyttsx3
import flet as ft

def checkDriving(temp, rpm, velocidad, posicion_acelerador, flagTemp, lastidmsg):
    def convertTexttoVoice(text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 130)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(text)
        engine.runAndWait()
    msg = "Todo esta correcto."
    idmsg = "Ok."

    #AVISOS DE TEMPERATURA
    if temp <= 60:
        msg = "El motor se encuentra frio, procure no exigirlo demasiado."
        idmsg="T01-"
        if rpm >= 3000:
            msg = "El motor no llegó a su temperatura óptima, procure disminuir el acelerador."
            idmsg="T02!"
    
    if temp >= 61 and temp <= 74:
        msg = "El motor esta a punto de alcanzar su temperatura optima."
        idmsg="T03-"

    if (temp >= 75 and temp <= 100 and flagTemp < 15):
        msg = "Temperatura óptima del motor alcanzada."
        flagTemp = flagTemp + 1
        idmsg="T04."

    if(temp >= 120):
        msg = "Atención!. La temperatura del motor es muy elevada, disminuya su velocidad o estacione el vehiculo sin apagar el motor."
        idmsg="T05!"

    #AVISOS DE REVOLUCION Y VELOCIDAD
    if rpm >= 6000:
        msg = "Cuidado!. Esta exigiendo muchas revoluciones al motor, se recomienda disminuir el acelerador."
        idmsg="RV01!"

    if velocidad > 120:
        msg = "Precaución, mantener esa velocidad podría ser peligroso y elevar el consumo de combustible."
        idmsg="RV02-"
    
    #POSICION DE ACELERADOR
    if posicion_acelerador >= 80:
        msg = "Advertencia, utilizar el acelerador a fondo llevará a un alto consumo de combustible"
        idmsg="RV03-"

    modeMsg = idmsg[-1]
    color = None
    if(modeMsg == "."):
        color = ft.colors.GREEN_700
    
    if(modeMsg == "-"):
        color = ft.colors.YELLOW_700

    if(modeMsg == "!"):
        color = ft.colors.RED_700

    if lastidmsg != idmsg: #si el id del mensaje es diferente, hablar
        convertTexttoVoice(msg)
    
    return [msg, flagTemp, color, idmsg]
