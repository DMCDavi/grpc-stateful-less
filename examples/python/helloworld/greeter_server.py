# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
from email import message
import logging
import time
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
from vinte_um import Jogador, VinteUm
#from vinte_um import Jogador, VinteUm
game = None


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    #global game
    def Login(self, request, context):
        global game
        auth_token = request.username + '_' + request.password
  
        if(game == None):
            createGame()
        player = game.criarJogador(auth_token)
        player.criarMao(game.baralho)

        return helloworld_pb2.LoginReply(message='Você fez login com sucesso.', auth_token=auth_token)


    def TurnAction(self, request, context):
        global game
        
        jogador = self.VerifyAuth(request.auth_token)
        print(jogador.mao)
        if(request.dig == "S" or request.dig == "s"):
            jogador.cavarCarta(game.baralho)
        else:
            jogador.jogando = False
        changeTurn()
        
        return helloworld_pb2.HelloReply(message=str(jogador.jogando))
    
    def VerifyAuth(self, auth_token):
        global game

        for jogador in game.jogadores:
          
            if(jogador.auth_token == auth_token):
            
                
                return jogador
        return None
 
    def VerifyTurn(self,request, context):
        
        while(not game.endGame):
            continue
        message = self.ShowWinner()
        return helloworld_pb2.HelloReply(message=message)
    
    def ShowWinner(self):
        global game
        jog = []
        som = 0
        for jogador in game.jogadores:
            if(jogador.soma == som):
                print(jogador.soma)
                jog.append(jogador)
                som = jogador.soma
            elif(jogador.soma > som and jogador.soma <= 21):
               
                jog.clear()
                
                jog.append(jogador)
                som = jogador.soma
            
        if(len(jog) == 1):
            return ("Vencedor da partida é: "+jog[0].auth_token.split("_")[0])
        else:
            x = []
            for i in jog:
                x.append(i.auth_token.split("_")[0])  
            return ("O jogo terminou em empate entre: " + str(x))                
                     

def VerifyWin():
    global game
    
    for jogador in game.jogadores:
        if(jogador.jogando):
            return True
    game.endGame = True
    return False 

def changeTurn():
    global game
    count = len(game.jogadores)
    if(game.vez < count-1):
        game.vez += 1
    else:
        game.vez = 0
    VerifyWin()        
        
def createGame():
    global game
    print("Bem vindo ao jogo VINTE E UM!")
    time.sleep(2)
    print("Embaralhando as cartas...")
    time.sleep(2)
    print("Distribuindo as cartas...")
    time.sleep(2)
    game = VinteUm()
    game.criarBaralho()
    

  
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    #createGame()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
