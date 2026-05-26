# Objeto final que queremos construir
class ComboComida:
def __init__(self):
self.hamburguesa = None
self.bebida = None
self.papas = None

# Para ver el resultado final
def __str__(self):
return f"Combo: {self.hamburguesa}, {self.bebida}, {self.papas}"

# Constructor: arma el combo paso a paso
class ConstructorCombo:
def __init__(self):
# Iniciamos un combo vac o
self.combo = ComboComida()

# M todos para agregar partes (retornamos self para encadenar)
def agregar_hamburguesa(self, tipo):
self.combo.hamburguesa = tipo
return self # Permite encadenar llamadas

def agregar_bebida(self, nombre):
self.combo.bebida = nombre
return self

def agregar_papas(self, tamano):
self.combo.papas = tamano
return self

# Devuelve el objeto terminado
def construir(self):
return self.combo

#---PRUEBA DEL C DIGO--
if __name__ == "__main__":
# Creamos un combo paso a paso o todo junto
combo1 = ConstructorCombo()\
.agregar_hamburguesa("Doble queso")\
.agregar_bebida("Gaseosa 500ml")\
.agregar_papas("Grandes")\
.construir()

print(combo1)

# Otro combo diferente
combo2 = ConstructorCombo()\
.agregar_hamburguesa("Pollo")\
.agregar_bebida("Agua")\
.agregar_papas("Peque as")\
.construir()

print(combo2)
