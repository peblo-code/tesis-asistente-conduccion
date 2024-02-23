import obd
import time
import pygame
import os

# Inicializa pygame
pygame.init()

# Crea una instancia del reproductor de sonido
pygame.mixer.init()

# Carga el archivo de sonido
sound = pygame.mixer.Sound('./static/2023-10-27 16-22-21.mp3')

# Inicializa la conexión OBD-II
ports = obd.scan_serial()      # return list of valid USB or RF ports                
connection = obd.OBD(ports[1]) # connect to the first port in the list

# Bandera
flagAlarm = 0



def checkShift():
    while True:
        speed = connection.query(obd.commands.SPEED).value.magnitude
        if speed > 15:
            rpm = connection.query(obd.commands.RPM).value.magnitude
            throttle = connection.query(obd.commands.THROTTLE_POS).value.magnitude
            engineLoad = connection.query(obd.commands.ENGINE_LOAD).value.magnitude
            if(engineLoad > 75 and throttle >= 50 and rpm <= 2900):
                os.system('cls')
                print("SHIFT DOWN!")          
                # Reproduce el sonido
                sound.play()

                # Espera a que el sonido termine de reproducirse antes de salir
                pygame.time.wait(int(sound.get_length() * 1000))

                # Detén pygame
                
            elif(engineLoad > 35 and throttle >= 20 and throttle <= 40 and rpm > 2400):
                os.system('cls')
                print("SHIFT UP!")
                # Reproduce el sonido
                sound.play()

                # Espera a que el sonido termine de reproducirse antes de salir
                if flagAlarm == 0:
                    pygame.time.wait(int(sound.get_length() * 1000))
                    flagAlarm = 1

                # Detén pygame
                
            else:
                os.system('cls')
                print("Nice")
                flagAlarm = 1
        else:
            os.system('cls')
            print("Ralenti")
            flagAlarm = 1
        time.sleep(1)

checkShift()
