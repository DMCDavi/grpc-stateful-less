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
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc

user_states = []
print("app funciona")
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    def Login(self, request, context):
        auth_token = request.username + '_' + request.password
        print("login funciona")
        if(self.HasSession(auth_token)):
            for state in user_states:
                if(state['auth_token'] == auth_token):
                    return helloworld_pb2.LoginReply(message='Você já tem uma sessão ativa, e seu número é ' + state['number'], auth_token=auth_token)

        if (request.is_stateful):
            user_states.append({'auth_token': auth_token})

        return helloworld_pb2.LoginReply(message='Você fez login com sucesso.', auth_token=auth_token)

    def ChooseNumber(self, request, context):
        for state in user_states:
            if(state['auth_token'] == request.auth_token):
                state['number'] = request.number
                return helloworld_pb2.HelloReply(message='O número ' + request.number + ' foi salvo em sua sessão.')

        return helloworld_pb2.HelloReply(message='Seu número é ' + request.number)

    def HasSession(self, auth_token):
        for state in user_states:
            if(state['auth_token'] == auth_token):
                return 1
        return 0
        


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
