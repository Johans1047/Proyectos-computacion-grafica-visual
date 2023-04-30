import turtle
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import time


class parte_1:
    @staticmethod
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
            turtle.pensize(2)
            turtle.goto(x0, y0)

            err2 = 2 * err

            if err2 > -dy:
                err = err - dy
                x0 = x0 + incx

            if err2 < dx:
                err = err + dx
                y0 = y0 + incy

    @staticmethod
    def draw_triangle(x0, y0, x1, y1, x2, y2):
        ventana = turtle.Screen()
        ventana.title("Creacion de triangulo")
        ventana.setup(900, 800)
        parte_1.Bresenham(x0, y0, x1, y1)
        parte_1.Bresenham(x1, y1, x2, y2)
        parte_1.Bresenham(x2, y2, x0, y0)

    @staticmethod
    def draw_pentagon(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4):
        ventana = turtle.Screen()
        ventana.title("Creacion de pentagono")
        ventana.setup(900, 800)
        parte_1.Bresenham(x0, y0, x1, y1)
        parte_1.Bresenham(x1, y1, x2, y2)
        parte_1.Bresenham(x2, y2, x3, y3)
        parte_1.Bresenham(x3, y3, x4, y4)
        parte_1.Bresenham(x4, y4, x0, y0)

    @staticmethod
    def triangle_points():
        # Puntos del triángulo
        p1_t = (0, 200)
        p2_t = (-200, -200)
        p3_t = (200, -200)

        turtle.penup()
        turtle.goto(p1_t)
        turtle.pendown()

        parte_1.draw_triangle(p1_t[0], p1_t[1], p2_t[0], p2_t[1], p3_t[0], p3_t[1])

    @staticmethod
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

        parte_1.draw_pentagon(p1_p[0], p1_p[1], p2_p[0], p2_p[1], p3_p[0], p3_p[1], p4_p[0], p4_p[1], p5_p[0], p5_p[1])

    @staticmethod
    def clear_screen():
        # Esperar a que el usuario presione una tecla para limpiar la pantalla
        while True:
            turtle.reset()
            break


# -----------------------------------------------------------------------------------------------------------------------
class parte_2:
    @staticmethod
    def draw_triangle(t):
        ventana = turtle.Screen()
        ventana.title("Relleno de Triángulo")
        ventana.setup(900, 800)
        t.penup()
        t.goto(-100, -50)
        t.pencolor('black')
        t.pendown()
        t.pensize(2)
        for i in range(3):
            t.forward(200)
            t.left(120)

    @staticmethod
    def floodfill(x, y, old_color, new_color):
        ventana = turtle.Screen()
        ventana.title("Relleno de Triángulo")
        ventana.setup(900, 800)
        t = turtle.Turtle()
        parte_2.draw_triangle(t)
        if t.xcor() == x and t.ycor() == y and t.fillcolor() == old_color:
            t.fillcolor(new_color)
            t.begin_fill()
            t.goto(x, y)
            for i in range(3):
                t.forward(200)
                t.left(120)
            t.end_fill()
            parte_2.floodfill(x + 1, y, old_color, new_color)
            t.fillcolor(old_color)  # Restablecer el color de relleno
            parte_2.floodfill(x - 1, y, old_color, new_color)
            t.fillcolor(old_color)  # Restablecer el color de relleno
            parte_2.floodfill(x, y + 1, old_color, new_color)
            t.fillcolor(old_color)  # Restablecer el color de relleno
            parte_2.floodfill(x, y - 1, old_color, new_color)
            t.fillcolor(old_color)  # Restablecer el color de relleno

    @staticmethod
    def floodfill_call():
        parte_2.floodfill(-100.00000000000003, -49.999999999999915, 'black', 'red')

    @staticmethod
    def clear_screen_2():
        t = turtle.Turtle()
        t.penup()
        t.goto(-100, -50)
        t.pendown()
        t.pencolor('white')
        t.pensize(2)
        t.fillcolor('white')
        t.begin_fill()
        for i in range(3):
            t.forward(200)
            t.left(120)
        t.end_fill()


