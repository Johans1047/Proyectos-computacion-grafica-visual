import turtle


def dibujar_triangulo():
    ventana = turtle.Screen()
    ventana.setup(500, 500)
    ventana.title("Triangulo")

    dibujante = turtle.Turtle()
    dibujante.pensize(3)
    dibujante.speed(0)

    # Dibuja el triángulo
    dibujante.penup()
    dibujante.goto(-100, -100)
    dibujante.pendown()
    dibujante.fillcolor("white")
    dibujante.begin_fill()
    for _ in range(3):
        dibujante.forward(200)
        dibujante.left(120)
    dibujante.end_fill()


def floodfill(x, y, old_color, new_color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(new_color)
    turtle.stamp()

    imagen = turtle.getcanvas().postscript(colormode='color')
    pixels = []
    for row in imagen.split('\n')[2:-1]:
        row_pixels = [int(row[i:i + 3], 8) for i in range(0, len(row), 4)]
        pixels.append(row_pixels)

    width, height = len(pixels[0]), len(pixels)

    if (0 <= x < width) and (0 <= y < height):
        if pixels[height - 1 - y][x] == old_color:
            pixels[height - 1 - y][x] = new_color
            floodfill(x + 1, y, old_color, new_color)
            floodfill(x - 1, y, old_color, new_color)
            floodfill(x, y + 1, old_color, new_color)
            floodfill(x, y - 1, old_color, new_color)


# Rellena el triángulo de color rojo
dibujar_triangulo()
turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
floodfill(0, 0, 16777215, 'red')
turtle.done()
