import os
from  PyLTSpice.LTSpiceBatch import SimCommander,LTCommander
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
from interfaz.principal import Principal
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import time


class Ventana(QtWidgets.QMainWindow, Principal):
    def __init__(self):
        self.setupUI(self)



    def simular(self):
        # se crea la simulacion
        simulation = SimCommander(os.path.dirname(os.path.realpath(__file__)) + "\\Ecualizador.asc")
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

        # se configuran los valores de resistencia
        



def hola(a,b):  #fubncion callback
    print("hola")


simulation = SimCommander(os.path.dirname(os.path.realpath(__file__)) + "\\Ecualizador.asc")
simulation.set_component_value('V3', 'wavefile=Pistas/Bass.wav')
simulation.set_component_value('V4', 'wavefile="Pistas/EG 2.wav"')
simulation.set_component_value('V5', 'wavefile="Pistas/Keys 1.wav"')
# se indica que se debe exportar el .wav
simulation.add_instructions(".wave salida.wav 16 44.1k V(vout)",
                            ".tran 10")
simulation.run()
simulation.wait_completion()

LTR = LTSpiceRawRead("Ecualizador_1.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())


Vo = LTR.get_trace("V(Vout)")
x = LTR.get_trace('time') # Gets the time axis
steps = LTR.get_steps()
for step in range(len(steps)):
    # print(steps[step])
    plt.plot(x.get_time_axis(step), Vo.get_wave(step), label=steps[step])

plt.legend() # order a legend
plt.show()

