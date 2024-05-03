import playsound

def checkShift(speedValue, rpmValue, throttle, engineLoad):

    # Carga el archivo de sonido
    sound = '../app/static/2023-10-27 16-22-21.mp3'
    
    if speedValue > 15:

        if(engineLoad > 75 and throttle >= 50 and rpmValue <= 2900):
            # Reproduce el sonido
            playsound(sound)

            # Espera a que el sonido termine de reproducirse antes de salir
            

            
            return("↓")

            # Detén pygame
            
        elif(engineLoad > 35 and throttle >= 20 and throttle <= 40 and rpmValue > 2400):
            # Reproduce el sonido
            playsound(sound)

            # Espera a que el sonido termine de reproducirse antes de salir
            

            
            return("↑")
            
        else:
            return("-")

    else:
        return("-")

