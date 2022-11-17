# def teste(x):
#     print (x)


# teste(2)
def func1():
    global x
    x = 10
    print(f'Função func1 - x = {x}')


def func2(y):
    global x
    x = 20 + int(y)
    print(f'Função func2 - x = {x}')
    return x


x = 0
func1()
func2(2)
print(f'Programa principal - x = {x}')


def regressiva(x):
    print(x)
    regressiva(x - 1)
