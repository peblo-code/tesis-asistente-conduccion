import flet as ft
def checkShift(speedValue, rpmValue, throttle, engineLoad, bipAudio):
    
    if speedValue > 15:

        if(engineLoad > 75 and throttle >= 50 and rpmValue <= 2900):
            # Reproduce el sonido
            bipAudio.play()

            # Espera a que el sonido termine de reproducirse antes de salir
            bipAudio.pause()

            
            return("↓")

            # Detén pygame
            
        elif(engineLoad > 35 and throttle >= 20 and throttle <= 40 and rpmValue > 2400):
            # Reproduce el sonido
            bipAudio.play()

            # Espera a que el sonido termine de reproducirse antes de salir
            bipAudio.pause()

            
            return("↑")
            
        else:
            return("-")

    else:
        return("-")

