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

regex = '(p ∨ r ∨ s) ∧ (q ∨ p ∨ s)'

print(infix_to_Postfix(regex))