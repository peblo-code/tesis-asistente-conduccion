import pygame

def checkShift(speedValue, rpmValue, throttle, engineLoad):
    # Inicializa pygame
    pygame.init()

    # Crea una instancia del reproductor de sonido
    pygame.mixer.init()

    # Carga el archivo de sonido
    sound = pygame.mixer.Sound('../app/static/2023-10-27 16-22-21.mp3')
    
    if speedValue > 15:

        if(engineLoad > 75 and throttle >= 50 and rpmValue <= 2900):
            # Reproduce el sonido
            sound.play()

            # Espera a que el sonido termine de reproducirse antes de salir
            pygame.time.wait(int(sound.get_length() * 1000))

            sound.stop()
            return("↓")

            # Detén pygame
            
        elif(engineLoad > 35 and throttle >= 20 and throttle <= 40 and rpmValue > 2400):
            # Reproduce el sonido
            sound.play()

            # Espera a que el sonido termine de reproducirse antes de salir
            pygame.time.wait(int(sound.get_length() * 1000))

            sound.stop()
            return("↑")
            
        else:
            return("-")

    else:
        return("-")