class parte_3:
    @staticmethod
    def triangle_points2():
        ventana = turtle.Screen()
        ventana.title("Traslacion de centroide")
        ventana.setup(900, 800)
        # Puntos del triángulo
        p1_t = (150, 45)
        p2_t = (50, 80)
        p3_t = (275, 150)

        turtle.penup()
        turtle.goto(p1_t)
        turtle.pendown()

        parte_1.draw_triangle(p1_t[0], p1_t[1], p2_t[0], p2_t[1], p3_t[0], p3_t[1])

        # Coordenadas del centroide
        cx = (p1_t[0] + p2_t[0] + p3_t[0]) / 3
        cy = (p1_t[1] + p2_t[1] + p3_t[1]) / 3

        coordenada_1 = f"Las coordenadas actuales del centroide son: ({cx}, {cy})"

        # Definir la nueva posición del centroide
        nc = (50, 200)

        # Calcular el vector de traslación
        vector_traslacion = (nc[0] - cx, nc[1] - cy)

        # Translada cada vértice de la figura original
        p1nuevo = (p1_t[0] + vector_traslacion[0], p1_t[1] + vector_traslacion[1])
        p2nuevo = (p2_t[0] + vector_traslacion[0], p2_t[1] + vector_traslacion[1])
        p3nuevo = (p3_t[0] + vector_traslacion[0], p3_t[1] + vector_traslacion[1])

        time.sleep(3)  # Esperar 3 segundos

        parte_1.clear_screen()

        turtle.penup()  # Levanta la pluma
        turtle.goto(p1nuevo)
        turtle.pendown()  # Baja la pluma para que se pueda volver a dibujar

        parte_1.draw_triangle(p1nuevo[0], p1nuevo[1], p2nuevo[0], p2nuevo[1], p3nuevo[0], p3nuevo[1])

        coordenada_2 = print(f"La nueva posición del centroide es: ({nc[0]}, {nc[1]})")

    # -----------------------------------------------------------------------------------------------------------------------


