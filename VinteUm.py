from asyncio.windows_events import NULL
import random

class Jogador:

	dinheiros = 0
	mao = []
	soma = 0
	jogando = True

	def __init__(self, usuario, senha, nome) -> None:
		super().__init__()
		self.usuario = usuario
		self.senha = senha
		self.nome = nome

	def somarMao(self, carta):
		if(carta == "A"):
			self.soma += 1
		elif(carta == "J" or carta == "Q" or carta == "K"):
			self.soma += 10
		else:
			self.soma += carta
		print(self.soma)
		self.verificaSoma()

	def criarMao(self,baralho):
		mao = []
		mao.append(self.cavarCarta(baralho))
		mao.append(self.cavarCarta(baralho))
		print(mao)

	def cavarCarta(self,baralho):
		if self.jogando:
			carta = baralho.pop()
			self.somarMao(carta) 
			return carta
		return NULL
	
	def verificaSoma(self):
		if self.soma > 21:
			self.jogando = False
			self.soma = 0
			print("Voce perdeu")
		elif self.soma == 21:
			self.jogando = False
			print("Voce ganhou")


class VinteUm:

	jogadores = []

	def criarJogador(self, usuario, senha, nome):
		jogador = Jogador(usuario, senha, nome)
		self.jogadores.append(jogador)
		return jogador

	def criarBaralho(self):
		baralho = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
		random.shuffle(baralho)
		print(baralho)
		return baralho
	
	def ganhou(self):
		maior_soma = 0
		vencedor = NULL
		for j in self.jogadores:
			if j.soma > maior_soma:
				maior_soma = j.soma
				vencedor = j
		return vencedor




if __name__ == '__main__':
	jogo = VinteUm()
	baralho = jogo.criarBaralho()
	jogador1 = jogo.criarJogador('dmcdavi', '123', 'davi')
	jogador2 = jogo.criarJogador('vago', '123', 'vago')
	jogador3 = jogo.criarJogador('fezes', '123', 'joao')
	jogador1.criarMao(baralho)
	jogador2.criarMao(baralho)
	jogador3.criarMao(baralho)
	for i in range(4):
		jogador1.cavarCarta(baralho)
		jogador2.cavarCarta(baralho)
		jogador3.cavarCarta(baralho)
	print(jogo.ganhou())
