# ============================================================
# DECORATOR: añade funcionalidad extra a una función/objeto
# SIN modificar su código original.
# En Python se usa con la sintaxis @nombre_decorador.
#
# Ejemplo: añadir validación a funciones matemáticas
# (verificar que los argumentos sean válidos antes de calcular)
# ============================================================

# --- Decorador 1: valida que los argumentos sean números ---
def validar_numeros(func):
    """Verifica que todos los argumentos sean int o float."""
    def envoltura(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Se esperaba número, se recibió: {type(arg).__name__}")
        print(f"  [Validador] Argumentos válidos: {args}")
        return func(*args, **kwargs)
    return envoltura


# --- Decorador 2: verifica que no haya división por cero ---
def sin_division_cero(func):
    """Previene divisiones por cero antes de ejecutar la función."""
    def envoltura(a, b, *args, **kwargs):
        if b == 0:
            raise ZeroDivisionError("El divisor no puede ser cero")
        return func(a, b, *args, **kwargs)
    return envoltura


# --- Decorador 3: muestra log de la operación ---
def log_operacion(func):
    """Registra qué función se ejecutó y con qué resultado."""
    def envoltura(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"  [LOG] {func.__name__}({', '.join(str(a) for a in args)}) = {resultado}")
        return resultado
    return envoltura


# ============================================================
# Funciones matemáticas decoradas
# ============================================================

@log_operacion
@validar_numeros
def sumar(a, b):
    """Suma dos números."""
    return a + b

@log_operacion
@validar_numeros
def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

@log_operacion
@sin_division_cero
@validar_numeros
def dividir(a, b):
    """Divide a entre b, con protección contra división por cero."""
    return a / b

@log_operacion
@validar_numeros
def potencia(base, exponente):
    """Calcula base elevada al exponente."""
    return base ** exponente


# ============================================================
# Programa principal
# ============================================================
print("=== Patrón Decorator – Validación Matemática ===\n")

print("-- Suma --")
sumar(10, 5)

print("\n-- Multiplicación --")
multiplicar(7, 8)

print("\n-- División válida --")
dividir(20, 4)

print("\n-- División por cero (capturada por decorador) --")
try:
    dividir(10, 0)
except ZeroDivisionError as e:
    print(f"  Error capturado: {e}")

print("\n-- Potencia --")
potencia(2, 10)

print("\n-- Argumento inválido (string en lugar de número) --")
try:
    sumar("hola", 5)
except TypeError as e:
    print(f"  Error capturado: {e}")
