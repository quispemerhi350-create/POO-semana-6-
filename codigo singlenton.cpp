#include <iostream>
using namespace std;

// Clase que representa la configuraci n del sistema
class Config {
private:
// nica instancia de la clase (est tica, pertenece a la clase, no a los objetos)
static Config* instancia;

// Constructor PRIVADO: no se puede crear objetos desde fuera
Config() {
cout << "Configuraci n cargada por primera vez.\n";
}

public:
// M todo para obtener la nica instancia
static Config* obtenerInstancia() {
// Si no existe, la creamos
if (!instancia) {
instancia = new Config();
}
// Siempre devolvemos la misma direcci n de memoria
return instancia;
}

// M todo de ejemplo
void mostrarMensaje() {
cout << "Bienvenido al sistema global.\n";
}
};

// Inicializamos el puntero est tico en nulo
Config* Config::instancia = nullptr;

int main() {
// Intentamos crear dos "objetos"
Config* conf1 = Config::obtenerInstancia();
Config* conf2 = Config::obtenerInstancia();

conf1->mostrarMensaje();

// Comprobamos si son el mismo objeto (misma direcci n de memoria)
cout << " Son la misma instancia?-> " << (conf1 == conf2 ? "S " : "NO") << endl;

return 0;
}
