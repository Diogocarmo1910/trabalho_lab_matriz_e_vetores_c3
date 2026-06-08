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







