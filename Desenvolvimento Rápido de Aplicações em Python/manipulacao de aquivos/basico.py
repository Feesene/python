

try:
    arquivo = open("teste.txt")
    print(repr(arquivo.read()))

except FileNotFoundError as erro:
    print("Arquivo nao existe!")
