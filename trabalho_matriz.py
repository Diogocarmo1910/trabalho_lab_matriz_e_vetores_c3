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

filiais = ['Filial Centro', 'Filial Shopping', 'Filial Praia']
semanas = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4']

faturamento = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

for c in range(0, 3):
    for d in range(0, 4):
        while True:
            valor = float(input(f"Faturamento da {filiais[c]} na {semanas[d]}: "))
            if valor < 0:
                print("Valor invalido! Digite um numero positivo.")
            else:
                faturamento[c][d] = valor
                break

print(faturamento[c][d])


if __name__ == "__main__":
    numero = ler_numero_positivo("Digite um numero: ")
    abertura()