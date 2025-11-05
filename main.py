# main.py - Programa principal

from Grafo import Grafo
from algoritmos import kruskal_mst, backtracking_rutas

def crear_grafo_empresa():
    """
    Crea el grafo con las sedes y rutas de la empresa de comidas
    """
    g = Grafo()
    
    print("\n🏢 SISTEMA DE ENTREGA - EMPRESA DE COMIDAS")
    print("="*60)
    print("💵 Costo del Diesel: $9,500 COP/galón")
    print("⛽ Rendimiento: 10 km/galón")
    print("📊 Costo por km: $950 COP")
    print("="*60)
    
    # Definir las 6 sedes
    sedes = [
        "Bodega Central",
        "Sede Norte",
        "Sede Sur",
        "Sede Este",
        "Sede Oeste",
        "Sede Centro"
    ]
    
    # Agregar sedes al grafo
    for sede in sedes:
        g.agregar_sede(sede)
    
    # Agregar rutas (distancias en km)
    # Estas distancias son realistas para una ciudad
    rutas = [
        ("Bodega Central", "Sede Norte", 8),
        ("Bodega Central", "Sede Centro", 5),
        ("Bodega Central", "Sede Oeste", 12),
        ("Sede Norte", "Sede Este", 6),
        ("Sede Norte", "Sede Centro", 7),
        ("Sede Sur", "Sede Centro", 4),
        ("Sede Sur", "Sede Este", 9),
        ("Sede Este", "Sede Centro", 5),
        ("Sede Oeste", "Sede Centro", 10),
        ("Sede Oeste", "Sede Sur", 11)
    ]
    
    for sede1, sede2, distancia in rutas:
        g.agregar_ruta(sede1, sede2, distancia)
    
    return g

def main():
    """Función principal del programa"""
    
    # 1. Crear el grafo
    grafo = crear_grafo_empresa()
    
    # 2. Mostrar el grafo completo
    grafo.mostrar_grafo()
    
    # 3. Calcular el Árbol de Expansión Mínimo
    mst, costo_mst = kruskal_mst(grafo)
    
    # 4. Encontrar la mejor ruta con backtracking
    inicio = "Bodega Central"
    mejor_ruta, costo_ruta = backtracking_rutas(grafo, inicio)
    
    # 5. Resumen final
    print("\n" + "="*60)
    print("📊 RESUMEN EJECUTIVO")
    print("="*60)
    print(f"\n1️⃣  CONEXIÓN MÍNIMA (MST):")
    print(f"   - Costo para conectar todas las sedes: ${costo_mst:,} COP")
    print(f"   - Útil para: Planificación de infraestructura base")
    
    print(f"\n2️⃣  RUTA ÓPTIMA DE ENTREGA (Backtracking):")
    print(f"   - Costo total del recorrido: ${costo_ruta:,} COP")
    print(f"   - Ruta: {' → '.join(mejor_ruta)}")
    print(f"   - Útil para: Entregas diarias de materia prima")
    
    print("\n" + "="*60)
    print("✅ Análisis completado exitosamente")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()