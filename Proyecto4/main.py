import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Nuevas variables difusas
temperature = ctrl.Antecedent(np.arange(0, 41, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Funciones de membresía de temperatura
temperature['cold'] = fuzz.trapmf(temperature.universe, [0, 0, 15, 20])
temperature['warm'] = fuzz.trimf(temperature.universe, [15, 25, 35])
temperature['hot'] = fuzz.trapmf(temperature.universe, [30, 35, 40, 40])

# Funciones de membresía de humedad
humidity['low'] = fuzz.trapmf(humidity.universe, [0, 0, 30, 40])
humidity['medium'] = fuzz.trimf(humidity.universe, [30, 50, 70])
humidity['high'] = fuzz.trapmf(humidity.universe, [60, 70, 100, 100])

# Funciones de membresía de velocidad del ventilador
fan_speed['off'] = fuzz.trapmf(fan_speed.universe, [0, 0, 20, 30])
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [20, 40, 60])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [40, 60, 80])
fan_speed['high'] = fuzz.trapmf(fan_speed.universe, [70, 90, 100, 100])

# Visualización y guardado de imágenes
def save_view(variable, filename):
    plt.figure()
    variable.view()
    plt.savefig(f'images/{filename}.png')
    plt.close()

save_view(temperature, 'temperature_view')
save_view(humidity, 'humidity_view')
save_view(fan_speed, 'fan_speed_view')

# Reglas
rule1 = ctrl.Rule(temperature['cold'] & humidity['low'], fan_speed['off'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['medium'], fan_speed['low'])
rule3 = ctrl.Rule(temperature['cold'] & humidity['high'], fan_speed['low'])
rule4 = ctrl.Rule(temperature['warm'] & humidity['low'], fan_speed['low'])
rule5 = ctrl.Rule(temperature['warm'] & humidity['medium'], fan_speed['medium'])
rule6 = ctrl.Rule(temperature['warm'] & humidity['high'], fan_speed['high'])
rule7 = ctrl.Rule(temperature['hot'] & humidity['low'], fan_speed['high'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['medium'], fan_speed['high'])
rule9 = ctrl.Rule(temperature['hot'] & humidity['high'], fan_speed['high'])

# Sistema de control
fan_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
fan_simulation = ctrl.ControlSystemSimulation(fan_control)

# Entradas
fan_simulation.input['temperature'] = 25
fan_simulation.input['humidity'] = 65

# Computa la salida
fan_simulation.compute()

print(f"Velocidad del ventilador: {fan_simulation.output['fan_speed']}")

# Guardar visualización de la simulación de la salida
plt.figure()
fan_speed.view(sim=fan_simulation)
plt.savefig('images/fan_speed_simulation.png')
plt.close()
