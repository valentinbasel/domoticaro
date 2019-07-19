import domoticaro
import time 
casa = domoticaro.iniciar("icaro_cdc")
casa.hardware.iniciar("/dev/ttyACM0")

rele1 = casa.hardware.Rele_1
rele2 = casa.hardware.Rele_2 
rele3 = casa.hardware.Rele_3
rele4 = casa.hardware.Rele_4
LCD = casa.hardware.lcd 
a = casa.hardware.Analogico1

# for t in range(9):
    # valor =str(a.leer())
    # LCD.borrar()
    # LCD.escribir("la temp es: "+valor) 
    # time.sleep(1)

# rele1.on()
# time.sleep(1)
# rele1.off()
# time.sleep(1)

for t in range(17):
    casa.hardware.Rele_1.conmutar()
    print (rele2.conmutar())
    print (rele3.conmutar())
    print (rele4.conmutar())
    time.sleep(3)
    
casa.hardware.cerrar()


