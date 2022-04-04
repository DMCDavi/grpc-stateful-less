# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld_pb2 as helloworld__pb2


class GreeterStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/helloworld.Greeter/Login',
                request_serializer=helloworld__pb2.LoginRequest.SerializeToString,
                response_deserializer=helloworld__pb2.LoginReply.FromString,
                )
        self.TurnAction = channel.unary_unary(
                '/helloworld.Greeter/TurnAction',
                request_serializer=helloworld__pb2.TurnRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )
        self.VerifyTurn = channel.unary_unary(
                '/helloworld.Greeter/VerifyTurn',
                request_serializer=helloworld__pb2.VerifyTurnRequest.SerializeToString,
                response_deserializer=helloworld__pb2.HelloReply.FromString,
                )


class GreeterServicer(object):
    """The greeting service definition.
    """

    def Login(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnAction(self, request, context):
        """Sends another greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def VerifyTurn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreeterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=helloworld__pb2.LoginRequest.FromString,
                    response_serializer=helloworld__pb2.LoginReply.SerializeToString,
            ),
            'TurnAction': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnAction,
                    request_deserializer=helloworld__pb2.TurnRequest.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
            'VerifyTurn': grpc.unary_unary_rpc_method_handler(
                    servicer.VerifyTurn,
                    request_deserializer=helloworld__pb2.VerifyTurnRequest.FromString,
                    response_serializer=helloworld__pb2.HelloReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld.Greeter', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter(object):
    """The greeting service definition.
    """

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/Login',
            helloworld__pb2.LoginRequest.SerializeToString,
            helloworld__pb2.LoginReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/TurnAction',
            helloworld__pb2.TurnRequest.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def VerifyTurn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld.Greeter/VerifyTurn',
            helloworld__pb2.VerifyTurnRequest.SerializeToString,
            helloworld__pb2.HelloReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
