import obd
import time
import pygame
from obdConnection import tryConnection

def checkShift():
    if tryConnection():
        # Inicializa pygame
        pygame.init()

        # Crea una instancia del reproductor de sonido
        pygame.mixer.init()

        # Carga el archivo de sonido
        sound = pygame.mixer.Sound('./app/static/2023-10-27 16-22-21.mp3')

        # Bandera
        flagAlarm = 0

        # Se establece la conexion
        connection = tryConnection()
        
        while True:
            speed = connection.query(obd.commands.SPEED).value.magnitude
            if speed > 15:
                rpm = connection.query(obd.commands.RPM).value.magnitude
                throttle = connection.query(obd.commands.THROTTLE_POS).value.magnitude
                engineLoad = connection.query(obd.commands.ENGINE_LOAD).value.magnitude
                if(engineLoad > 75 and throttle >= 50 and rpm <= 2900):
                    return("DOWN")          
                    # Reproduce el sonido
                    sound.play()

                    # Espera a que el sonido termine de reproducirse antes de salir
                    pygame.time.wait(int(sound.get_length() * 1000))

                    # Detén pygame
                    
                elif(engineLoad > 35 and throttle >= 20 and throttle <= 40 and rpm > 2400):
                    return("UP")
                    # Reproduce el sonido
                    sound.play()

                    # Espera a que el sonido termine de reproducirse antes de salir
                    if flagAlarm == 0:
                        pygame.time.wait(int(sound.get_length() * 1000))
                        flagAlarm = 1

                    # Detén pygame
                    
                else:
                    return("OK")
                    flagAlarm = 1
            else:
                return("OK-N")
                flagAlarm = 1
            time.sleep(1)
    else:
        print("Ups")
        return 0

checkShift()
