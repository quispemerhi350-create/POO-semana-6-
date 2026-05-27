// ============================================================
// STRATEGY: permite seleccionar un algoritmo en tiempo de
// ejecución sin cambiar el código que lo usa.
// El Contexto delega el trabajo a la estrategia activa.
//
// Ejemplo: elegir entre diferentes algoritmos de ordenamiento
//   - Burbuja (simple pero lento)
//   - Selección (intermedio)
//   - Inserción (eficiente para listas casi ordenadas)
// ============================================================

#include <iostream>
#include <vector>
#include <algorithm> // Para swap
using namespace std;

// Función auxiliar para imprimir un vector
void imprimir(const vector<int>& v, const string& etiqueta) {
    cout << etiqueta << ": [ ";
    for (int x : v) cout << x << " ";
    cout << "]\n";
}

// --- ESTRATEGIA BASE (interfaz abstracta) ---
class EstrategiaOrdenamiento {
public:
    // Método virtual que implementa cada estrategia concreta
    virtual void ordenar(vector<int>& datos) = 0;
    virtual string nombre() = 0;
    virtual ~EstrategiaOrdenamiento() {}
};

// --- ESTRATEGIA 1: Burbuja ---
// Compara pares adyacentes y los intercambia si están en mal orden
class OrdenamientoBurbuja : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        int n = datos.size();
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (datos[j] > datos[j + 1]) {
                    swap(datos[j], datos[j + 1]); // Intercambia
                }
            }
        }
    }
    string nombre() override { return "Burbuja"; }
};

// --- ESTRATEGIA 2: Selección ---
// Encuentra el mínimo y lo coloca al inicio en cada pasada
class OrdenamientoSeleccion : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        int n = datos.size();
        for (int i = 0; i < n - 1; i++) {
            int minIdx = i;
            for (int j = i + 1; j < n; j++) {
                if (datos[j] < datos[minIdx]) minIdx = j;
            }
            swap(datos[i], datos[minIdx]); // Pone el mínimo en su lugar
        }
    }
    string nombre() override { return "Seleccion"; }
};

// --- ESTRATEGIA 3: Inserción ---
// Toma cada elemento y lo inserta en su posición correcta
class OrdenamientoInsercion : public EstrategiaOrdenamiento {
public:
    void ordenar(vector<int>& datos) override {
        int n = datos.size();
        for (int i = 1; i < n; i++) {
            int clave = datos[i];
            int j = i - 1;
            // Mueve los elementos mayores una posición a la derecha
            while (j >= 0 && datos[j] > clave) {
                datos[j + 1] = datos[j];
                j--;
            }
            datos[j + 1] = clave;
        }
    }
    string nombre() override { return "Insercion"; }
};

// --- CONTEXTO: usa cualquier estrategia de ordenamiento ---
class Ordenador {
    EstrategiaOrdenamiento* estrategia; // Puntero a la estrategia activa
public:
    Ordenador(EstrategiaOrdenamiento* e) : estrategia(e) {}

    // Cambiar estrategia en tiempo de ejecución
    void setEstrategia(EstrategiaOrdenamiento* e) {
        estrategia = e;
    }

    // Ordena usando la estrategia activa
    void ejecutar(vector<int>& datos) {
        cout << "Usando estrategia: " << estrategia->nombre() << "\n";
        imprimir(datos, "  Antes");
        estrategia->ordenar(datos);
        imprimir(datos, "  Despues");
    }
};

int main() {
    cout << "=== Patrón Strategy – Ordenamiento ===\n\n";

    vector<int> datos1 = {64, 34, 25, 12, 22, 11, 90};
    vector<int> datos2 = {5, 3, 8, 1, 9, 2, 7};
    vector<int> datos3 = {15, 7, 3, 19, 4, 11};

    // Instanciamos las estrategias
    OrdenamientoBurbuja   burbuja;
    OrdenamientoSeleccion seleccion;
    OrdenamientoInsercion insercion;

    // Creamos el contexto con burbuja
    Ordenador ordenador(&burbuja);
    ordenador.ejecutar(datos1);

    cout << "\n";

    // Cambiamos estrategia en tiempo de ejecución → selección
    ordenador.setEstrategia(&seleccion);
    ordenador.ejecutar(datos2);

    cout << "\n";

    // Cambiamos de nuevo → inserción
    ordenador.setEstrategia(&insercion);
    ordenador.ejecutar(datos3);

    return 0;
}
