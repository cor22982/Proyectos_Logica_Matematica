% hecho para poder utilizar el simbolo x
x.

% Regla para derivar potencias
derivada(X^E, Y) :-
    E \= 0,  % E que no sea cero
    Y = Coef * X^E1,  % Definir la derivada
    Coef is E,  % El coeficiente es el exponente E
    E1 is E - 1.  % Reducir el exponente en 1

% Regla para manejar la derivada de una constante (E = 0)
derivada(X^0, 0).

% Regla para derivar un polinomio (suma de términos)
derivada(T1 + T2, Y) :-   % Y es la derivada de T1 + T2
    derivada(T1, Y1),     % Derivada del primer término
    derivada(T2, Y2),     % Derivada del segundo término
    Y = Y1 + Y2.          % Sumar las derivadas

% Regla para derivar un polinomio con multiples terminos
derivada(Terminos, Y) :- 
    Terminos =.. [ + | T], % Separar los términos por suma
    maplist(derivada, T, Y1), % Derivar cada término
    Y =.. [ + | Y1]. % Reunir las derivadas de nuevo en una suma

% Regla para manejar exponentes negativos
derivada(X^-E, Y) :-  % E es positivo
    E > 0,  % Asegurar que E sea positivo
    Y = -Coef * X^(-E1),  % Definir la derivada
    Coef is E,  % El coeficiente es el exponente E
    E1 is E + 1.  % Aumentar el exponente en 1

% Regla para derivar términos constantes
derivada(C, 0) :- number(C).  % C es una constante
