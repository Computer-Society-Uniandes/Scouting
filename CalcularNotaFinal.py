def calcular_nota_necesaria(notas, porcentajes, nota_minima):

    # Covertir porcentajes a fracciones
    porcentajes = [porcentaje / 100 for porcentaje in porcentajes]

    # Calcular la suma de las notas ponderadas
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas += notas[i] * porcentajes[i] 

    # Calcular el porcentaje restante para la próxima nota	
    porcentaje_restante = 1 - sum(porcentajes)

    # Calcular la nota necesaria para pasar
    nota_necesaria = (nota_minima - suma_notas) / porcentaje_restante
    return nota_necesaria

# Ejemplo de uso:
notas = [3.0, 4.0, 3.5] # Notas obtenidas
porcentajes = [30, 30, 20] # Porcentajes de cada nota
nota_minima = 3.0 # Nota mínima para pasar

nota_necesaria = calcular_nota_necesaria(notas, porcentajes, nota_minima)
print(f'Necesitas sacar {nota_necesaria:.2f} en la próxima nota para pasar la materia.')
