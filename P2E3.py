import string
jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks,
code, and data. JupyterLab is flexible: configure and arrange the user
interface to support a wide range
of workflows in data science, scientific computing, and machine learning.
JupyterLab is extensible and
modular: write plugins that add new components and integrate with existing
ones.
"""
#solicite por teclado una letra e imprima
#las palabras que comienzan con dicha letra. 
#En caso que no se haya inrgesado un letra, indique el
#error
jupyter_info = jupyter_info.lower()
letter = input()
#if letter in string.ascii_letters:
#    words = jupyter_info.split()
#    for word in words:
#        if word.startswith(letter):
#            print(word)
#else:
#    print("No ha ingresado una letra.")
 #La función filter devuelve un objeto iterable con todos 
 # quellos valores de una colección de datos que cumplen una
 # determinada condición. Hay que invocarla con dos parámetros: 
 # una función que determina si un elemento dado cumple la 
 # condición y la colección de datos a filtrar: filter(funcion, datos) .   

if letter not in string.ascii_letters:
    print("¡No ha ingresado una letra!")
else:
    words = filter(lambda w: w.startswith(letter), jupyter_info.split())
    for word in words:
        print(word)

