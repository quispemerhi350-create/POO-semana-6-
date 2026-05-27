# ============================================================
# COMMAND: encapsula una operación como un objeto independiente.
# Ventajas:
#   - Se puede guardar un historial de operaciones
#   - Se puede implementar DESHACER (undo) y REHACER (redo)
#   - Se pueden encolar operaciones para ejecutar después
#
# Ejemplo: editor de texto con guardar y deshacer.
# ============================================================

# --- El RECEPTOR: el editor de texto real ---
class EditorTexto:
    def __init__(self):
        self.contenido = ""

    def escribir(self, texto):
        """Agrega texto al documento."""
        self.contenido += texto
        print(f"  [Editor] Escrito: '{texto}'")
        print(f"  [Editor] Contenido actual: '{self.contenido}'")

    def borrar_ultimo(self, cantidad):
        """Borra los últimos N caracteres."""
        self.contenido = self.contenido[:-cantidad]
        print(f"  [Editor] Borrados {cantidad} caracteres")
        print(f"  [Editor] Contenido actual: '{self.contenido}'")

    def guardar(self, nombre_archivo):
        """Simula guardar el archivo."""
        print(f"  [Editor] Guardado como '{nombre_archivo}.txt'")
        print(f"  [Editor] Contenido guardado: '{self.contenido}'")

    def mostrar(self):
        print(f"  [Editor] Contenido: '{self.contenido}'")


# --- Clase BASE del comando ---
class Comando:
    def ejecutar(self):
        raise NotImplementedError
    def deshacer(self):
        raise NotImplementedError


# --- COMANDO 1: Escribir texto ---
class ComandoEscribir(Comando):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto  = texto

    def ejecutar(self):
        self.editor.escribir(self.texto)

    def deshacer(self):
        # Deshacer = borrar los caracteres que escribimos
        self.editor.borrar_ultimo(len(self.texto))


# --- COMANDO 2: Guardar archivo ---
class ComandoGuardar(Comando):
    def __init__(self, editor, nombre):
        self.editor = editor
        self.nombre = nombre

    def ejecutar(self):
        self.editor.guardar(self.nombre)

    def deshacer(self):
        # Guardar no se puede deshacer de verdad (simplificación)
        print(f"  [Undo] No se puede deshacer el guardado de '{self.nombre}'")


# --- INVOCADOR: ejecuta comandos y guarda historial ---
class Invocador:
    def __init__(self):
        self.historial = []  # Pila de comandos ejecutados

    def ejecutar(self, comando):
        """Ejecuta un comando y lo guarda en el historial."""
        comando.ejecutar()
        self.historial.append(comando)

    def deshacer(self):
        """Deshace el ÚLTIMO comando ejecutado (LIFO: último en entrar, primero en salir)."""
        if not self.historial:
            print("  [Undo] No hay comandos para deshacer.")
            return
        ultimo = self.historial.pop()  # Saca el último de la pila
        print(f"  [Undo] Deshaciendo: {type(ultimo).__name__}")
        ultimo.deshacer()

    def ver_historial(self):
        print(f"  Historial ({len(self.historial)} comandos):")
        for cmd in self.historial:
            print(f"    - {type(cmd).__name__}")


# ============================================================
# Programa principal
# ============================================================
print("=== Patrón Command – Editor de Texto ===\n")

editor    = EditorTexto()
invocador = Invocador()

print("-- Escribiendo texto --")
invocador.ejecutar(ComandoEscribir(editor, "Hola, "))
invocador.ejecutar(ComandoEscribir(editor, "mundo"))
invocador.ejecutar(ComandoEscribir(editor, "!"))

print("\n-- Guardando --")
invocador.ejecutar(ComandoGuardar(editor, "mi_documento"))

print("\n-- Historial de comandos --")
invocador.ver_historial()

print("\n-- Deshaciendo (undo) 2 veces --")
invocador.deshacer()   # Deshace el "!"
invocador.deshacer()   # Deshace "mundo"

print("\n-- Estado después de deshacer --")
editor.mostrar()
