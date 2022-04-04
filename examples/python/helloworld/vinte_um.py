
import random

class Jogador:
	auth_token = None
	mao = []
	soma = 0
	jogando = True
	turno = False
	
	def __init__(self, auth_token) -> None:
		super().__init__()
		self.auth_token = None
		self.mao = []
		self.soma = 0
		self.jogando = True
		self.turno = False
		self.auth_token = auth_token
		


	def somarMao(self, carta):
		if(carta == "A"):
			self.soma += 1
		elif(carta == "J" or carta == "Q" or carta == "K"):
			self.soma += 10
		else:
			self.soma += carta

	def criarMao(self,baralho):
		self.mao = []
		self.cavarCarta(baralho)
		self.cavarCarta(baralho)
		

	def cavarCarta(self,baralho):
		if self.jogando:
			carta = baralho.pop()
			self.somarMao(carta)
			self.mao.append(carta)
			return carta
  
		return None
	
	def verificaSoma(self):
		if self.soma > 21:
			self.jogando = False
			return "Você passou de 21 e perdeu ;-;"
			
		elif self.soma == 21:
			self.jogando = False
			return "Parabéns, você tem 21 pontos! espere os outros jogadores"
			


class VinteUm:
	jogadores = []
	baralho = []
	endGame = False
	
	def __init__(self) -> None:
		super().__init__()
		self.vez = 0
		self.jogadores = []
		self.baralho = []
		self.endGame = False
	
	def criarJogador(self, auth_token):
		jogador = Jogador(auth_token)
		self.jogadores.append(jogador)
		return jogador

	def criarBaralho(self):
		self.baralho = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K",
				"A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
		random.shuffle(self.baralho)

	def ganhou(self):
		maior_soma = 0
		vencedor = None
		for j in self.jogadores:
			if j.soma > maior_soma:
				maior_soma = j.soma
				vencedor = j
		return vencedor


