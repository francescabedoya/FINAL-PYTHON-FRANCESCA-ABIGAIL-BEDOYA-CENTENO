def codificar(mensaje, rotaciones):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    longitud_alfabeto = len(alfabeto)
    codificado = ""
    for letra in mensaje:
        if not letra.isalpha() or letra.lower() == 'ñ':
            codificado += letra
            continue
        valor_letra = ord(letra)
       
        alfabeto_a_usar = alfabeto
        limite = 97  
        if letra.isupper():
            limite = 65
            alfabeto_a_usar = alfabeto_mayusculas

        posicion = (valor_letra - limite + rotaciones) % longitud_alfabeto
 
        codificado += alfabeto_a_usar[posicion]
    return codificado
    