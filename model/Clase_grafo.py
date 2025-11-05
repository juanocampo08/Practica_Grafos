
class Grafo:
    def __init__(self):
        self.grafo = {}
        self.sedes = []
        self.costo_por_km = 950 

    def agregar_sede(self, nombre_sede):
        """Agrega una sede al grafo."""
        if nombre_sede not in self.grafo:
            self.grafo[nombre_sede] = []
            self.sedes.append(nombre_sede)


    def agregar_ruta(self, sede_1, sede_2, distancia_km):
        """Agrega una ruta bireccional entre dos sedes.
        
        sede_1 y sede_2: nombres de las sedes.
        distancia_km: distancia en kilómetros entre las sedes.
        """
        if sede_1 not in self.grafo:
            self.agregar_sede(sede_1)
        if sede_2 not in self.grafo:
            self.agregar_sede(sede_2)
        
        costo = distancia_km * self.costo_por_km

        self.grafo[sede_1].append((sede_2, distancia_km, costo))
        self.grafo[sede_2].append((sede_1, distancia_km, costo))

    def obtener_rutas(self, sede):
        """Devuelve las rutas desde una sede dada."""
        return self.grafo.get(sede, [])

        

grafo_prueba = Grafo()

grafo_prueba.agregar_ruta("sede1", "sede2", 10)
grafo_prueba.agregar_ruta("sede1", "sede3", 20)
grafo_prueba.agregar_ruta("sede2", "sede3", 15)
print(grafo_prueba.obtener_rutas("sede1"))
print("-"*20)
print(grafo_prueba.grafo)


    