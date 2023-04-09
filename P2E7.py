#Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de
#palabras sin distinguir entre mayúsculas y minúsculas, en la frase.
import string
texto = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""
print("Mayúsculas: ", len(list(filter(lambda x : x in string.ascii_uppercase, texto))))
print("Minúsculas: ", len(list(filter(lambda x : x in string.ascii_lowercase, texto))))
print("Caracteres no letras: ", len(list(filter(lambda x : x not in string.ascii_letters and x != " ", texto))))
print("Cantidad de palabras: ", len(texto.split()))