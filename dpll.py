
"""
Integrantes:
• Gustavo Adolfo Cruz Bardales - 22779
• Javier Andrés Chen González - 22153
• Josué Emanuel Say Garcia - 22801
• Pedro Pablo Guzmán Mayén - 22111
• Mathew Alexander Cordero Aquino - 22982
• Sebastián Estrada Tuch - 21405

"""

def selectLiteral(B):
    """
    Selecciona una literal para asignar en forma positiva.
    
    Parámetros:
    B (list of list): El conjunto de cláusulas.

    Retorna:
    str: Una literal seleccionada.
    """
    for clause in B:
        for literal in clause:
            return literal  # Devuelve la primera literal encontrada

def simplify(B, L):
    """
    Simplifica el conjunto de cláusulas dado una literal L.
    
    Parámetros:
    B (list of list): El conjunto de cláusulas.
    L (str): La literal a utilizar para simplificar el conjunto de cláusulas.

    Retorna:
    list: El conjunto de cláusulas simplificado B', o None si se encuentra una cláusula vacía.
    """
    B_prime = []
    for clause in B:
        if L in clause:
            # Elimina la cláusula que contiene L
            continue
        L_neg = '¬' + L if not L.startswith('¬') else L[1:]
        if L_neg in clause:
            # Elimina todas las ocurrencias de la literal complementaria de L
            new_clause = [lit for lit in clause if lit != L_neg]
            if not new_clause:
                # Si la cláusula queda vacía, la fórmula es insatisfacible
                return None  # Indica insatisfacción con None para señalar cláusula vacía
            B_prime.append(new_clause)
        else:
            B_prime.append(clause)
    return B_prime

def dpll(B, I):
    """
    Algoritmo DPLL para determinar la satisfacibilidad de una fórmula booleana en forma de cláusulas.

    Parámetros:
    B (list of list): Un conjunto de cláusulas (cada cláusula es una lista de literales) en forma de CNF.
    I (dict): Una asignación parcial de valores a variables.

    Retorna:
    bool, dict: Devuelve True y la asignación I si la fórmula es satisfacible, o False y una asignación vacía si no es satisfacible.
    """
    if not B:
        return True, I  # Fórmula satisfactoriamente vacía

    if any(not clause for clause in B):
        return False, {}  # Presencia de cláusula vacía

    L = selectLiteral(B)  # Selecciona una literal no asignada

    # Intento con L = True para I
    B_sub = simplify(B, L)
    if B_sub is not None:  # Solo continúa si no se encontró una cláusula vacía
        I_sub = I.copy()
        I_sub[L] = True
        result, I1 = dpll(B_sub, I_sub)
        if result:
            return True, I1
    
    # Intento con L = False para I
    L_neg = '¬' + L if not L.startswith('¬') else L[1:]
    B_sub_neg = simplify(B, L_neg)
    if B_sub_neg is not None:  # Solo continúa si no se encontró una cláusula vacía
        I_sub_neg = I.copy()
        I_sub_neg[L] = False
        result_neg, I2 = dpll(B_sub_neg, I_sub_neg)
        if result_neg:
            return True, I2

    return False, {}  # Si ambos intentos fallan, la fórmula es insatisfacible

def printResult(B, I):
    """
    Imprime el resultado del algoritmo DPLL para un conjunto de cláusulas y una asignación inicial.
    
    Parámetros:
    B (list of list): Un conjunto de cláusulas (cada cláusula es una lista de literales) en forma de CNF.
    I (dict): Una asignación inicial parcial de valores a variables.
    """
    resultado, asignacion = dpll(B, I)
    
    if resultado:
        print("La fórmula es satisfacible.")
        print("Asignación parcial que satisface la fórmula:")
        print(asignacion)
    else:
        print("La fórmula es insatisfacible.")

# Ejemplo de uso
clausulas = [['¬p', '¬q', '¬s'], ['¬q', '¬p', '¬s']]  # Conjunto de cláusulas con letras usando listas
asignacion_inicial = {}  # Asignación inicial vacía

printResult(clausulas, asignacion_inicial)
