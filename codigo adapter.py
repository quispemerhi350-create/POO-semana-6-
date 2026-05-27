# ============================================================
# ADAPTER: convierte la interfaz de una clase en otra que el
# cliente espera. Es como un "traductor" entre dos sistemas
# incompatibles, sin modificar el código original.
#
# Ejemplo: sistema que trabaja en SOLES, pero tenemos un
# proveedor de pagos que solo habla en DÓLARES.
# ============================================================

# --- Sistema existente que trabaja en DÓLARES (no podemos modificarlo) ---
class PasarelaDolares:
    """Simula un sistema externo de pagos en USD (no lo modificamos)."""

    def pagar_usd(self, monto_usd):
        print(f"  [PasarelaDolares] Procesando pago de ${monto_usd:.2f} USD")
        return True


# --- Lo que nuestro sistema espera: pagos en SOLES ---
class SistemaSoles:
    """Interfaz que nuestro sistema local usa (trabaja en PEN)."""

    def pagar_soles(self, monto_soles):
        raise NotImplementedError("Implementar en subclase")


# --- El ADAPTADOR: traduce soles → dólares internamente ---
class AdaptadorPago(SistemaSoles):
    TIPO_CAMBIO = 3.75  # 1 USD = 3.75 PEN (aproximado)

    def __init__(self, pasarela_dolares):
        # Guardamos referencia al sistema externo
        self.pasarela = pasarela_dolares

    def pagar_soles(self, monto_soles):
        # Convertimos soles a dólares antes de llamar al sistema externo
        monto_usd = monto_soles / self.TIPO_CAMBIO
        print(f"  [Adaptador] S/ {monto_soles:.2f} → ${monto_usd:.2f} USD (TC: {self.TIPO_CAMBIO})")
        return self.pasarela.pagar_usd(monto_usd)


# ============================================================
# Programa principal
# ============================================================
print("=== Patrón Adapter – Conversión Soles/Dólares ===\n")

# El cliente solo conoce el sistema en soles
pasarela = PasarelaDolares()       # Sistema externo en dólares
adaptador = AdaptadorPago(pasarela) # El adaptador hace la traducción

# Pagos en soles (el cliente no sabe que internamente se usan dólares)
montos_soles = [150.00, 375.00, 562.50]

for monto in montos_soles:
    print(f"Pagando S/ {monto:.2f}:")
    resultado = adaptador.pagar_soles(monto)
    print(f"  Resultado: {'Exitoso' if resultado else 'Fallido'}\n")
