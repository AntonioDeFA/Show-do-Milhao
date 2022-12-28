class Competicao:

    def __init__(self):
        self.perguntas = [[]]

    def retornar_todas_perguntas(self):
        return self.perguntas

    def adicionar_pergunta(self, pergunta):
        if pergunta.nivel_pergunta-1>4:
            raise Exception("O nivel das questões só vai até o nivel 5")
        self.perguntas[pergunta.nivel_pergunta].append(pergunta)

    def remover_pergunta(self, pergunta):
        self.perguntas[pergunta.nivel_pergunta].remove(pergunta)

    def validar_quantidade_perguntas(self):
        for var in self.perguntas:
            if len(var) < 5:
                return False
        return True
