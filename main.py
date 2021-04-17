import os
from  PyLTSpice.LTSpiceBatch import SimCommander,LTCommander
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
from interfaz.principal import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import time


class Ventana(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnMezclar.clicked.connect(self.simular)
        self.btnBlues.clicked.connect(self.blues)
        self.btnJazz.clicked.connect(self.jazz)
        self.btnRock.clicked.connect(self.rock)
        self.btnMetal.clicked.connect(self.metal)
        # se llenan los combo box
        archivo = os.listdir("Pistas")

        for i in archivo:
            self.cmbTrack1.addItem(i)
            self.cmbTrack2.addItem(i)
            self.cmbTrack3.addItem(i)
        

    def blues(self):
        self.Slider1.setValue(-5)
        self.Slider2.setValue(-5)
        self.Slider3.setValue(0)
        self.Slider4.setValue(0)
        self.Slider5.setValue(0)
        self.Slider6.setValue(5)
        self.Slider7.setValue(10)
        self.Slider8.setValue(15)
        self.Slider9.setValue(10)
        self.Slider10.setValue(5)

    def jazz(self):
        self.Slider1.setValue(0)
        self.Slider2.setValue(0)
        self.Slider3.setValue(0)
        self.Slider4.setValue(5)
        self.Slider5.setValue(5)
        self.Slider6.setValue(5)
        self.Slider7.setValue(0)
        self.Slider8.setValue(5)
        self.Slider9.setValue(5)
        self.Slider10.setValue(10)

    def rock(self):
        self.Slider1.setValue(0)   
        self.Slider2.setValue(3)
        self.Slider3.setValue(6)
        self.Slider4.setValue(9)
        self.Slider5.setValue(0)
        self.Slider6.setValue(0)
        self.Slider7.setValue(5)
        self.Slider8.setValue(5)
        self.Slider9.setValue(0)
        self.Slider10.setValue(5)

    def metal(self):
        self.Slider1.setValue(3)
        self.Slider2.setValue(6)
        self.Slider3.setValue(9)
        self.Slider4.setValue(15)
        self.Slider5.setValue(3)
        self.Slider6.setValue(3)
        self.Slider7.setValue(3)
        self.Slider8.setValue(-3)
        self.Slider9.setValue(-3)
        self.Slider10.setValue(-3)

    def simular(self):
        # se crea la simulacion
        simulation = SimCommander(os.path.dirname(os.path.realpath(__file__)) + "\\Ecualizador.asc")
        # valores para los parametros
        nombreSalida = self.txtNombre.text()
        print(self.chckDistortion.isChecked())
        # establecer si se quiere distorsion o no
        # resistencias de retroalimentacion negativa de los amplificadores no inversores de cada banda
        r1 = 10**(self.Slider1.value()/20) * 10000 # calculo del valor de la primera resistenica
        r2 = 10**(self.Slider2.value()/20) * 10000 # calculo del valor de la segunda resistenica
        r3 = 10**(self.Slider3.value()/20) * 10000 # calculo del valor de la tercera resistenica
        r4 = 10**(self.Slider4.value()/20) * 10000 # calculo del valor de la cuarta resistenica
        r5 = 10**(self.Slider5.value()/20) * 10000 # calculo del valor de la quinta resistenica
        r6 = 10**(self.Slider6.value()/20) * 10000 # calculo del valor de la sexta resistenica
        r7 = 10**(self.Slider7.value()/20) * 10000 # calculo del valor de la septima resistenica
        r8 = 10**(self.Slider8.value()/20) * 10000 # calculo del valor de la octava resistenica
        r9 = 10**(self.Slider9.value()/20) * 10000 # calculo del valor de la novena resistenica
        r10 = 10**(self.Slider10.value()/20) * 10000 # calculo del valor de la decima resistenica

        if self.chckDistortion.isChecked():
           simulation.set_parameter('distor', '1')
        else:
           simulation.set_parameter('distor', '0')

        cancion1 = self.cmbTrack1.itemText(self.cmbTrack1.currentIndex())
        cancion2 = self.cmbTrack2.itemText(self.cmbTrack2.currentIndex())
        cancion3 = self.cmbTrack3.itemText(self.cmbTrack3.currentIndex())

        if cancion1 == "Elige una pista:":
            cancion1 = '0'
        else:
            cancion1 = 'wavefile= "Pistas/'+cancion1 + '"'
            
        if cancion2 == "Elige una pista:":
            cancion2 = '0'
        else:
            cancion2 = 'wavefile="Pistas/'+cancion2 + '"'

        if cancion3 == "Elige una pista:":
            cancion3 = '0'
        else:
            cancion3 = 'wavefile=  "Pistas/'+cancion3 + '"'


        print(cancion1)
        print(cancion2)
        print(cancion3)
        # se configuran los valores de resistencia
        simulation.set_component_value('R76', str(r1))
        simulation.set_component_value('R78', str(r2))
        simulation.set_component_value('R80', str(r3))
        simulation.set_component_value('R82', str(r4))
        simulation.set_component_value('R84', str(r5))
        simulation.set_component_value('R86', str(r6))
        simulation.set_component_value('R88', str(r7))
        simulation.set_component_value('R90', str(r8))
        simulation.set_component_value('R92', str(r9))
        simulation.set_component_value('R94', str(r10))
        simulation.set_component_value('V3', cancion1)
        simulation.set_component_value('V4', cancion2)
        simulation.set_component_value('V5', cancion3)
        # se indica que se debe exportar el .wav
        simulation.add_instructions(".wave " + nombreSalida + ".wav 16 44.1k V(vout)",
                                    ".tran 12")
        simulation.run()
        simulation.wait_completion() # espera a que se complete
        print("simulacion finalizada")


app = QtWidgets.QApplication([])
ventana = Ventana()
ventana.show()
app.exec_()































