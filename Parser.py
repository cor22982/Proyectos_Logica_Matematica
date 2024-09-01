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


regex = '(p ∨ q) ∧ (q ∨ s) ∧ (p ∨ s) ∧ (q ∨ s) '
rt = infix_to_Postfix(regex)
valor = Parser(rt)
print(valor)