from Parser import *
from dpll import *
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