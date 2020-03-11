
# 15 -----
# Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso
# {'Matemáticas': 6, 'Física': 4, 'Química': 5}
# y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
# donde <asignatura> es cada una de las asignaturas del curso,
# y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.


def showSubjects(asigsDict):

    keys_asignaturas = list(asigsDict.keys())
    for keys in keys_asignaturas:
        print(keys + " tiene " + str(asigsDict[keys]) + " créditos.")
    else:
        print("Total de créditos: " + str(sum(asigsDict.values())))


# create dictionary with the subjects and their credits
creds_asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
showSubjects(creds_asignaturas)
