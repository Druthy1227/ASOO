# alunos = ["Ana", "Bruno", "Carla"]

# print(alunos[0]) 
# print(alunos[-1]) #(Último)

# print(alunos[0:2]) # Sempre termina com -1


notas = [7.0, 5.5, 9.0]

notas.append(8.0) # Adiciona ao Fim
notas.insert(0,6.0) # Adiciona na posição 0 (Começo)
notas.remove(5.5) # Remove pelo VALOR
ultima = notas.pop() # Remove e guarda o último valor
print(notas.sort()) #Ordena Crescente
# print(notas.sort(reverse=True)) #Decrescente

# print(len(notas), sum(notas))
# print(max(notas), min(notas))
# print(sum(notas) / len(notas))

aluno = {
"matricula": 2026001,
"nome": "Ana Beatriz",
"media": 8.5
}
print(aluno["nome"])         #Ana Beatriz
aluno["media"] = 9.0         # Altera
aluno["curso"] = "SI"        # Adiciona

for chave, valor in aluno.items():
    print(f"{chave}: {valor}")