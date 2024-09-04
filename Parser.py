from Stack import Stack
def getPrecedence (c):
  precedencias = {
    '(': 1,
    '∨': 2,
    '∧': 3,
    '¬': 4,
    
  }
  return precedencias.get(c, 6)

def deletespaces(regext):
  regex = ""
  for i in regext:
    if i != ' ':
      regex+= i
  return regex

def infix_to_Postfix (regex):
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
         
         
