import networkx as nx
import matplotlib.pyplot as plt

class SistemaExpertoRutas:
    def __init__(self):
        self.grafo = nx.Graph()
        self.reglas = []  # Esta línea es para agregar reglas al sistema experto en el futuro, por el momento no se usa.

    def agregar_nodo(self, nodo):
        self.grafo.add_node(nodo)

    def agregar_arista(self, nodo1, nodo2, peso):
        self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def agregar_regla(self, antecedente, consecuente):  # Esta función no se usa por el momento.
        self.reglas.append((antecedente, consecuente))

    def mejor_ruta(self, inicio, fin):
        try:
            ruta = nx.dijkstra_path(self.grafo, source=inicio, target=fin, weight='weight')                 # La funcion "dijkstra_path" es la que se encarga de buscar la ruta mas corta.
            distancia = nx.dijkstra_path_length(self.grafo, source=inicio, target=fin, weight='weight')     # Segun la ruta va sumando el peso o distancia de cada una para sumar y arrojar ese resultado.
            return ruta, distancia
        except nx.NetworkXNoPath:
            return None, float('inf')

    def mostrar_ruta(self, ruta, distancia):                                                                # Esta funcions nos arroja el resultado final en texto.
        if ruta:
            print(f"La mejor ruta desde {ruta[0]} hasta {ruta[-1]} es: {' -> '.join(ruta)} con una distancia de {distancia}")
        else:
            print("No hay una ruta posible entre los puntos dados.")                                        # si no existieran nodos nos arroja este mensaje.

    def mostrar_grafo(self, ruta=None):                                                                     # Codigo para mostrar graficamente los grafos.
        pos = nx.spring_layout(self.grafo)  # Layout del grafo

        # Dibujar nodos y aristas
        nx.draw(self.grafo, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)     # Propiedades de los nodos, de la letra y de
        nx.draw_networkx_edge_labels(self.grafo, pos, edge_labels={(u, v): d['weight'] for u, v, d in self.grafo.edges(data=True)})

        if ruta:
            # Dibujar la ruta destacada
            ruta_aristas = list(zip(ruta, ruta[1:]))
            nx.draw_networkx_edges(self.grafo, pos, edgelist=ruta_aristas, edge_color='r', width=2)

        plt.show()

# Crear el sistema experto de rutas
sistema = SistemaExpertoRutas()

# Agregar nodos (puntos)
for nodo in ["A", "B", "C", "D", "E", "F", "G", "H"]:
    sistema.agregar_nodo(nodo)

# Agregar aristas (caminos con distancias)
sistema.agregar_arista("A", "B", 10)
sistema.agregar_arista("A", "C", 15)
sistema.agregar_arista("B", "C", 35)
sistema.agregar_arista("B", "D", 25)
sistema.agregar_arista("B", "E", 20)
sistema.agregar_arista("C", "D", 30)
sistema.agregar_arista("C", "E", 25)
sistema.agregar_arista("D", "E", 15)
sistema.agregar_arista("D", "F", 35)
sistema.agregar_arista("E", "F", 10)
sistema.agregar_arista("F", "G", 25)
sistema.agregar_arista("F", "H", 30)
sistema.agregar_arista("G", "H", 5)

# Encontrar la mejor ruta de A a H
ruta, distancia = sistema.mejor_ruta("C", "G")
sistema.mostrar_ruta(ruta, distancia)

# Mostrar el grafo y la ruta
sistema.mostrar_grafo(ruta)
