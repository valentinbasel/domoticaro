import domoticaro
import time 
casa = domoticaro.iniciar("icaro_cdc")
casa.hardware.iniciar("/dev/ttyACM0")

rele1 = casa.hardware.Rele_1
rele2 = casa.hardware.Rele_2 
rele3 = casa.hardware.Rele_3
rele4 = casa.hardware.Rele_4
# ~ LCD = casa.hardware.lcd 
# ~ a = casa.hardware.Analogico_1

# ~ for t in range(9):
    # ~ valor =str(a.leer())
    # ~ LCD.borrar()
    # ~ LCD.escribir("la temp es: "+valor) 
    # ~ time.sleep(1)

# rele1.on()
# time.sleep(1)
# rele1.off()
# time.sleep(1)

for t in range(17):
    print("prendo")
    casa.hardware.Rele_1.on()
    casa.hardware.Rele_2.on()
    casa.hardware.Rele_3.on()
    casa.hardware.Rele_4.on()

    time.sleep(1)
    print("prendo")
    casa.hardware.Rele_1.off()
    casa.hardware.Rele_2.off()
    casa.hardware.Rele_3.off()
    casa.hardware.Rele_4.off()

    time.sleep(1)    
    
casa.hardware.cerrar()


