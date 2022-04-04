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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging
from urllib import response
from vinte_um import Jogador, VinteUm
import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import time

def createLoginForm(stub):
        username = input("Digite seu login: ")
        password = input("Digite sua senha: ")
       
        
        return stub.Login(helloworld_pb2.LoginRequest(username=username, password=password))

def dig(stub, auth_token):
        
        extraCard = input("Deseja cavar mais uma carta? S/N: ")
        
        return stub.TurnAction(helloworld_pb2.TurnRequest(auth_token=auth_token, dig = extraCard))
        
        
        
                
                
                        
        #return stub.ChooseNumber(helloworld_pb2.StateRequest(auth_token=auth_token))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        login = createLoginForm(stub)
        print(login.message)
        while(True):
                diga = dig(stub, login.auth_token)
                stub.VerifyTurn(helloworld_pb2.VerifyTurnRequest(auth_token=login.auth_token))
        #print(state_response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
