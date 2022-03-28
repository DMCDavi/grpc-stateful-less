import numpy as np
import random

class Jogador(self,usuario,senha,nome):
	usuario = self.usuario
	senha = self.senha
	nome = self.nome

	dinheiros = 0
	mao = []
	soma = 0

	def somarMao(self, carta):
		if(carta == "A"):
			self.soma += 1
		else if(carta == "J" or carta == "Q" or carta == "K"):
			self.soma += 10
		else:
			self.soma += carta


class VinteUm(self):


	def criarBaralho(self):
		baralho = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
		random.shuffle(baralho)
		print(baralho)
		return baralho

	def criarMao(self,baralho):
		mao = []

		mao.append(cavarCarta(baralho))
		mao.append(cavarCarta(baralho))
		print(mao)


	def cavarCarta(self,baralho):
		return baralho.pop()


baralho = criarBaralho()
criarMao(baralho)
