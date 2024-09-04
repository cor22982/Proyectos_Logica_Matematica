
"""
Integrantes:
• Gustavo Adolfo Cruz Bardales - 22779
• Javier Andrés Chen González - 22153
• Josué Emanuel Say Garcia - 22801
• Pedro Pablo Guzmán Mayén - 22111
• Mathew Alexander Cordero Aquino - 22982
• Sebastián Estrada Tuch - 21405

"""

class Stack:
    """ Inicia una pila vacía"""
    def __init__(self):
        self.stack = []
    """ Agrega un elemento al tope de la pila"""
    def push(self, item):
        self.stack.append(item)
    """ Remueve y retorna el elemento al topa de la pila"""
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")
    """ Retorna el elemento al tope de la pila sin removerlo"""
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from empty stack")
    """ Revisa si la pila está vacía, retorna 0 si se cumple"""
    def is_empty(self):
        return len(self.stack) == 0
    """ Retorna el numero de elementos en la pila"""
    def size(self):
        return len(self.stack)
    """ Retorna la pila como una cadena (string)"""
    def __str__(self):
        return str(self.stack)
