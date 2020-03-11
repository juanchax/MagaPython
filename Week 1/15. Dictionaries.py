
# 15 -----
# Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso,
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

creds_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
keys_asignaturas = list(creds_asignaturas.keys())

for keys in keys_asignaturas:
    print(keys + " tiene " + str(creds_asignaturas[keys]) + " créditos.")

print("Total de créditos: " + str(sum(creds_asignaturas.values())))
