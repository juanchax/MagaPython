# 09 -----------
#
# Crear un diccionario con 10 estudiantes y sus respectivas notas. Luego
# crear una función que nos informe los estudiantes aprobados (nota >= 7),
# los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados
# (0 <= nota < 4).

student_grades = {
                'Alan': 9,
                'Sofi': 10,
                'Richard': 7,
                'Lula': 6,
                'Jere': 8,
                'Yani': 9,
                'Mau': 5,
                'Abril': 6,
                'George': 7,
                'Carito': 3
                }

def student_status(grade_dict):
    students_aprobado = []
    students_reprobado = []
    students_aplazado = []

    for name, grade in student_grades.items():
        if grade >= 7:
            students_aprobado.append(name)
        elif grade >= 4:
            students_reprobado.append(name)
        else:
            students_aplazado.append(name)
    return students_aprobado, students_reprobado, students_aplazado

aprobados, reprobados, aplazados = student_status(student_grades)

print('Estudiantes Aprobados: %s. Estudiantes Reprobados: %s. Estudiantes Aplazados: %s' % (', '.join(aprobados), ', '.join(reprobados), ' ,'.join(aplazados)))
