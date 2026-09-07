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
"""

4.
dado = input("Digite um número: ")
print(type(dado))

dado = int(dado)
print(type(dado))

dado = bool(dado)
print(type(dado))

"""
5. 
(8 - 4)
2 ** 2
5 * 2 ** 2
5 * 2 ** 2 / (8 - 4)
10 + resultado

6. Quando queremos atribuir um valor usamos =, já o == é usado para comparar a igualdade.

7. Retornam False, pois o Python interpreta 0 e "" como valores falsos.

"""

8. 
renda_mensal = float(input("Digite sua renda mensal: "))
dependentes = int(input("Digite a quantidade de dependentes: "))
elegivel = renda_mensal <3000 or dependentes >2
print(elegivel)

9.
nome = input("Digite seu nome: ")
valor_total = float(input("Informe o valor total recebido: "))
total_gastos = float(input("Informe o total de gastos: "))

saldo_final = float(valor_total - total_gastos) + 100
meta_atingida = saldo_final >= 1500
print(f"Olá {nome}. Seu saldo final é de {saldo_final}. Confira aqui se sua meta foi atingida: {meta_atingida}")

"""
10. A tipagem dinâmica significa que o Python identifica automaticamente o tipo do valor atribuído a uma variável. Já a conversão explícita de tipos ocorre quando o programador precisa converter um valor de um tipo para outro. 
Um exemplo é quando se deseja realizar uma operação matemática com um valor armazenado como str, sendo necessário convertê-lo para int ou float antes da operação.
"""