def main():
    def opcion_bresenham():
        # Ocultamos la pantalla principal
        ventana.withdraw()

        # Creamos la ventana bresenham
        ventana_parte_1()

    def opcion_floodfill():
        # Ocultamos la pantalla principal
        ventana.withdraw()

        # Creamos la ventana floodfill
        ventana_parte_2()

    def opcion_traslacion():
        # Ocultamos la pantalla principal
        ventana.withdraw()

        # Creamos la ventana de traslacion
        ventana_parte_3()

    def ventana_parte_1():
        # Crear la nueva ventana como una ventana secunadaria que pertenece a la misma instancia
        ventana_bresenham = tk.Toplevel(ventana)
        ventana_bresenham.title("Proyecto 1 - Algoritmo Bresenham")
        ventana_bresenham.geometry("400x370")

        # Cambiar color de fondo
        ventana_bresenham.configure(bg="lightblue")

        # Crear botones
        boton_triangulo = tk.Button(ventana_bresenham, text="Triángulo", command=lambda: parte_1.triangle_points(),
                                    height=3, width=20)
        boton_pentagono = tk.Button(ventana_bresenham, text="Pentágono", command=lambda: parte_1.pentagon_points(),
                                    height=3, width=20)
        boton_cls1 = tk.Button(ventana_bresenham, text="Limpiar Pantalla", command=lambda: parte_1.clear_screen(),
                               height=2, width=15)

        # Posicionar botones
        boton_triangulo.pack(pady=30)
        boton_pentagono.pack(pady=30)
        boton_cls1.pack(pady=30)

        # Agregar un botón para volver a la ventana principal
        boton_volver = tk.Button(ventana_bresenham, text="Volver",
                                 command=lambda: volver_a_ventana_principal(ventana_bresenham))
        boton_volver.place(x=10, y=5)

        # Mostrar la ventana
        ventana_bresenham.mainloop()

    def ventana_parte_2():
        # Crear la nueva ventana como una ventana secunadaria que pertenece a la misma instancia
        ventana_floodfill = tk.Toplevel(ventana)
        ventana_floodfill.title("Proyecto 1 - Algoritmo Floodfill")
        ventana_floodfill.geometry("400x250")

        # Cambiar color de fondo
        ventana_floodfill.configure(bg="lightblue")

        # Crear botones
        boton_fill = tk.Button(ventana_floodfill, text="Rellenar figura", command=lambda: parte_2.floodfill_call(),
                               height=3, width=20)
        boton_cls2 = tk.Button(ventana_floodfill, text="Limpiar Pantalla", command=lambda: parte_2.clear_screen_2(),
                               height=2, width=15)

        # Posicionar botones
        boton_fill.pack(pady=30)
        boton_cls2.pack(pady=30)

        # Agregar un botón para volver a la ventana principal
        boton_volver = tk.Button(ventana_floodfill, text="Volver",
                                 command=lambda: volver_a_ventana_principal(ventana_floodfill))
        boton_volver.place(x=10, y=5)

        # Mostrar la ventana
        ventana_floodfill.mainloop()

    def ventana_parte_3():
        # Crear la nueva ventana como una ventana secunadaria que pertenece a la misma instancia
        ventana_traslacion = tk.Toplevel(ventana)
        ventana_traslacion.title("Proyecto 1 - Algoritmo de Traslación")
        ventana_traslacion.geometry("400x250")

        # Cambiar color de fondo
        ventana_traslacion.configure(bg="lightblue")

        # Crear botones
        boton_crear = tk.Button(ventana_traslacion, text="Crear Figura", command=lambda: parte_3.triangle_points2(),
                                height=3, width=20)
        boton_cls3 = tk.Button(ventana_traslacion, text="Limpiar Pantalla", command=lambda: parte_1.clear_screen(),
                               height=2, width=15)

        # Posicionar botones
        boton_crear.pack(pady=30)
        boton_cls3.pack(pady=30)

        # Agregar un botón para volver a la ventana principal
        boton_volver = tk.Button(ventana_traslacion, text="Volver",
                                 command=lambda: volver_a_ventana_principal(ventana_traslacion))
        boton_volver.place(x=10, y=5)

        # Mostrar la ventana
        ventana_traslacion.mainloop()

    def volver_a_ventana_principal(ventana_secundaria):
        # Destruir la ventana bresenham
        ventana_secundaria.destroy()

        # Mostrar la ventana principal
        ventana.deiconify()

        # Crear la ventana principal

    ventana = tk.Tk()
    ventana.title("Proyecto 1- Graficos por computadora")
    ventana.geometry("720x380")

    # Cambiar color de fondo
    ventana.configure(bg="lightblue")

    # Carga la imagen 1 y la convierte en un objeto de imagen de tkinter
    imagen1 = Image.open('UTP1.png')
    imagen1 = imagen1.resize((200, 200))  # Cambiar el tamaño de la imagen
    imagen_tk1 = ImageTk.PhotoImage(imagen1)
    # Carga la imagen 2 y la convierte en un objeto de imagen de tkinter
    imagen2 = Image.open('UTP2.png')
    imagen2 = imagen2.resize((200, 200))  # Cambiar el tamaño de la imagen
    imagen_tk2 = ImageTk.PhotoImage(imagen2)
    # Crea una instancia de Label y muestra la imagen 1 en la ventana
    label_imagen1 = Label(ventana, image=imagen_tk1, bg="lightblue")
    label_imagen1.place(x=0, y=0)
    # Crea una instancia de Label y muestra la imagen 2 en la ventana
    label_imagen2 = Label(ventana, image=imagen_tk2, bg="lightblue")
    label_imagen2.place(x=525, y=0)

    # Crear botones
    boton1 = tk.Button(ventana, text="Parte 1", command=opcion_bresenham, height=3, width=20)
    boton2 = tk.Button(ventana, text="Parte 2", command=opcion_floodfill, height=3, width=20)
    boton3 = tk.Button(ventana, text="Parte 3", command=opcion_traslacion, height=3, width=20)
    boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit, height=2, width=15)

    # Posicionar botones
    boton1.pack(pady=30)
    boton2.pack(pady=30)
    boton3.pack(pady=30)
    boton_salir.place(x=575, y=300)
    # Mostrar la ventana
    ventana.mainloop()


if __name__ == "__main__":
    main()
