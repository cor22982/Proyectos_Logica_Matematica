% Hecho para poder utilizar el símbolo x
x.


% Regla general para derivar un polinomio con múltiples términos
derivada(Terminos, Y) :- 
    Terminos =.. [Op | T],  % Separar los términos por el operador (+ o -)
    ( Op = (+) ; Op = (-) ),  % Asegurarse de que el operador sea válido (suma o resta)
    maplist(derivada, T, Y1),  % Derivar cada término
    Y =.. [Op | Y1].  % Reunir las derivadas con el mismo operador

% Derivadas de polinomios con exponente positivos, negativos, cero
derivada(X^E, Y) :-
    ( E > 0 ->  % Caso de exponentes positivos
        Coef is E,
        E1 is E - 1,
        Y = (Coef * (X^E1))  % Derivada de X^E
    ; E < 0 ->  % Caso de exponentes negativos
        PosE is -E,
        E1 is PosE + 1,
        Coef is PosE,
        Y = -(Coef * (X^(-E1)))  % Derivada de X^(-E)
    ; E = 0 ->  % Derivada de constante
        Y = 0
    ).

% Derivada de X^1 (caso especial)
derivada(X^1, 1).

% Derivada de una constante (número)
derivada(C, 0) :- number(C).
