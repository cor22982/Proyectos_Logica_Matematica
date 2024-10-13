% Hecho para poder utilizar el símbolo x y funciones
x.
funcion_trigonometrica(sin).
funcion_trigonometrica(cos).
funcion_trigonometrica(tan).

funcion_inversa_trigonometrica(arctan).

funcion_exponencial(exp).
funcion_logaritmica(ln).

% Derivada de un producto cuando A es un número y B es una variable
derivada(A*B, Y) :-
    number(A),
    derivada(B, Bprima),
    Y = A * Bprima.

% Derivada de un producto cuando B es un número y A es una variable
derivada(A*B, Y) :-
    number(B),
    derivada(A, Aprima),
    Y = B * Aprima.

% Derivada de un producto - Regla del producto
derivada(A*B, Y) :-
    derivada(A, Aprima),
    derivada(B, Bprima),
    Y = Aprima*B + A*Bprima.

% Derivada de una división - Regla del cociente
derivada(A/B, Y) :-
    derivada(A, Aprima),
    derivada(B, Bprima),
    Y = (Aprima*B - A*Bprima) / (B^2).

% Derivada de funciones compuestas - Regla de la cadena
derivada(F(G), Y) :-
    (funcion_trigonometrica(F); 
     funcion_inversa_trigonometrica(F); 
     funcion_exponencial(F); 
     funcion_logaritmica(F)),   % Verifica si F está entre las funciones definidas
    derivada(G, Gprima),
    derivada(F(G), Fprima),
    Y = Fprima * Gprima.

% Derivada Seno
derivada(sin(X), Y) :-
    derivada(X, Y1),
    Y = cos(X) * Y1.

% Derivada Coseno
derivada(cos(X), Y) :-
    derivada(X, Y1),
    Y = -sin(X) * Y1.

% Derivada Tangente
derivada(tan(X), Y) :-
    derivada(X, Y1),
    Y = (1 + tan(X)^2) * Y1.

% Derivada ArcoTangente
derivada(arctan(X), Y) :-
    derivada(X, Y1),
    Y = Y1 / (1 + X^2).

% Derivada Exponencial
derivada(exp(X), Y) :-
    derivada(X, Y1),
    Y = exp(X) * Y1.

% Derivada Logaritmo Natural
derivada(ln(X), Y) :-
    derivada(X, Xprima),
    Y = Xprima / X.

% Regla general para derivar un polinomio con múltiples términos
derivada(Terminos, Y) :- 
    Terminos =.. [Op | T],  % Separar los términos por el operador (+ o -)
    ( Op = (+) ; Op = (-) ),  % Asegurarse de que el operador sea válido (suma o resta)
    maplist(derivada, T, Y1),
    Y =.. [Op | Y1].

% Derivadas de polinomios con exponente positivos, negativos, cero
derivada(X^E, Y) :-
    ( E > 0 ->  % Caso de exponentes positivos
        Coef is E,
        E1 is E - 1,
        Y = (Coef * (X^E1))
    ; E < 0 ->  % Caso de exponentes negativos
        PosE is -E,
        E1 is PosE + 1,
        Coef is PosE,
        Y = -(Coef * (X^(-E1)))
    ; E = 0 ->  % Derivada de constante
        Y = 0
    ).

% Derivada de X^1 (caso especial)
derivada(x^1, 1).
derivada(x, 1).

% Derivada de una constante (número)
derivada(C, 0) :- number(C).
