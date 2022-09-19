"""
    function divisible_por(num)
{
  if (num divisible entre 3 y 5)
  {
    regresa verdadero;
  }
  else
  {
    regresa falso;
  }

}
    """


def divisible_por(n):
    """ Método que indica si un número es divisible entre 3 y 5

    Args:
        n (int): número  a decidir si es divisible entre 3 y 5

    Returns:
        bool : verdadero si es divisible, Falso si no lo es
    """
    if (n % 3 == 0 and n % 5 == 0):
        return True
    else:
        return False


"""
Método main;
recibo en n el numero maximo a checa;
for (i = 0 ; i <= n; i = i + 1)
{
  call divisible_por(i); //recibo en r la respuesta
  if (r es verdadero)
  {
    imprimo i;
  }
} 
"""


def main():
    n = int(input("Dame el numero : "))
    for i in range(1, n + 1):
        if (divisible_por(i)):
            print(i)


main()
