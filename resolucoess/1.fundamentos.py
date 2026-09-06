"""
1.A tipagem forte não junta dois tipos incompatíveis automáticamente. 

2.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = num1 + num2
print(f"A soma entre os números {num1} e {num2} é: {soma}. O tipo de dado do resultado é {type(soma)}")

3.
a = Inválido, pois uma variável não pode começar com número.
b = Válido, pois variáveis podem começar com _.
c = Inválido, pois, em Python, o hífen é considerado um operador de subtração.
d = Válido, pois variáveis podem conter _.
e = Inválido, pois é uma palavra reservada, e variáveis não podem ser nomeadas com palavras reservadas.









4. Crie uma variável chamada dado e atribua inicialmente um número inteiro a ela. Em seguida, reatribua a variável para um texto (str) e depois para um booleano (bool). A cada alteração, use print() para exibir o valor e o tipo atual da variável.

5. Sem executar o código, analise a expressão abaixo e indique a ordem em que as operações serão realizadas, de acordo com a precedência dos operadores em Python:
resultado = 10 + 5 * 2 ** 2 / (8 - 4)

6. Qual é a diferença funcional entre = e ==?

7. O que as chamadas bool(0) e bool("") retornam e por quê?

8. Crie um verificador de elegibilidade para um benefício. O programa deve receber:
- A renda mensal, que pode conter casas decimais;
- A quantidade de dependentes, que deve ser um número inteiro.
Armazene na variável elegivel uma única expressão lógica que retorne True quando a renda for menor que 3000.00 ou a quantidade de dependentes for maior que 2. Por fim, exiba o valor de elegivel na tela.

9. Mini-Programa Integrador — Controle financeiro
- Solicite o nome da pessoa, o valor total recebido e o total de gastos.
- Determine o saldo final considerando o valor recebido, os gastos e um bônus fixo de 100.00.
- Crie uma variável meta_atingida para verificar se o saldo final atingiu o valor mínimo de 1500.00.
- Exiba o nome, o saldo final e o resultado da verificação da meta.

10. Qual é a diferença entre tipagem dinâmica e conversão explícita de tipos em Python? Dê um exemplo de quando uma conversão de tipo seria necessária. 
"""
"""
4.
dado = input("Digite um número: ")
print(type(dado))

dado = int(dado)
print(type(dado))

dado = bool(dado)
print(type(dado))





5. 
(8 - 4)
2 ** 2
5 * 2 ** 2
5 * 2 ** 2 / (8 - 4)
10 + resultado

6. Quando queremos atribuir um valor usamos =, já o == é usado para comparar a igualdade.

7. Retornam False, pois o Python interpreta 0 e "" como valores falsos.

8. 
renda_mensal = float(input("Digite sua renda mensal: "))
dependentes = int(input("Digite a quantidade de dependentes: "))
elegivel = renda_mensal <3000 or dependentes >2
print(elegivel)

9. Mini-Programa Integrador — Controle financeiro
- Solicite o nome da pessoa, o valor total recebido e o total de gastos.
- Determine o saldo final considerando o valor recebido, os gastos e um bônus fixo de 100.00.
- Crie uma variável meta_atingida para verificar se o saldo final atingiu o valor mínimo de 1500.00.
- Exiba o nome, o saldo final e o resultado da verificação da meta.

"""

nome = input("Digite seu nome: ")
valor_total = float(input("Informe o valor total recebido: "))
total_gastos = float(input("Informe o total de gastos: "))

saldo_final = float(valor_total - total_gastos) + 100
meta_atingida = saldo_final >= 1500
print(f"Olá {nome}. Seu saldo final é de {saldo_final}. Confira aqui se sua meta foi atingida: {meta_atingida}")