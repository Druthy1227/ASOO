"""
=============================================================================
SIMULADO DE AVALIACAO PRATICA
Analise de Sistemas Orientado a Objetos — UNI-RN — 2026.2
Prof. Wendell Oliveira de Araujo

SISTEMA DE VENDA DE INGRESSOS DE CINEMA

Nome:  ______________________________________  Matricula: ______________

INSTRUCOES
  - Complete apenas os trechos marcados com # TODO.
  - NAO altere a classe Filme nem o programa de teste do final do arquivo.
  - Execute o programa quantas vezes quiser: a saida esperada esta no
    enunciado em PDF. Se a sua saida bater com ela, a questao esta correta.
  - Consulta liberada: slides das aulas, seus arquivos poo01 a poo04 e
    anotacoes. Nao e permitido consultar colegas.
=============================================================================
"""

# =============================================================================
# CLASSE FORNECIDA — nao altere
# =============================================================================

class Filme:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min, {self.classificacao})"


# =============================================================================
# QUESTAO 1 (3,0) — Classe Ingresso com encapsulamento
#
# Crie a classe Ingresso com:
#   - construtor recebendo: comprador, preco e poltrona # Ok
#   - o preco deve ser um atributo PRIVADO # Ok
#   - get_preco()  -> devolve o preco # Ok
#   - set_preco(valor) -> so altera se o valor for maior que zero; # Ok
#                         caso contrario, exibe:
#                         Preco invalido! Deve ser maior que zero.

#   - valor() -> devolve o valor a ser pago pelo ingresso
#   - __str__() -> devolve, por exemplo:
#                  Ana Beatriz | poltrona A1 | R$ 30.00
#
# DICA: faca o __str__ usar self.valor(), e nao o atributo direto.
#       Isso sera importante na Questao 2.
# =============================================================================

class Ingresso:
    def __init__(self, comprador, preco, poltrona):
        self.comprador = comprador
        self.__preco = preco
        self.poltrona = poltrona

    def get_preco(self):
        return self.__preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print("Preço inválido! Deve ser maior que zero")

    def valor(self):
        return self.get_preco()

    def __str__ (self):
        return f"{self.comprador} | poltrona {self.poltrona} | R$ {self.valor():.2f}"
    pass


# =============================================================================
# QUESTAO 2 (2,5) — Heranca: IngressoMeiaEntrada
#
# Crie a classe IngressoMeiaEntrada, que E UM tipo de Ingresso:
#   - construtor recebendo: comprador, preco, poltrona e tipo_desconto
#     (use super() para aproveitar o construtor da superclasse) # Ok
#   - sobrescreva valor() para devolver METADE do preco # OK
#   - sobrescreva __str__() para acrescentar o tipo de desconto ao final, # OK
#     aproveitando a versao da superclasse. Exemplo:
#     Bruno Carvalho | poltrona A2 | R$ 15.00 (meia - estudante) # OK
# =============================================================================

class IngressoMeiaEntrada(Ingresso):
    def __init__(self, comprador, preco, poltrona, tipo_desconto):
        super().__init__(comprador, preco, poltrona)
        self.tipo_desconto = tipo_desconto

    def valor(self):
        return super().valor() / 2

    def __str__(self):
        return f"({super().__str__()} meia - {self.tipo_desconto})"
    pass


# =============================================================================
# QUESTAO 3 (3,0) — Classe gerenciadora Sessao
#
# Crie a classe Sessao com:
#   - construtor recebendo: filme (um OBJETO da classe Filme) e horario
#   - a colecao de ingressos deve ser um atributo PRIVADO, iniciando vazia
#   - vender(ingresso) -> adiciona o ingresso a colecao
#   - listar() -> exibe todos os ingressos, um por linha
#   - buscar(comprador) -> devolve o OBJETO ingresso encontrado, ou None
#   - total_ingressos() -> devolve a quantidade de ingressos vendidos
#   - faturamento() -> devolve a soma do valor de TODOS os ingressos
#
# ATENCAO: o faturamento deve funcionar corretamente com ingressos inteiros
#          e de meia-entrada misturados na mesma sessao.
# =============================================================================

class Sessao:
    def __init__(self, filme, horario):
        self.filme = filme
        self.horario = horario
        self.__ingressos = []        

    def vender(self, ingresso):
        self.__ingressos.append(ingresso)

    def listar(self):
        for ingresso in self.__ingressos:
            print(ingresso)

    def buscar(self, comprador):
        for ingresso in self.__ingressos:
            if ingresso.comprador == comprador:
                return ingresso
        return None

    def total_ingressos(self):
        return len(self.__ingressos)

    def faturamento(self):
        total = 0
        for ingresso in self.__ingressos:
            total += ingresso.valor()
        return total

    pass
    


# =============================================================================
# QUESTAO 4 (1,5) — Justificativas
#
# Responda nos espacos abaixo, em poucas linhas, com suas proprias palavras.
#
# a) Por que a relacao entre Sessao e Ingresso e de COMPOSICAO,
#    e nao de agregacao?
#
#    R: Ingresso DEPENDE de seção, se uma seção deixar de existir, for adiada ou qualquer outra situação, o mesmo deve se aplicar aos ingressos
#
#
# b) Por que IngressoMeiaEntrada HERDA de Ingresso, em vez de TER um Ingresso
#    como atributo?
#
#    R: Por possui a relação semântica "É um", Um IngressoMeiaEntrada É UM Ingresso e vice-versa, tendo as mesmas características fundamentais (comprador, preco, poltrona) e caso alguma característica seja adicionad ou removida, provavelmente se aplicara a Meia Entrada
#
#
# c) Onde exatamente esta o polimorfismo no metodo faturamento()?
#
#    R: No laço de repetição (for) dentro da Classe Sessão. Ao chamar o ingresso.valor(), o sistema determina qual valor é executado (O inteiro ou dividido por 2) com base na classe pertencente.
#
# =============================================================================


# =============================================================================
# PROGRAMA DE TESTE — nao altere nada daqui para baixo
# =============================================================================

if __name__ == "__main__":
    duna = Filme("Duna: Parte Dois", 166, "14 anos")
    sessao = Sessao(duna, "19:30")

    print("=== SESSAO ===")
    print(f"{sessao.filme} - {sessao.horario}")

    sessao.vender(Ingresso("Ana Beatriz", 30.0, "A1"))
    sessao.vender(IngressoMeiaEntrada("Bruno Carvalho", 30.0, "A2", "estudante"))
    sessao.vender(Ingresso("Carla Dias", 30.0, "B5"))
    sessao.vender(IngressoMeiaEntrada("Diego Nunes", 30.0, "B6", "idoso"))

    print("\n--- INGRESSOS VENDIDOS ---")
    sessao.listar()

    print(f"\nTotal de ingressos: {sessao.total_ingressos()}")
    print(f"Faturamento: R$ {sessao.faturamento():.2f}")

    achado = sessao.buscar("Carla Dias")
    print(f"\nBusca por 'Carla Dias': {achado}")

    perdido = sessao.buscar("Fulano")
    if perdido is None:
        print("Busca por 'Fulano': nao encontrado")

    print()
    ing = Ingresso("Teste", 20.0, "C1")
    ing.set_preco(-5)
    print(f"Preco apos tentativa invalida: R$ {ing.get_preco():.2f}")
