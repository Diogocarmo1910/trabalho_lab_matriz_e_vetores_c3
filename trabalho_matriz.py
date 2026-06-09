def abertura():
    print("=" * 50)
    print("   CONTROLE DE DESEMPENHO DE FILIAIS ")
    print("=" * 50)
    print("Integrantes do grupo:")
    print(" - Diogo Araujo do Carmo")
    print(" - Arthur Shunck ")
    print(" - Matheus Mandelli")
    print("=" * 50)

def ler_numero_positivo(mensagem):
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



if __name__ == "__main__":
    numero = ler_numero_positivo("Digite um numero: ")
    abertura()