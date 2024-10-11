# 1. **\( \ln\left(\frac{x}{x+1}\right) \)**
**Derivada**
\[
   \frac{(x + 1) \left( -\frac{x}{(x + 1)^2} + \frac{1}{x + 1} \right)}{x}
\]

**Conceptos clave**:
- **Regla del logaritmo**: 
  \[
  \ln\left(\frac{a}{b}\right) = \ln(a) - \ln(b)
  \]
- **Regla del cociente**: Para derivar la función interna \(\frac{x}{x+1}\).
- **Regla de la cadena**: Para derivar \( \ln(u) \).

# 2. **\( \sin(e^{3x}) \)**
**Derivada**
\[
   3e^{3x}\cos(e^{3x})
\]

**Conceptos clave**:
- **Derivada de \( \sin(x) \)**.
- **Regla de la cadena**: Para derivar \( \sin(f(x)) \), donde \( f(x) = e^{3x} \).
- **Derivada de \( e^x \)** y la regla de la cadena para la exponencial.

# 3. **\( \ln\left(\sin\left(\frac{x+1}{x}\right)\right) \)**
**Derivada**
\[
\left(\frac{1}{x} - \frac{x + 1}{x^2}\right) \frac{\cos\left(\frac{x + 1}{x}\right)}{\sin\left(\frac{x + 1}{x}\right)}
\]

**Conceptos clave**:
- **Regla del logaritmo**: Para derivar \( \ln(f(x)) \).
- **Derivada de \( \sin(x) \)**.
- **Regla de la cadena**: Para manejar \( \sin(f(x)) \).
- **Regla del cociente**: Para derivar \(\frac{x+1}{x}\).

# 4. **\( \frac{x^5 + x^3}{x^2 + 1} \)**
**Derivada**
\[
-\frac{2x(x^5 + x^3)}{(x^2 + 1)^2} + \frac{5x^4 + 3x^2}{x^2 + 1}
\]

**Conceptos clave**:
- **Regla del cociente**: Para derivar \( \frac{u}{v} \).
- **Derivadas de potencias**: Para \( u = x^5 + x^3 \) y \( v = x^2 + 1 \).

# 5. **\( \arctan((x^2 + 1)^{10}) \)**
**Derivada**
\[
\frac{20x}{(x^2 + 1)^{20} + 1}
\]

**Conceptos clave**:
- **Derivada de \( \arctan(x) \)**.
- **Regla de la cadena**: Para manejar \( \arctan(f(x)) \) y \( f(x) = (x^2 + 1)^{10} \).
- **Derivada de potencias**: Para derivar \((x^2 + 1)^{10}\).

# Resumen de conceptos aplicados

1. **Logaritmos**:
   - Regla del logaritmo (para derivar logaritmos).
2. **Funciones trigonométricas**:
   - Derivadas de \( \sin \), \( \cos \), \( \tan \) y sus inversas.
3. **Exponenciales**:
   - Derivada de \( e^x \) y potencias.
4. **Regla del producto y cociente**:
   - Usadas para funciones que son productos o cocientes de otras funciones.
5. **Regla de la cadena**:
   - Para funciones compuestas (funciones dentro de funciones).


# Comandos
Ejecutar SWI-Prolog:

```bash
swipl
```

Cargar el Archivo en SWI-Prolog:
```bash
[nombre_del_archivo].
```


