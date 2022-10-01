def main():
    pass


"""
Linea 1 de l pseudocigo
Linea 2 del pseudocigo
"""


def menor(num1, num2, num3):
    """ Metodo que calcula el enor de tres numeros

    Args:
        num1 (int): Primer numero a validar
        num2 (int): SEgundo numero a validar
        num3 (int): Tercer numero a validar

    Return:
        manor (int) EL menor de tres numeros
    """
    if (num1 <= num2):
        menorn = num1
    else:
        menorn = num2
    if (num3 < menorn):
        menorn = num3

    return menorn


print(__name__)

if (__name__ == '__main__'):
    respuesta = menor(3, 1, 8)
    pmenorn = 10
    print(respuesta)
    print(menor(3, 1, 8))
    help(menor)
