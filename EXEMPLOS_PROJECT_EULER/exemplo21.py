# Função que calcula a soma dos divisores próprios de um número n
def soma_divisores(n):
    soma = 1  # começamos com 1 porque todo número é divisível por 1

    # vamos testar possíveis divisores de 2 até a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # se i divide n sem resto
            soma += i  # adiciona o divisor
            if i != n // i:  # evita repetir quando for raiz exata
                soma += n // i  # adiciona o "par" do divisor

    return soma  # devolve o total


# Variável para guardar a soma dos números amigáveis
total = 0

# Vamos testar todos os números de 2 até 9999
for a in range(2, 10000):
    b = soma_divisores(a)  # calcula d(a)

    # Verifica se é um número amigável
    if b < a and soma_divisores(b) == a:
        total += a  # soma o número
        print(a, b)
# Mostra o resultado final
print("Soma dos números amigáveis:", total)