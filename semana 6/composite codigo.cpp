// ============================================================
// COMPOSITE: permite tratar objetos individuales y grupos de
// objetos de la misma manera.
// Ejemplo clásico: sistema de archivos donde una CARPETA puede
// contener ARCHIVOS y otras CARPETAS, pero todos responden
// al mismo método mostrar().
//
// Componentes del patrón:
//   1. Componente (clase base virtual)
//   2. Hoja (elemento simple: Archivo)
//   3. Composite (contenedor: Carpeta)
// ============================================================

#include <iostream>
#include <vector>
#include <string>
using namespace std;

// --- 1. COMPONENTE BASE: interfaz común para archivos y carpetas ---
class Componente {
public:
    string nombre;
    Componente(string n) : nombre(n) {}

    // Método virtual: cada clase lo implementa a su manera
    virtual void mostrar(int nivel = 0) = 0;

    virtual ~Componente() {}
};

// Función auxiliar: imprime espacios para simular indentación
void indentar(int nivel) {
    for (int i = 0; i < nivel * 3; i++) cout << " ";
}

// --- 2. HOJA: un archivo simple (no tiene hijos) ---
class Archivo : public Componente {
    string extension;
public:
    Archivo(string nombre, string ext) : Componente(nombre), extension(ext) {}

    // Un archivo solo se muestra a sí mismo
    void mostrar(int nivel = 0) override {
        indentar(nivel);
        cout << "[ ] " << nombre << "." << extension << "\n";
    }
};

// --- 3. COMPOSITE: una carpeta que puede contener hijos ---
class Carpeta : public Componente {
    vector<Componente*> hijos; // Puede contener archivos o carpetas
public:
    Carpeta(string nombre) : Componente(nombre) {}

    // Agregar un hijo (archivo o carpeta)
    void agregar(Componente* c) {
        hijos.push_back(c);
    }

    // Muestra la carpeta y luego llama recursivamente a sus hijos
    void mostrar(int nivel = 0) override {
        indentar(nivel);
        cout << "[+] " << nombre << "/\n";

        // Recursión: cada hijo se muestra con un nivel más de indentación
        for (Componente* hijo : hijos) {
            hijo->mostrar(nivel + 1);
        }
    }

    ~Carpeta() {
        for (Componente* hijo : hijos) delete hijo;
    }
};

int main() {
    cout << "=== Patrón Composite – Sistema de Archivos ===\n\n";

    // Estructura jerárquica:
    // Proyecto/
    //   src/
    //     main.cpp
    //     config.h
    //   docs/
    //     manual.pdf
    //     diagrama.png
    //   readme.txt

    Carpeta* proyecto = new Carpeta("Proyecto");

    Carpeta* src = new Carpeta("src");
    src->agregar(new Archivo("main",    "cpp"));
    src->agregar(new Archivo("config",  "h"));
    src->agregar(new Archivo("utils",   "cpp"));

    Carpeta* docs = new Carpeta("docs");
    docs->agregar(new Archivo("manual",   "pdf"));
    docs->agregar(new Archivo("diagrama", "png"));

    Carpeta* tests = new Carpeta("tests");
    tests->agregar(new Archivo("test_main", "cpp"));

    proyecto->agregar(src);
    proyecto->agregar(docs);
    proyecto->agregar(tests);
    proyecto->agregar(new Archivo("readme", "txt"));
    proyecto->agregar(new Archivo("makefile", "mk"));

    // Mostrar toda la jerarquía con un solo método
    proyecto->mostrar();

    cout << "\n--- Mostrando solo la subcarpeta 'src' ---\n";
    src->mostrar();

    delete proyecto;
    return 0;
}
