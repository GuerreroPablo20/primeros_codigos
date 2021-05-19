def es_primo(numero_seleccionado):

## -------------------------------------------------------
## ----- FUNCION QUE DETERMINA SI ES UN NUMERO PRIMO -----

    vector = range(2,numero_seleccionado+1)
    longitud = len(vector)
    contador = 0

    if numero_seleccionado == 1:
        return True

    for i in vector:
        if numero_seleccionado % i !=0:
            contador += 1
            continue
    
    if contador+1 == longitud:
        return True
    else:
        return False 

def run():
## -------------------------------------------------------
## ----- PROGRAMA QUE INVOCA A FUNCION DE NUM PRIMOS -----
    valor = int(input('Ingrese el numero : '))
    respuesta = es_primo(valor)
    if respuesta == True:
        print('El numero ' + str(valor) + ' es un numero primo' )
    else:
        print('El numero ' + str(valor) + ' no es un numero primo' )


if __name__ == '__main__':
    run()