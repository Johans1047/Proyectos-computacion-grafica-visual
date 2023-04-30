import turtle


def Bresenham(x0, y0, x1, y1):
    # Distancia recorrida en cada eje y declaración de variables
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)

    # Incremento en las secciones con avance inclinado
    if x0 < x1:
        incx = 1
    else:
        incx = -1

    if y0 < y1:
        incy = 1
    else:
        incy = -1

    # Inicializar el valor de error
    err = dx - dy

    while x0 != x1 and y0 != y1:  # Mientras el punto inicial sea distinto al final

        turtle.color("Red")
        turtle.goto(x0, y0)

        err2 = 2 * err

        if err2 > -dy:
            err = err - dy
            x0 = x0 + incx

        if err2 < dx:
            err = err + dx
            y0 = y0 + incy


def draw_triangle(x0, y0, x1, y1, x2, y2):
    Bresenham(x0, y0, x1, y1)
    Bresenham(x1, y1, x2, y2)
    Bresenham(x2, y2, x0, y0)


def draw_pentagon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4):
    Bresenham(x0, y0, x1, y1)
    Bresenham(x1, y1, x2, y2)
    Bresenham(x2, y2, x3, y3)
    Bresenham(x3, y3, x4, y4)
    Bresenham(x4, y4, x0, y0)


def triangle_points():
    # Puntos del triángulo
    p1_t = (0, 200)
    p2_t = (-200, -200)
    p3_t = (200, -200)

    turtle.penup()
    turtle.goto(p1_t)
    turtle.pendown()

    draw_triangle(p1_t[0], p1_t[1], p2_t[0], p2_t[1], p3_t[0], p3_t[1])


def triangle_points2():
    # Puntos del triángulo
    p1_t = (150, 45)
    p2_t = (50, 80)
    p3_t = (275, 150)

    turtle.penup()
    turtle.goto(p1_t)
    turtle.pendown()

    draw_triangle(p1_t[0], p1_t[1], p2_t[0], p2_t[1], p3_t[0], p3_t[1])

    # Coordenadas del centroide
    cx = (p1_t[0] + p2_t[0] + p3_t[0]) / 3
    cy = (p1_t[1] + p2_t[1] + p3_t[1]) / 3

    print(f"Las coordenadas actuales del centroide son: ({cx}, {cy})")

    # Definir la nueva posición del centroide
    nc = (50, 200)

    # Calcular el vector de traslación
    vector_traslacion = (nc[0] - cx, nc[1] - cy)

    # Translada cada vértice de la figura original
    p1nuevo = (p1_t[0] + vector_traslacion[0], p1_t[1] + vector_traslacion[1])
    p2nuevo = (p2_t[0] + vector_traslacion[0], p2_t[1] + vector_traslacion[1])
    p3nuevo = (p3_t[0] + vector_traslacion[0], p3_t[1] + vector_traslacion[1])

    clear_screen()

    turtle.penup()  # Levanta la pluma
    turtle.goto(p1nuevo)
    turtle.pendown()  # Baja la pluma para que se pueda volver a dibujar

    draw_triangle(p1nuevo[0], p1nuevo[1], p2nuevo[0], p2nuevo[1], p3nuevo[0], p3nuevo[1])

    print(f"La nueva posición del centroide es: ({nc[0]}, {nc[1]})")


def pentagon_points():
    # Puntos del pentagono
    p1_p = (-100, -100)
    p2_p = (100, -100)
    p3_p = (150, 75)
    p4_p = (0, 150)
    p5_p = (-150, 75)

    turtle.penup()
    turtle.goto(p1_p)
    turtle.pendown()

    draw_pentagon(p1_p[0], p1_p[1], p2_p[0], p2_p[1], p3_p[0], p3_p[1], p4_p[0], p4_p[1], p5_p[0], p5_p[1])


def clear_screen():
    # Esperar a que el usuario presione una tecla para limpiar la pantalla
    while True:

        cls = int(input("Introduce el número 0 para limpiar la pantalla: "))

        if cls == 0:
            turtle.reset()
            break


# -------------------------------------------------------------------------------------------------------------------------------

# PARTE 1
figure = int(input("Introduzca 1 para dibujar un triángulo, 2 para dibujar un pentángono: "))

if figure == 1:

    triangle_points()
    clear_screen()

elif figure == 2:

    pentagon_points()
    clear_screen()

else:
    print("Por defecto se mostrará el triángulo.")
    triangle_points()
    clear_screen()

# --------------------------------------------------------------------------------------------------------------------------------

# PARTE 3 - Creamos un triángulo para utilizar un algoritmo de traslación
triangle_points2()

turtle.done()  # Para que la pantalla espere a que el usuario la cierre