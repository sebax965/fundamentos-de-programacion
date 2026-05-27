# 1. DATOS INICIALES
# Formato de la matriz: [ID cliente, duración (segundos) , eventos Clics]
sesiones_clientes = [
    [101, 200, 12],   # cumple duración > 180 y clics > 8 ->alto
    [102, 45, 2],    # Cumple Duración < 60 o Clics < 3   -> Bajo
    [103, 150, 5],   # No cumple Alto ni Bajo            -> Medio
    [104, 300, 1],   # Clics < 3 (cumple la condición O) -> Bajo
    [105, 190, 10]   # Cumple Duración > 180 y Clics > 8  -> Alto
]

# 2. MODULO (FUNCIÓN) DE CLASIFICACIÓN
def clasificar _ compromiso(duración, clics) :
    """
    evalua el nivel de compromiso de una sesión segun las reglas de negocio.
    """
    # logica de negocio
    # clasificar como "alto" si duración > 180 y clics > 8
    if duración > 180 and clics > 8
      return "alto"
    # Clasificar como "Bajo" si Duración < 60 O Clics < 3
    elif duracion < 60 or clics < 3:
        return "Bajo"
    
    # Clasificar como "Medio" en todos los demás casos
    else:
        return "Medio"

# 3. PROCESAMIENTO Y SALIDA ( general el informe)
print("==========================================")
print("      INFORME DE COMPROMISO DE CLIENTES    ")
print("==========================================")
print(f"{' ID cliente' :< 15}{'clasificacion final' :<20}")
print("==========================================")


# Recorrer la matriz fila por fila
for sesion in sesiones_clientes:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    
    # Llamar a la función para obtener la clasificación
    resultado = clasificar_compromiso(duracion, clics)
    
    # Mostrar en el informe
    print(f"{id_cliente:<15}{resultado:<20}")

print("=========================================")
