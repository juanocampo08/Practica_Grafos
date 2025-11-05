class UnionFind:
    """
    Estructura para detectar ciclos (necesaria para Kruskal)
    """
    def __init__(self, elementos):
        # Cada elemento es su propio padre al inicio
        self.padre = {elemento: elemento for elemento in elementos}
        self.rango = {elemento: 0 for elemento in elementos}
    
    def encontrar(self, elemento):
        """Encuentra la raíz del conjunto al que pertenece el elemento"""
        if self.padre[elemento] != elemento:
            # Compresión de ruta para optimizar
            self.padre[elemento] = self.encontrar(self.padre[elemento])
        return self.padre[elemento]
    
    def unir(self, elem1, elem2):
        """Une dos conjuntos"""
        raiz1 = self.encontrar(elem1)
        raiz2 = self.encontrar(elem2)
        
        if raiz1 != raiz2:
            # Unir por rango para mantener el árbol balanceado
            if self.rango[raiz1] < self.rango[raiz2]:
                self.padre[raiz1] = raiz2
            elif self.rango[raiz1] > self.rango[raiz2]:
                self.padre[raiz2] = raiz1
            else:
                self.padre[raiz2] = raiz1
                self.rango[raiz1] += 1
            return True
        return False
def kruskal_mst(grafo):
    """
    Algoritmo de Kruskal para encontrar el Árbol de Expansión Mínimo
    
    ¿Qué hace?
    Encuentra el conjunto de rutas más baratas que conectan todas las sedes
    sin formar ciclos.
    """
    print("\n" + "="*60)
    print("CALCULANDO ÁRBOL DE EXPANSIÓN MÍNIMO (Algoritmo de Kruskal)")
    print("="*60)
    
    # Obtener todas las aristas y ordenarlas por costo (de menor a mayor)
    aristas = grafo.obtener_todas_las_aristas()
    aristas_ordenadas = sorted(aristas, key=lambda x: x[3])  # Ordenar por costo
    
    print("\n📊 Aristas ordenadas por costo:")
    for i, (s1, s2, dist, costo) in enumerate(aristas_ordenadas, 1):
        print(f"{i}. {s1} ↔ {s2}: {dist} km (${costo:,})")
    
    # Crear estructura Union-Find para detectar ciclos
    uf = UnionFind(grafo.sedes)
    
    # Lista para guardar las aristas del MST
    mst = []
    costo_total = 0
    
    print("\n🔍 Proceso de selección:")
    for sede1, sede2, distancia, costo in aristas_ordenadas:
        # Si no forma ciclo, agregar al MST
        if uf.unir(sede1, sede2):
            mst.append((sede1, sede2, distancia, costo))
            costo_total += costo
            print(f"✅ Agregada: {sede1} ↔ {sede2} ({distancia} km, ${costo:,})")
        else:
            print(f"❌ Rechazada: {sede1} ↔ {sede2} (formaría un ciclo)")
        
        # Si ya tenemos n-1 aristas, terminamos
        if len(mst) == len(grafo.sedes) - 1:
            break
    
    print("\n" + "="*60)
    print("RESULTADO DEL MST:")
    print("="*60)
    print(f"💰 Costo total mínimo para conectar todas las sedes: ${costo_total:,} COP")
    print(f"🛣️  Número de rutas utilizadas: {len(mst)}")
    
    return mst, costo_total


def backtracking_rutas(grafo, inicio):
    """
    Usa backtracking para encontrar la mejor ruta de entrega
    que visite todas las sedes y regrese al inicio
    
    ¿Qué hace?
    Prueba todas las posibles combinaciones de rutas para encontrar
    la más económica.
    """
    print("\n" + "="*60)
    print("OPTIMIZACIÓN CON BACKTRACKING")
    print("="*60)
    
    n_sedes = len(grafo.sedes)
    mejor_ruta = None
    mejor_costo = float('inf')
    
    # Variable para contar cuántas rutas exploramos
    rutas_exploradas = [0]
    
    def calcular_costo_ruta(ruta):
        """Calcula el costo total de una secuencia de sedes"""
        costo = 0
        for i in range(len(ruta) - 1):
            sede_actual = ruta[i]
            sede_siguiente = ruta[i + 1]
            
            # Buscar el costo de ir de sede_actual a sede_siguiente
            for destino, distancia, costo_tramo in grafo.obtener_rutas(sede_actual):
                if destino == sede_siguiente:
                    costo += costo_tramo
                    break
        return costo
    
    def backtrack(ruta_actual, sedes_visitadas, costo_actual):
        """Función recursiva de backtracking"""
        nonlocal mejor_ruta, mejor_costo
        rutas_exploradas[0] += 1
        
        # Caso base: visitamos todas las sedes
        if len(sedes_visitadas) == n_sedes:
            # Intentar regresar al inicio
            sede_actual = ruta_actual[-1]
            for destino, distancia, costo_regreso in grafo.obtener_rutas(sede_actual):
                if destino == inicio:
                    costo_total = costo_actual + costo_regreso
                    ruta_completa = ruta_actual + [inicio]
                    
                    # Si es mejor que la mejor encontrada, actualizar
                    if costo_total < mejor_costo:
                        mejor_costo = costo_total
                        mejor_ruta = ruta_completa
                    return
        
        # Poda: si ya gastamos más que la mejor ruta, no seguir explorando
        if costo_actual >= mejor_costo:
            return
        
        # Explorar todas las sedes vecinas no visitadas
        sede_actual = ruta_actual[-1]
        for destino, distancia, costo_tramo in grafo.obtener_rutas(sede_actual):
            if destino not in sedes_visitadas:
                # Hacer la elección
                ruta_actual.append(destino)
                sedes_visitadas.add(destino)
                
                # Recursión
                backtrack(ruta_actual, sedes_visitadas, costo_actual + costo_tramo)
                
                # Deshacer la elección (backtrack)
                ruta_actual.pop()
                sedes_visitadas.remove(destino)
    
    # Iniciar el backtracking desde la sede inicial
    print(f"\n🏁 Iniciando búsqueda desde: {inicio}")
    backtrack([inicio], {inicio}, 0)
    
    print(f"🔍 Rutas exploradas: {rutas_exploradas[0]}")
    
    if mejor_ruta:
        print("\n" + "="*60)
        print("MEJOR RUTA DE ENTREGA ENCONTRADA:")
        print("="*60)
        print(f"📍 Secuencia: {' → '.join(mejor_ruta)}")
        print(f"💰 Costo total: ${mejor_costo:,} COP")
        print(f"📏 Sedes visitadas: {len(mejor_ruta) - 1}")
        
        # Mostrar detalle de cada tramo
        print("\n📋 Detalle de la ruta:")
        for i in range(len(mejor_ruta) - 1):
            origen = mejor_ruta[i]
            destino = mejor_ruta[i + 1]
            for dest, dist, costo in grafo.obtener_rutas(origen):
                if dest == destino:
                    print(f"{i+1}. {origen} → {destino}: {dist} km (${costo:,})")
                    break
    
    return mejor_ruta, mejor_costo
