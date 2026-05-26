# Clase base o interfaz
class Transporte:
def entregar(self):
pass # M todo vac o, lo definir n las clases hijas

# Clases concretas (tipos de transporte)
class Camion(Transporte):
def entregar(self):
return "Entrega realizada por CARRETERA"

class Barco(Transporte):
def entregar(self):
return "Entrega realizada por MAR"

# F BRICA: Se encarga de crear el objeto correcto
class FabricaTransporte:
@staticmethod
def obtener_transporte(tipo):
# Seg n el tipo recibido, devolvemos el objeto necesario
if tipo.lower() == "camion":
return Camion()
elif tipo.lower() == "barco":
return Barco()
else:
raise ValueError("Tipo de transporte no v lido")

#---PRUEBA DEL C DIGO--
if __name__ == "__main__":
# Creamos transporte tipo Cami n
t1 = FabricaTransporte.obtener_transporte("camion")
print(t1.entregar())

# Creamos transporte tipo Barco
t2 = FabricaTransporte.obtener_transporte("barco")
print(t2.entregar())
