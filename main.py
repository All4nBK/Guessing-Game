# Bibliotecas
import random  # Importa a biblioteca 'random' para gerar números aleatórios.

# Variáveis
numeroMaquina = []  # Lista que irá guardar números de 0 até o número que o usuário escolher inicialmente.
tentativas = 0  # Variável que irá guardar o número de tentativas.
loop = 1  # Variável para definir se o código vai entrar em loop ou não.
menorNumero = 0  # Variável que irá mostrar o menor número digitado pelo usuário.
maiorNumero = 0  # Variável que irá mostrar o maior número digitado pelo usuário.

# Código principal
numeroUsuario = int(input("Escolha o intervalo? "))  # Solicita ao usuário que escolha um número para definir o intervalo de números que o código irá escolher.
maiorNumero = numeroUsuario  # Atribui o maior valor para a variável 'maiorNumero'.

for i in range(0, numeroUsuario + 1):  # Irá definir o range de 0 até o número definido pelo usuário na variável 'numeroUsuario'.
    numeroMaquina.append(i)  # Está atribuindo um valor dentro da lista a cada vez que o loop for executado.
numeroEscolhido = random.choice(numeroMaquina)  # Usa a biblioteca 'random' para escolher um valor da lista e armazená-lo na variável 'numeroEscolhido'.

while loop != 0:
    numeroTentativa = int(input("Qual o número que foi escolhido? "))  # Solicita ao usuário um número como tentativa.
    tentativas += 1  # Incrementa o número de tentativas.

    if numeroTentativa > numeroEscolhido:
        maiorNumero = numeroTentativa
        print("Você chutou alto demais, tente novamente.\nO número está entre", menorNumero, "e", maiorNumero)
    elif numeroTentativa < numeroEscolhido:
        menorNumero = numeroTentativa
        print("Você chutou baixo demais.\nO número está entre", menorNumero, "e", maiorNumero)
    else:
        if tentativas <= 5:
            print("Parabéns! Você acertou após", tentativas, "tentativas")
        elif tentativas > 5 and tentativas < 10:
            print("Parabéns! Você acertou após", tentativas, "tentativas, mas poderia ser mais rápido.")
        else:
            print("Sangue Ruim! Você acertou após", tentativas, "tentativas")
        loop = 0  # Encerra o loop.

print(numeroEscolhido)  # Exibe o número escolhido pela máquina após o jogo.