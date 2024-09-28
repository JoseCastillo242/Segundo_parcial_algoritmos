select = input('Selecciona tu funcion M para multiplicar o E para elevar: ')
def principal():
    if select == "M":
        func2()
    else:
        if select == "E":
            func1()
        else:
            print('No pusiste un valor valido! intenta denuevo')
            return()

def func1():
    valor1 = int(input('Ingrese un numero entero: '))
    test = valor1 * valor1
    print('Tu numero al cuadrado es: ', test)

def func2():
    origin3 = int(input('Ingrese un numero entero: '))
    origin5 = int(input('Ingrese otro numero entero: '))
    test2 = origin3 * origin5
    print('El producto de tus numeros es', test2)
    
principal()