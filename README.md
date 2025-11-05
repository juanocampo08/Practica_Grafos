# 🚚 Sistema de Optimización de Rutas de Entrega

## Descripción del Proyecto
Este proyecto simula un sistema de entrega de materia prima para una empresa de comidas con múltiples sedes en la ciudad. El sistema calcula la ruta más económica para entregar a todas las sedes considerando:
- Distancia entre sedes (en km)
- Costo del combustible (Diesel)
- Optimización usando algoritmos de grafos

## Estructura del Proyecto
```
PRACTICA_GRAFOS/
│
├── main.py              # Programa principal
├── grafo.py            # Clase del grafo y operaciones
├── algoritmos.py       # MST y Backtracking
└── README.md           # Este archivo
```

## Cómo Ejecutar el Proyecto

### Requisitos
- Python 3.7 o superior
- No requiere librerías externas

### Ejecución
```bash
python main.py
```

## Supuestos Asumidos

1. **Costo de combustible**: $9,500 COP por galón de Diesel
2. **Rendimiento del vehículo**: 10 km por galón
3. **Costo por kilómetro**: $950 COP/km
4. **Sedes**: 6 sedes distribuidas en la ciudad
5. **Punto de inicio**: Bodega Central (Sede 0)
6. **Rutas bidireccionales**: Todas las rutas pueden recorrerse en ambas direcciones
7. **Entrega diaria**: Se debe visitar cada sede exactamente una vez

## Algoritmos Implementados

### 1. Árbol de Expansión Mínimo (Kruskal)
Encuentra el conjunto de rutas que conecta todas las sedes con el menor costo total.

### 2. Backtracking
Explora diferentes secuencias de entrega para encontrar la ruta óptima que:
- Visite todas las sedes
- Minimice el costo total
- Retorne al punto de inicio

## Desarrollador
- Juan Ocampo (@juanocampo08)