import os
from  PyLTSpice.LTSpiceBatch import SimCommander
from PyLTSpice.LTSpice_RawRead import LTSpiceRawRead
import matplotlib.pyplot as plt

entrada = input("Ingrese la ruta del .wav: ")
simulation = SimCommander(os.path.dirname(os.path.realpath(__file__))+ "\\probando.asc")
simulation.set_component_value('R1', '10k')
simulation.set_component_value('V1', 'wavefile='+entrada)
# se indica que se debe exportar el .wav
simulation.add_instructions(".wave salida.wav 16 44.1k V(vout)",
                            ".tran 5")
simulation.run()
simulation.wait_completion()

LTR = LTSpiceRawRead("probando_1.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())

IR1 = LTR.get_trace("V(vin)")
Vo = LTR.get_trace("V(vout)")
x = LTR.get_trace('time') # Gets the time axis
steps = LTR.get_steps()
for step in range(len(steps)):
    # print(steps[step])
    plt.plot(x.get_time_axis(step), IR1.get_wave(step), label=steps[step])
    plt.plot(x.get_time_axis(step), Vo.get_wave(step), label=steps[step])

plt.legend() # order a legend
plt.show()

