print("Turma de ASSO - 4° Período")
print("Revisão de Python")

# ------ x ------

nome = "Ana";
media1 = 7.66666
print(f"{nome}: {media1:>10.2f}")

# ------ x ------

# Desafio A
nome = "Luiz";
cidade = "Natal";
idade = 20;

print(f"\nMeu nome é {nome}, moro em {cidade} e tenho {idade} anos de idade.")

# Desafio B
nota1 = 6.5
nota2 = 8.3
media1 = (nota1 + nota2) / 2

print(f"\nA média das notas é de {media1}.")

#Desafio C

valor = 64849

print(f"\nNa quantia de {valor} reais, cabem {valor/50}notas de 50 reais, e sobram {valor%50} reais.")


# ----------
# Estruturas de Controle

media2 = float(7)
if media2 >= 7:
    print("Aprovado");
elif media2 >= 4:
    print("Recuperação");
else:
    print("Reprovado");

# ----------

media3 = 8.0
frequencia = 60

if media3 >= 7 and frequencia >= 75:
    print("Aprovado(media3)");
else:
    print("Reprovado (media3)");

# Aninhação (if dentro de if)

if media3 >= 7:
    if frequencia >= 75:
        print("Aprovado(media3)");
    else:
        print("Reprovado por falta(media3)");


# ---------
# while / for
# While - sei a quantidade de repeitções
# for - Não sei a quantidade de repetições

contador = 1
while contador <= 5:
    print(contador);
    contador += 1

soma = 0
for nota in [7,8,6]:
    soma += nota
print(soma);


# -------
for i in range(5):
    print(i);

for i in range(1, 7):
    print(i);

for i in range(10, 0, -2):
    print(i)

for aluno in ["Ana", "Bruno"]:
    print(aluno)


## Laços aninhados

for i in range(1,4):
    for j in range (1,4):
        print(f"{i}x{j}={i*j}")


# --------
# Desafio A (2)

# Leia 5 notas usando for
# Mostre a média e a maior nota

notas = [5,6,10,7,9]
soma1 = 0
maior = 0
for i in notas:
    soma1 = soma1 + i
    if i >= maior:
        maior = i

print(f"A soma das notas é {soma1} e a maior nota é {maior}")


# Desafio B (2)
# Peça números até o usuário digitar 0
# Ao final, mostre quantos foram digitados e a soma


contador1 = 0
soma2 = 0
numero = int(input("Digite um número para somar ou 0 para exibir o resultado: "))

while numero != 0:
    contador1 += 1
    soma2 += numero

    numero = int(input("Digite um número para somar ou 0 para exibir o resultado: "))

print("\n--- Resultado ---")
print(f"Quantidade de números digitados: {contador1}")
print(f"A soma total é: {soma2}")

# Desafio C
# Peça um número inteiro
# Mostre a tabuada dele de 1 a 10
tabuada = int(input("Digite um númnero: "))

for i in range (1,11):
    print(f"{tabuada} x {i} = {tabuada * i}")

## Coleções/Listas

alunos = ["Ana", "Bruno", "Carla"]

print(alunos[0]) 
print(alunos[-1]) #(Último)