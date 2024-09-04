
"""
Integrantes:
• Gustavo Adolfo Cruz Bardales - 22779
• Javier Andrés Chen González - 22153
• Josué Emanuel Say Garcia - 22801
• Pedro Pablo Guzmán Mayén - 22111
• Mathew Alexander Cordero Aquino - 22982
• Sebastián Estrada Tuch - 21405

"""
from Stack import Stack

def getPrecedence (c):
    """
    Retorna la precedencia del operador
    """
  precedencias = {
    '(': 1,
    '∨': 2,
    '∧': 3,
    '¬': 4,
    
  }
  return precedencias.get(c, 6)

def deletespaces(regext):
    """
    Elimina los espacios en blanco de la expresión lógica
    """
  regex = ""
  for i in regext:
    if i != ' ':
      regex+= i
  return regex

def infix_to_Postfix (regex):
    """
    Convierte la expresión de infix a postfix
    """
  postfix = ""
  stack = Stack()
  regex = deletespaces(regex)
  for c in regex:
    if c.isalnum():
      postfix += c
    elif c == '(':
      stack.push(c)
    elif c == ')':
      while stack.peek() != '(':
        top = stack.pop()
        postfix += top
      stack.pop() 
    else:
      while stack.size() > 0 and getPrecedence(stack.peek()) >= getPrecedence(c):
        top = stack.pop()
        postfix += top
      stack.push(c)

  while stack.size() > 0:
    top = stack.pop()
    postfix += top
  
  return postfix


def Parser(regex):
    """
    Parsea la expresión postfija y organiza los operadores y operandos en una pila
    """
  stack  = []
  for i in regex:
    if i.isalnum() and i != '∨':
      stack.append(i)
    elif i == '¬':
      top = stack.pop()
      stack.append(f'{i}{top}')
    elif i == '∨':
      top1 = stack.pop()
      top2 = stack.pop()
      if isinstance(top2, list):
        top2.append(top1)
        stack.append(top2)
      else:
        stack2 = [top2,top1]
        stack.append(stack2)
    elif i == '∧':
      top1 = stack.pop()
      top2 = stack.pop()
      if isinstance(top1, list):
         stack3 = top1
      else:
        stack3 = [top1]   
      if isinstance(top2, list):
         stack2 = top2
      else:
         stack2 = [top2]
      stack.append(stack2)
      stack.append(stack3)
  return stack

def fuerzaBruta(expresion):
    """
    Evalúa una expresión lógica utilizando el algoritmo de fuerza bruta.
    Prueba todas las posibles asignaciones de valores de verdad a las variables.
    """
    variables = [1, 2, 3, 4]  

    for i in range(2 ** len(variables)):
        asignacion = {}
        for j, var in enumerate(variables):
            asignacion[var] = (i & (1 << j)) != 0

        satisfacible = True
        for clausula in expresion:
            clausula_verdadera = False
            for literal in clausula:
                if literal > 0 and asignacion[literal]:
                    clausula_verdadera = True 
                    break
                elif literal < 0 and not asignacion[-literal]:
                    clausula_verdadera = True
                    break
            if not clausula_verdadera:
                satisfacible = False
                break

        if satisfacible:
            return True, asignacion
    return False, None


valor_String = {
   'p': 1,
   'q': 2,
   'r': 3,
   's': 4,
   '¬p': -1,
   '¬q': -2,
   '¬r': -3,
   '¬s': -4,
}

def convertTo_Ceros(valor):
    """
    Convierte una lista de expresiones en una lista de ceros inicialización de matriz.
    """
    lista = []
    for i in range(len(valor)):
        fila = []
        for j in range(len(valor[i])):
            fila.append(0)
        lista.append(fila)
    return lista

def parseToString(valor):
  return {
    'p': valor.get(1), 
    'q': valor.get(2), 
    'r': valor.get(3), 
    's': valor.get(4)
  }

def parseToNumber(list_numbers, list_expresion):
   for i in range (len(list_expresion)):
      for j in range (len(list_expresion[i])):
         list_numbers[i][j] = valor_String[list_expresion[i][j]]
         
         
