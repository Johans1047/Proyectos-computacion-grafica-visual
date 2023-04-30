import turtle

# Creamos la ventana de Turtle con dimensiones 500x500
ventana = turtle.Screen()
ventana.title("Relleno de triangulo")
ventana.setup(500, 500)

t = turtle.Turtle()
t.pensize(3)
t.speed(1)

# Definimos una función para dibujar un triángulo
def draw_triangle():
    t.penup()
    t.goto(-100, -50)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    for i in range(3):
        t.forward(200)
        t.left(120)
    t.end_fill()

# Definimos una función para implementar el algoritmo de floodfill
def floodfill(x, y, old_color, new_color):
    if t.xcor() == x and t.ycor() == y and t.fillcolor() == old_color:
        t.fillcolor(new_color)
        t.begin_fill()
        t.goto(x, y)
        for i in range(3):
            t.forward(200)
            t.right(120)
        t.end_fill()
        floodfill(x + 1, y, old_color, new_color)
        t.fillcolor(old_color)  # Restablecer el color de relleno
        floodfill(x - 1, y, old_color, new_color)
        t.fillcolor(old_color)  # Restablecer el color de relleno
        floodfill(x, y + 1, old_color, new_color)
        t.fillcolor(old_color)  # Restablecer el color de relleno
        floodfill(x, y - 1, old_color, new_color)
        t.fillcolor(old_color)  # Restablecer el color de relleno

# Llamamos a la función para dibujar el triángulo
draw_triangle()

# Llamamos a la función para implementar el algoritmo de floodfill
floodfill(0, 0, "white", "red")

# Mantenemos la ventana abierta hasta que el usuario la cierre
turtle.done()
