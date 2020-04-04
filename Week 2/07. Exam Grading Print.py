# 07 ---------------
#
# Crear un diccionario con 5 estudiantes y sus respectivas notas. Imprimir
# por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario,
# si no con nombre : nota). Tener en cuenta que para aprobar el alumno debe
# sacarse una nota mayor o igual a 7 y menor o igual a 10.

studentGrades = {
    "Marcelo Alvear": 6,
    "Juana Manso": 8,
    "Roque Perez": 10,
    "Manuela Pedraza": 4,
    "Juana Azurduy": 7
}
# para cada par name = studentGrades.key() grade = stutendGrades.value()
for name, grade in studentGrades.items():
    # si el value es mayor o igual a 7
    if grade >= 7:
        print(f"{name} : {grade}")