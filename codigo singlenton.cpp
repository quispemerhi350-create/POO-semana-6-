1 #include <iostream>
2 using namespace std;
3
4 // Clase que representa la configuraci n del sistema
5 class Config {
6 private:
7 // nica instancia de la clase (est tica, pertenece a la clase, no a los objetos)
8 static Config* instancia;
9
10 // Constructor PRIVADO: no se puede crear objetos desde fuera
11 Config() {
12 cout << "Configuraci n cargada por primera vez.\n";
13 }
14
15 public:
16 // M todo para obtener la nica instancia
17 static Config* obtenerInstancia() {
18 // Si no existe, la creamos
19 if (!instancia) {
20 instancia = new Config();
21 }
22 // Siempre devolvemos la misma direcci n de memoria
23 return instancia;
24 }
25
26 // M todo de ejemplo
27 void mostrarMensaje() {
28 cout << "Bienvenido al sistema global.\n";
29 }
30 };
31
32 // Inicializamos el puntero est tico en nulo
33 Config* Config::instancia = nullptr;
34
35 int main() {
36 // Intentamos crear dos "objetos"
37 Config* conf1 = Config::obtenerInstancia();
38 Config* conf2 = Config::obtenerInstancia();
39
40 conf1->mostrarMensaje();
41
42 // Comprobamos si son el mismo objeto (misma direcci n de memoria)
43 cout << " Son la misma instancia?-> " << (conf1 == conf2 ? "S " : "NO") << endl;
44
45 return 0;
46 }
