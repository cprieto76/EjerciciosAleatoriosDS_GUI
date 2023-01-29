from tkinter import * # Libreria para crear interfaces graficas
import random   # modulo para generar numeros aleatorios o escoger elementos de una lista aleatoriamente

diccionario_preguntas = {"uno": "pregunta 1", "dos": "pregunta 2", "tres": "pregunta 3", "cuatro": "pregunta 4",
                         "cinco": "pregunta 5"}
lista_preguntas = []
raiz = Tk()  # Esta funcion del modulo tkinter crea una aplicacion tkinter. Crea una ventana nivel alto (top-level). La funcion retorna 
             #, un objeto asignado tipicamente a una variable

raiz.title("preguntas") # title() es un metodo de la clase Tk que coloca titulo de la ventana

def seleccion_preguntas():                                       # Funcion
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)   # randint() es una función incorporada del modulo random que retorna 
                                                                 # entero aleatorio entre dos numeros dados (inclusive).
    print("dentro de seleccion de preguntas")
    print(lista_preguntas[random_index])


def preguntas():
    for numero in diccionario_preguntas:
        lista_preguntas.append(numero)
    random_index = random.randint(0, len(lista_preguntas) - 1)
    print(lista_preguntas[random_index])
    random_index = random.randint(0, len(lista_preguntas) - 1)
    print(diccionario_preguntas[lista_preguntas[random_index]])
    return diccionario_preguntas[lista_preguntas[random_index]]


def click_boton_pregunta():
    texto = Label(raiz, text= preguntas()).grid()  #Label es una clase del modulo Tkinter, se utiliza para crear un widget (artilugo,
                                                   # interfase) para mostrar texto o imagenes.
                                                   # El metodo grid() llama entonces el objeto label, que empaqueta la etiqueta en la 
                                                   # ventana principal utilizando el administrador de geometría de cuadrícula.
def click_boton_hita():
    texto = Label(raiz, text= preguntas()).grid()


boton_pregunta = Button(raiz, text="pregunta", padx=50, pady=25, command=click_boton_pregunta).grid(row=1, column=1)
# La clase Button se utiliza para crear un widget de botón en el que el usuario puede hacer clic para realizar una acción.
#Este código parece estar creando un widget de botón con el texto "pregunta" y colocándolo en un diseño de cuadrícula en la primera fila 
# y la primera columna. El botón también se le da un ancho y alto de 50 y 25 píxeles respectivamente. El atributo de comando 
# se establece en "click_boton_pregunta", lo que significa que cuando se hace clic en el botón, se llamará a 
# la función "click_boton_pregunta".

boton_hit = Button(raiz, text="hit!", padx=50, pady=25, command=click_boton_hita).grid(row=1, column=4)

preguntas()

raiz.mainloop()
# mainloop() es un método de la clase Tkinter Tk, que es la clase principal para crear una aplicación Tkinter. Este método ingresa 
# a un ciclo infinito que espera que ocurran los eventos y los procesa a medida que ocurren.
