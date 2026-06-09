O def é um bloco. Ele é utilizado para se caso necessario, ser reutilizado e organizado de uma forma que de pra entender o codigo completo. 
Isso é uma boa pratica de organização


Ex no codigo do trabalho:

def abertura():
    print("=" * 50)
    Essa parte é mais uma forma de aparecer no painel. Esse print repete o caractere a quantidade de vezes que o usuario desejar. Com isso, o painel fica mais vizual. 
    print("   CONTROLE DE DESEMPENHO DE FILIAIS ")
    print("=" * 50)
    print("Integrantes do grupo:")
    print(" - Diogo Araujo do Carmo")
    print(" - Arthur Shunck ")
    print(" - Matheus Mandelli")
    print("=" * 50)

já no proximo bloco:

#def ler_numero_positivo(mensagem):
    while True:
        entrada_numero = input(mensagem)
        if not entrada_numero.isdigit():
            print("Erro: digite um numero inteiro valido.")
            continue
        valor = int(entrada_numero)
        if valor < 0:
            print("Erro: digite um numero inteiro maior ou igual a 0.")
            continue
        return valor

Esse bloco é um bloco de validação para o numero que for digitado não ser negativo ou 0. Caso aconteça, dara um erro que ira que digitar novamente o numero. Esse numero terá que ser inteiro e positivo. 

def ler_float_positivo(mensagem):
    while True:
        entrada = input(mensagem).replace(",", ".")
        try:
            valor = float(entrada)
        except ValueError:
            print("Erro: digite um numero valido.")
            continue
        if valor < 0:
            print("Erro: nao sao permitidos valores negativos.")
            continue
        return valor

Esse bloco é quase a mesma coisa do bloco anterior, só que ele é um validador de numero float, ou decimal. 

entrada = input(mensagem).replace(",", ".")
Essa parte em especifico funciona 




