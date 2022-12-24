import random


class Pergunta:
    def __int__(self, texto_pergunta, respostas, nivel_pergunta):
        self.texto_pergunta = texto_pergunta
        self.repostas = respostas
        self.nivel_pergunta = nivel_pergunta

    def pergar_resposta_correta(self):
        for resposta in self.repostas:
            if resposta.resposta_correta:
                return resposta

    def eliminar_duas_erradas(self):
        cont = 0
        respostas_com_ajuda = self.repostas
        while cont != 0:
            numero = random.randint(0, 3)
            if not respostas_com_ajuda[numero].resposta_correta:
                respostas_com_ajuda.pop(numero)
                cont -= 1
        return respostas_com_ajuda

    def imprimir_pergunta(self):
        texto = self.texto_pergunta
        cont = 0
        opcoes = ["a)", "b)", "c)", "d)"]
        for resposta in self.respostas:
            texto += f"\n{opcoes[cont]}{resposta.texto_resposta}"
        return texto
