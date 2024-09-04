
"""
Integrantes:
• Gustavo Adolfo Cruz Bardales - 22779
• Javier Andrés Chen González - 22153
• Josué Emanuel Say Garcia - 22801
• Pedro Pablo Guzmán Mayén - 22111
• Mathew Alexander Cordero Aquino - 22982
• Sebastián Estrada Tuch - 21405

"""

from Parser import *
from dpll import *


"""
    Ejecuta el algoritmo especificado para resolver una expresión lógica booleana.

    Parámetros:
    - regex: Una cadena que representa la expresión lógica en notación infija.
    - algoritm: Una cadena que indica el algoritmo a utilizar.

    Retorna:
    - result: Un booleano que indica si la expresión es satisfactible (True) o no (False).
    - asignacion: Un diccionario que contiene la asignación de variables que satisface la expresión.
    """

def Ejecute_Algoritm(regex, algoritm):
   rt = infix_to_Postfix(regex)
   valor = Parser(rt)
   convert = convertTo_Ceros(valor)
   parseToNumber(convert, valor)
   if algoritm == 'Fuerza Bruta':
      result, asignacion = fuerzaBruta(convert)
   elif algoritm == 'DPL':
      asignacion_inicial = {}
      result, asignacion = dpll(valor, asignacion_inicial)
   return result, asignacion
