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

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

def createLoginForm(stub):
        username = input("Digite seu nome de usuario: ")
        password = input("Digite sua senha: ")
        is_stateful = input('Deseja salvar sua sessao? [y/n]')

        return stub.Login(helloworld_pb2.LoginRequest(username=username, password=password, is_stateful=is_stateful=='y'))

def createStateForm(stub, auth_token):
        number = input("Por favor digite um número de 0 a 100: ")
        return stub.ChooseNumber(helloworld_pb2.StateRequest(auth_token=auth_token, number=number))

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('0.0.0.0:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        login = createLoginForm(stub)
        print(login.message)
        state_response = createStateForm(stub, login.auth_token)
        print(state_response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
