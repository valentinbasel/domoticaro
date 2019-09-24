import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import serial
import serial.tools.list_ports
import time

class CDC_EMU(object):

    """ docstring clase CDC 

    interface de conexión serial USB_CDC para el proyecto de domotica
    DOMOTICARO.
    Implementa una capa de abstracción que permite conectar puerto CDC al
    hardware ICARO o ARDUINO,
    es una API para poder interactuar con el firmware DOMOTICARO_V1.
    su funcion es la de preparar el puerto /devttyUSB o ttyACM para enviar
    y recibir datos.
    una ves inicializada la clase, hay que tener en cuenta lo siguiente:
    el metodo self.puerto es donde se carga el valor del dispositivo serie.
    por defecto es /dev/ttyACM0. cambiarla antes de usar la funcion iniciar()
    """
    _PUERTO = '/dev/pts/5'  # valor inicial por defecto
    _BAUDIOS = 9600
    _BYTESIZE = 8
    _PARITY = 'N'
    _STOPBIT = 1
    _TIMEOUT = None
    _XONXOFF = True
    _RTSCTS = True
    _DSRDTR = True
    _RS232 = serial.Serial()
    
    def __init__(self):
        """TODO: to be defined1. """
        pass

    def puerto(self, arg1):
        """TODO: Docstring for puerto.

        :arg1: String con la dirección del puerto /dev/ttyACM para CDC
        :returns: True / False

        """
        self._PUERTO = arg1

    
    def iniciar(self):
        """TODO: Docstring for iniciar.

        :arg1: TODO
        :returns: TODO

        """
        self._RS232.port = self._PUERTO
        self._RS232.baudrate = self._BAUDIOS
        self._RS232.bytesize = self._BYTESIZE
        self._RS232.parity = self._PARITY
        self._RS232.stopbit = self._STOPBIT
        self._RS232.timeout = self._TIMEOUT
        self._RS232.xonxoff = self._XONXOFF
        self._RS232.rtscts = self._RTSCTS
        self._RS232.dsrdtr = self._DSRDTR
        self._RS232.exclusive = True
        try:
            self._RS232.open()
            print ("iniciar la placa en el puerto :",self._PUERTO)
            return True
        except Exception as e:
            raise e
            return False

    def cerrar(self):
        """TODO: Docstring for cerrar.

        :arg1: TODO
        :returns: TODO

        """
        try:
            self._RS232.close()
            return True
        except:
            return False

    def recibir(self):
        """TODO: Docstring for recibir.
        :returns: TODO

        """
        dato=self._RS232.readline()
        print (dato)

    def enviar(self, cadena_caracter):
        """TODO: Docstring for enviar.

        :arg1: TODO
        :returns: TODO

        """
        buff=''
        buff2=""
        if self._RS232.isOpen():
            try:
                for caracter in cadena_caracter:
                    self._RS232.write(caracter.encode("ascii"))
                    #time.sleep(0.01)

                
                while buff != b'\n':
                    buff = self._RS232.read()#self._RS232.inWaiting())
                    buff2 = buff2 + buff.decode("ascii") 
                    #print (buff2)
                #self._RS232.flush()
                return buff2
            except Exception as e:
                print(e)
                print("no se pudo completar el envio de datos")
                return False 
        else:
            print("el puerto: ",self._PUERTO, " esta cerrado")
            return False

class EMULADOR(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Emulador DOMOTICARO")

        self.box = Gtk.VBox(spacing=6)
        self.add(self.box)
        self.frame_LCD = Gtk.Frame(label="LCD")
        self.label_lcd1 = Gtk.Label(label = "Salida 1: ")
        self.label_lcd1.set_justify(Gtk.Justification.RIGHT)
        self.label_lcd2 = Gtk.Label(label = "Salida 2: ")
        self.label_lcd2.set_justify(Gtk.Justification.RIGHT)
        
        box_frame = Gtk.VBox(spacing =4)

        box_frame.pack_start(self.label_lcd1,True,True,0)
        box_frame.pack_start(self.label_lcd2,True,True,0)

        self.frame_LCD.add(box_frame)
        self.box.pack_start(self.frame_LCD,True,True,0)

        self.box_botones = Gtk.Box(spacing=6)
        self.box.pack_start(self.box_botones,True,True,0)

        self.button1 = Gtk.Button(label="Conectar")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box_botones.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Salir")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box_botones.pack_start(self.button2, True, True, 0)
        self.cdc = CDC_EMU()
    def on_button1_clicked(self, widget):
        print("conectar")
        self.cdc.iniciar()
        self.cdc.recibir()

    def on_button2_clicked(self, widget):
        print("salir")


win = EMULADOR()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
