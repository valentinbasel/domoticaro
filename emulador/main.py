import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class SwitcherWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Switch Demo")
        self.set_border_width(10)
        frame = Gtk.Frame(label = "Actuadores")
        vbox = Gtk.VBox(spacing=6)
        frame.add(vbox)
        self.add(frame)
        for a in range(4):
            hbox = Gtk.HBox(spacing=4)
            label = Gtk.Label("Rele_"+str(a))
            switch = Gtk.Switch()
            switch.connect("notify::active", self.on_switch_activated,a)
            switch.set_active(True)
            hbox.pack_start(label,True,True, 0)
            hbox.pack_start(switch,True,True, 0)
            vbox.pack_start(hbox, True, True, 0)

        for a in range(4):
            hbox = Gtk.HBox(spacing=4)
            label = Gtk.Label("Dig_"+str(a))
            switch = Gtk.Switch()
            switch.connect("notify::active", self.on_switch_activated,a)
            switch.set_active(True)
            hbox.pack_start(label,True,True, 0)
            hbox.pack_start(switch,True,True, 0)
            vbox.pack_start(hbox, True, True, 0)

        for b in range(3):
            hbox = Gtk.HBox(spacing=4)
            progressbar = Gtk.LevelBar()
            progressbar.set_min_value(0)
            progressbar.set_max_value(180)
            progressbar.set_value(90)
            label = Gtk.Label("Servo_"+str(b))
            hbox.pack_start(label,True,True, 0)
            label_valor = Gtk.Label(str(progressbar.get_value())) 
            hbox.pack_start(label,True,True,0)
            hbox.pack_start(progressbar,True,True, 0)
            hbox.pack_start(label_valor,True,True,0)
            vbox.pack_start(hbox,True,True,0)

        for b in range(2):
            hbox = Gtk.HBox(spacing=4)
            progressbar = Gtk.LevelBar()
            progressbar.set_min_value(0)
            progressbar.set_max_value(100)
            progressbar.set_value(30)
            label = Gtk.Label("PWM_"+str(b))
            hbox.pack_start(label,True,True, 0)
            label_valor = Gtk.Label(str(progressbar.get_value())) 
            hbox.pack_start(label,True,True,0)
            hbox.pack_start(progressbar,True,True, 0)
            hbox.pack_start(label_valor,True,True,0)
            vbox.pack_start(hbox,True,True,0)




    def on_switch_activated(self, switch, gparam,valor_rele):
        if switch.get_active():
            state = "on"
        else:
            state = "off"
        print("Rele_",valor_rele,": ", state)

win = SwitcherWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
