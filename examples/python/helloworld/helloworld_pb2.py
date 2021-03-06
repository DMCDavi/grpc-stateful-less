# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\x12\nhelloworld\"2\n\x0cLoginRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"1\n\nLoginReply\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x12\n\nauth_token\x18\x02 \x01(\t\"\'\n\x11VerifyTurnRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\".\n\x0bTurnRequest\x12\x12\n\nauth_token\x18\x01 \x01(\t\x12\x0b\n\x03\x64ig\x18\x02 \x01(\t\"\x1c\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t\"<\n\tTurnReply\x12\x0f\n\x07playing\x18\x01 \x01(\t\x12\r\n\x05\x63\x61rds\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t2\xcd\x01\n\x07Greeter\x12;\n\x05Login\x12\x18.helloworld.LoginRequest\x1a\x16.helloworld.LoginReply\"\x00\x12>\n\nTurnAction\x12\x17.helloworld.TurnRequest\x1a\x15.helloworld.TurnReply\"\x00\x12\x45\n\nVerifyTurn\x12\x1d.helloworld.VerifyTurnRequest\x1a\x16.helloworld.HelloReply\"\x00\x42\x36\n\x1bio.grpc.examples.helloworldB\x0fHelloWorldProtoP\x01\xa2\x02\x03HLWb\x06proto3')



_LOGINREQUEST = DESCRIPTOR.message_types_by_name['LoginRequest']
_LOGINREPLY = DESCRIPTOR.message_types_by_name['LoginReply']
_VERIFYTURNREQUEST = DESCRIPTOR.message_types_by_name['VerifyTurnRequest']
_TURNREQUEST = DESCRIPTOR.message_types_by_name['TurnRequest']
_HELLOREQUEST = DESCRIPTOR.message_types_by_name['HelloRequest']
_HELLOREPLY = DESCRIPTOR.message_types_by_name['HelloReply']
_TURNREPLY = DESCRIPTOR.message_types_by_name['TurnReply']
LoginRequest = _reflection.GeneratedProtocolMessageType('LoginRequest', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LoginRequest)
  })
_sym_db.RegisterMessage(LoginRequest)

LoginReply = _reflection.GeneratedProtocolMessageType('LoginReply', (_message.Message,), {
  'DESCRIPTOR' : _LOGINREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.LoginReply)
  })
_sym_db.RegisterMessage(LoginReply)

VerifyTurnRequest = _reflection.GeneratedProtocolMessageType('VerifyTurnRequest', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYTURNREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.VerifyTurnRequest)
  })
_sym_db.RegisterMessage(VerifyTurnRequest)

TurnRequest = _reflection.GeneratedProtocolMessageType('TurnRequest', (_message.Message,), {
  'DESCRIPTOR' : _TURNREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.TurnRequest)
  })
_sym_db.RegisterMessage(TurnRequest)

HelloRequest = _reflection.GeneratedProtocolMessageType('HelloRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREQUEST,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloRequest)
  })
_sym_db.RegisterMessage(HelloRequest)

HelloReply = _reflection.GeneratedProtocolMessageType('HelloReply', (_message.Message,), {
  'DESCRIPTOR' : _HELLOREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.HelloReply)
  })
_sym_db.RegisterMessage(HelloReply)

TurnReply = _reflection.GeneratedProtocolMessageType('TurnReply', (_message.Message,), {
  'DESCRIPTOR' : _TURNREPLY,
  '__module__' : 'helloworld_pb2'
  # @@protoc_insertion_point(class_scope:helloworld.TurnReply)
  })
_sym_db.RegisterMessage(TurnReply)

_GREETER = DESCRIPTOR.services_by_name['Greeter']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033io.grpc.examples.helloworldB\017HelloWorldProtoP\001\242\002\003HLW'
  _LOGINREQUEST._serialized_start=32
  _LOGINREQUEST._serialized_end=82
  _LOGINREPLY._serialized_start=84
  _LOGINREPLY._serialized_end=133
  _VERIFYTURNREQUEST._serialized_start=135
  _VERIFYTURNREQUEST._serialized_end=174
  _TURNREQUEST._serialized_start=176
  _TURNREQUEST._serialized_end=222
  _HELLOREQUEST._serialized_start=224
  _HELLOREQUEST._serialized_end=252
  _HELLOREPLY._serialized_start=254
  _HELLOREPLY._serialized_end=283
  _TURNREPLY._serialized_start=285
  _TURNREPLY._serialized_end=345
  _GREETER._serialized_start=348
  _GREETER._serialized_end=553
# @@protoc_insertion_point(module_scope)
