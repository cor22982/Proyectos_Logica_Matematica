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
      stack.append(top2)
      stack.append(top1)
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

def parseToNumber(valor):
  for i in range(len(valor)):
    for j in range(len(valor[i])):
      if valor[i][j] == 'p':
        valor[i][j] = 1
      elif valor[i][j] == 'q':
        valor[i][j] = 2
      elif valor[i][j] == 'r':
        valor[i][j] = 3
      elif valor[i][j] == 's':
        valor[i][j] = 4
  return valor

def parseToString(valor):
  return {
    'p': valor.get(1), 
    'q': valor.get(2), 
    'r': valor.get(3), 
    's': valor.get(4)
  }


regex = '(p ∨ q) ∧ (q ∨ s) ∧ (p ∨ s) ∧ (q ∨ s) '
rt = infix_to_Postfix(regex)
valor = Parser(rt)
print(valor)

result, asignacion = fuerzaBruta(parseToNumber(valor))

if result:
    print("La expresión es satisfacible")
    print(parseToString(asignacion))
else:
    print("La expresión no es satisfacible")