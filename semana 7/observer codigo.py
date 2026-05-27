# ============================================================
# OBSERVER: cuando un objeto (Sujeto) cambia su estado,
# notifica automáticamente a todos los objetos registrados
# (Observadores) que dependen de él.
#
# Ejemplo: sistema de notificaciones de un CHAT.
# Cuando se envía un mensaje al chat, todos los usuarios
# conectados lo reciben automáticamente.
# ============================================================

# --- Clase OBSERVADOR: representa un usuario del chat ---
class UsuarioChat:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes_recibidos = []  # Historial de mensajes

    def actualizar(self, mensaje, remitente):
        """Este método es llamado automáticamente cuando hay un nuevo mensaje."""
        notificacion = f"[{remitente} → {self.nombre}]: {mensaje}"
        self.mensajes_recibidos.append(notificacion)
        print(f"   {self.nombre} recibió: \"{mensaje}\" (de {remitente})")

    def ver_historial(self):
        print(f"\n  Historial de {self.nombre}:")
        for msg in self.mensajes_recibidos:
            print(f"    - {msg}")


# --- Clase SUJETO: el canal del chat que gestiona observadores ---
class CanalChat:
    def __init__(self, nombre_canal):
        self.nombre = nombre_canal
        self._observadores = []  # Lista de usuarios conectados

    def conectar(self, usuario):
        """Registra un usuario en el canal."""
        self._observadores.append(usuario)
        print(f"   {usuario.nombre} se conectó a #{self.nombre}")

    def desconectar(self, usuario):
        """Elimina un usuario del canal."""
        self._observadores.remove(usuario)
        print(f"   {usuario.nombre} se desconectó de #{self.nombre}")

    def enviar_mensaje(self, mensaje, remitente_nombre):
        """Notifica a TODOS los usuarios conectados (excepto al remitente)."""
        print(f"\n   [{remitente_nombre}] dice: \"{mensaje}\"")
        for usuario in self._observadores:
            # No notificamos al propio remitente
            if usuario.nombre != remitente_nombre:
                usuario.actualizar(mensaje, remitente_nombre)


# ============================================================
# Programa principal
# ============================================================
print("=== Patrón Observer – Sistema de Chat ===\n")

# Crear canal
canal = CanalChat("general")

# Crear usuarios
ana   = UsuarioChat("Ana")
bob   = UsuarioChat("Bob")
carlos = UsuarioChat("Carlos")

# Conectar usuarios al canal
print("-- Conexiones --")
canal.conectar(ana)
canal.conectar(bob)
canal.conectar(carlos)

# Enviar mensajes
print("\n-- Mensajes --")
canal.enviar_mensaje("Hola a todos!", "Ana")
canal.enviar_mensaje("Buenas! Todo bien?", "Bob")

# Carlos se desconecta
print("\n-- Carlos se desconecta --")
canal.desconectar(carlos)

canal.enviar_mensaje("Carlos ya no vera este mensaje", "Ana")

# Ver historial de Bob
print()
bob.ver_historial()
