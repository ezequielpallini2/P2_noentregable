frase = input("Ingrese una frase: ")
palabra = input("Ingrese una palabra: ")
cantidad = len(list(filter(lambda x: x == palabra, frase.split())))
print("Palabra: ", palabra, "Resultado: ", cantidad)