import domoticaro
import time 
casa = domoticaro.iniciar("arduino")
casa.hardware.iniciar("/dev/ttyACM0")

rele1 = casa.hardware.Rele_1
rele2 = casa.hardware.Rele_2 
rele3 = casa.hardware.Rele_3
rele4 = casa.hardware.Rele_4

time.sleep(2)
for t in range(4):
    print("prendo")
    casa.hardware.Rele_1.on()
    casa.hardware.Rele_2.on()
    casa.hardware.Rele_3.on()
    casa.hardware.Rele_4.on()

    time.sleep(5)
    print("apago")
    casa.hardware.Rele_1.off()
    casa.hardware.Rele_2.off()
    casa.hardware.Rele_3.off()
    casa.hardware.Rele_4.off()

    time.sleep(5)    
    
casa.hardware.cerrar()


