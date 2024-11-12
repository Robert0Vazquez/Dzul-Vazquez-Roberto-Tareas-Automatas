import csv

class automataFD:
    def __init__(self, archivo_csv):
        """Inicializar el DFSM leyendo los datos desde un archivo CSV"""
        self.Q, self.SIGMA, self.DELTA, self.START_STATE, self.ACCEPT_STATES = self.leer_csv(archivo_csv)
        self.EstadoActual = None

    def leer_csv(self, archivo_csv):
        """Leer el archivo CSV y obtener los estados, alfabeto, transiciones, estado inicial y final"""
        Q = []
        SIGMA = []
        DELTA = {}
        START_STATE = None
        ACCEPT_STATES = []

        with open(archivo_csv, mode='r') as file:
            reader = csv.reader(file)
            encabezado = next(reader)  # La primera fila tiene el alfabeto (SIGMA)
            SIGMA = encabezado[1:]  # Omitir la primera columna, ya que son los estados

            for fila in reader:
                estado = fila[0]
                transiciones = fila[1:]

                # Verificar si es estado inicial (+) o de aceptación (*)
                if estado.startswith('+'):
                    START_STATE = estado[1:]  # Quitar el símbolo "+"
                    estado = estado[1:]
                if estado.startswith('*'):
                    ACCEPT_STATES.append(estado[1:])  # Quitar el símbolo "*"
                    estado = estado[1:]
                if estado.startswith('+*'):
                    START_STATE = estado[2:]  # El estado es inicial y de aceptación
                    ACCEPT_STATES.append(estado[2:])
                    estado = estado[2:]

                Q.append(estado)  # Añadir el estado a Q
                DELTA[estado] = {SIGMA[i]: transiciones[i] for i in range(len(SIGMA))}

        print("STATES (Q):", Q)
        print("ALPHABET (SIGMA):", SIGMA)
        print("START STATE:", START_STATE)
        print("ACCEPT STATES:", ACCEPT_STATES)
        print("TRANSITIONS (DELTA):", DELTA)

        return Q, SIGMA, DELTA, START_STATE, ACCEPT_STATES

    def checar_estado_aceptacion(self):
        """Verifica si el estado actual pertenece a los estados de aceptación"""
        return self.EstadoActual in self.ACCEPT_STATES

    def recorrer_automata(self, w):
        """Recorre el autómata para ver si la cadena W llega a un estado final"""
        self.EstadoActual = self.START_STATE
        for x in w:
            if x in self.DELTA[self.EstadoActual]:
                self.EstadoActual = self.DELTA[self.EstadoActual][x]
            else:
                return False  # Si la entrada no es válida, rechaza la cadena
            if self.EstadoActual == "JACHI":
                return False
        return self.checar_estado_aceptacion()

def menu():
    AFD = None  # Para almacenar el autómata creado

    while True:
        print("\nMenú:")
        print("A. Nuevo Archivo CSV")
        print("B. Probar Otra Cadena (w)")
        print("C. Salir del programa")

        opcion = input("\nElige una opción: ").upper()

        match opcion:
            case 'A':
                archivo_csv = input("\nProporcione el nombre del archivo CSV (incluyendo la extensión .csv): ")
                try:
                    AFD = automataFD(archivo_csv)
                    input_w = list(input("\nProporcione la cadena: "))
                    resultado = AFD.recorrer_automata(input_w)
                    print("\nCadena Aceptada" if resultado else "\nCadena Rechazada")
                except FileNotFoundError:
                    print("\nArchivo no encontrado. Verifique el nombre y vuelva a intentarlo.")
            case 'B':
                if AFD:
                    input_w = list(input("\nProporcione la nueva cadena: "))
                    resultado = AFD.recorrer_automata(input_w)
                    print("\nCadena Aceptada" if resultado else "\nCadena Rechazada")
                else:
                    print("\nPrimero debe cargar un archivo CSV con la opción A.")
            case 'C':
                print("\nSaliendo del programa...")
                break
            case _:
                print("\nOpción inválida, por favor elige A, B o C.")

if __name__ == "__main__":
    print("\n\nAutómata de estado finito determinista desde archivo CSV\n")
    menu()
