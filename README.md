# Jogo de Adivinhação

Este é um simples jogo de adivinhação em Python, onde o jogador tenta adivinhar um número escolhido aleatoriamente pela máquina. O jogador recebe dicas para ajustar suas tentativas e é informado sobre o número de tentativas que levou para acertar.

## Funcionamento do Código

### Bibliotecas Utilizadas

O código utiliza a biblioteca `random` para randomizar os numeros.

```python
import random
```

### Variáveis Principais

- `numeroMaquina`: Uma lista que guarda números de 0 até o número definido pelo usuário.
- `tentativas`: Uma variável que conta o número de tentativas do jogador.
- `loop`: Uma variável para controlar o loop principal do jogo.
- `menorNumero`: Uma variável que guarda o menor número digitado pelo usuário.
- `maiorNumero`: Uma variável que guarda o maior número digitado pelo usuário.

### Intervalo de Números

O jogador é solicitado a escolher um número para definir o intervalo de números que o código pode escolher.

```python
numeroUsuario = int(input("Escolha o intervalo? "))
```

O código, em seguida, cria uma lista `numeroMaquina` com números de 0 até o número escolhido pelo usuário.

```python
for i in range(0, numeroUsuario + 1):
    numeroMaquina.append(i)
```

A máquina escolhe aleatoriamente um número dentro do intervalo definido.

```python
numeroEscolhido = random.choice(numeroMaquina)
```

### Loop Principal

O jogo está dentro de um loop `while`, onde o jogador pode continuar adivinhando até acertar o número.

```python
while loop != 0:
```

O jogador fornece um palpite, e o código fornece dicas com base no palpite.

- Se o palpite for maior que o número escolhido, o código informa que o palpite foi alto e atualiza a variável `maiorNumero`.

- Se o palpite for menor que o número escolhido, o código informa que o palpite foi baixo e atualiza a variável `menorNumero`.

- Se o palpite for igual ao número escolhido, o código encerra o jogo e fornece uma mensagem de parabéns com base no número de tentativas.

### Exibição do Número Escolhido

Após o término do jogo, o código exibe o número escolhido pela máquina.

```python
print(numeroEscolhido)
```

## Executando o Jogo

Para jogar o jogo, basta executar o código em um ambiente Python. Siga as instruções fornecidas durante o jogo para fazer seus palpites e tente acertar o número escolhido pela máquina.

Divirta-se jogando o jogo de adivinhação!