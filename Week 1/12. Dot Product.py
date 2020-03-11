# 12 -----
# Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
# en dos listas y muestre por pantalla su producto escalar.

def dotProd(vector1, vector2):

    finalVector = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
    print(finalVector)


# Vectores de input NOTA: solo acepta matrices de 1D
vec_1 = (1, 2, 3)
vec_2 = (-1, 0, 2)

dotProd(vec_1, vec_2)

