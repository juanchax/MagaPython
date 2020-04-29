# 01 ----------
#
#
# Esta guía es un solo ejercicio integrador de POO, les dejo para que uds suban su respuesta y abajo está hecho por mí.
# Ejercicio único
#
#  Crear una clase llamada Punto con sus dos coordenadas X e Y.
#  Añadir un método constructor para crear puntos fácilmente. Si no se recibe una coordenada, su valor será cero.
#  Sobreescribir el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
#  Añadir un método llamado cuadrante que indique a qué cuadrante pertenece el punto, teniendo en cuenta que si X == 0 e Y != 0 se sitúa sobre el eje Y, si X != 0 e Y == 0 se sitúa sobre el eje X y si X == 0 e Y == 0 está sobre el origen.
#  Añadir un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
#  (Optativo) Añadir un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:
#
# Nota:
#
# La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:
#
# import math
# math.sqrt(9)
#
#
#  Crear una clase llamada Rectángulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
#  Añadir un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
#  Añadir al rectángulo un método llamado base que muestre la base.
#  Añadir al rectángulo un método llamado altura que muestre la altura.
#  Añadir al rectángulo un método llamado area que muestre el area.
#
#
# Sugerencia:
#
# Pueden identificar fácilmente estos valores si intentan dibujar el cuadrado a partir de su diagonal. Recuerden que pueden utilizar la función abs() para saber el valor absoluto de un número.
#
# Experimentación
# Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
# Consultar a qué cuadrante pertenecen el punto A, C y D.
# Consultar los vectores AB y BA.
# (Optativo) Consultar la distancia entre los puntos 'A y B' y 'B y A'.
# (Optativo) Determinar cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
# Crear un rectángulo utilizando los puntos A y B.
# Consultar la base, altura y área del rectángulo.