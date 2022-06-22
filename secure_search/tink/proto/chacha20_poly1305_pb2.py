# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tink/proto/chacha20_poly1305.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tink/proto/chacha20_poly1305.proto',
  package='google.crypto.tink',
  syntax='proto3',
  serialized_options=b'\n\034com.google.crypto.tink.protoP\001Z7github.com/google/tink/proto/chacha20_poly1305_go_proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"tink/proto/chacha20_poly1305.proto\x12\x12google.crypto.tink\"\x1b\n\x19\x43haCha20Poly1305KeyFormat\"9\n\x13\x43haCha20Poly1305Key\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x11\n\tkey_value\x18\x02 \x01(\x0c\x42Y\n\x1c\x63om.google.crypto.tink.protoP\x01Z7github.com/google/tink/proto/chacha20_poly1305_go_protob\x06proto3'
)




_CHACHA20POLY1305KEYFORMAT = _descriptor.Descriptor(
  name='ChaCha20Poly1305KeyFormat',
  full_name='google.crypto.tink.ChaCha20Poly1305KeyFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=85,
)


_CHACHA20POLY1305KEY = _descriptor.Descriptor(
  name='ChaCha20Poly1305Key',
  full_name='google.crypto.tink.ChaCha20Poly1305Key',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.crypto.tink.ChaCha20Poly1305Key.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_value', full_name='google.crypto.tink.ChaCha20Poly1305Key.key_value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=87,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['ChaCha20Poly1305KeyFormat'] = _CHACHA20POLY1305KEYFORMAT
DESCRIPTOR.message_types_by_name['ChaCha20Poly1305Key'] = _CHACHA20POLY1305KEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChaCha20Poly1305KeyFormat = _reflection.GeneratedProtocolMessageType('ChaCha20Poly1305KeyFormat', (_message.Message,), {
  'DESCRIPTOR' : _CHACHA20POLY1305KEYFORMAT,
  '__module__' : 'tink.proto.chacha20_poly1305_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.ChaCha20Poly1305KeyFormat)
  })
_sym_db.RegisterMessage(ChaCha20Poly1305KeyFormat)

ChaCha20Poly1305Key = _reflection.GeneratedProtocolMessageType('ChaCha20Poly1305Key', (_message.Message,), {
  'DESCRIPTOR' : _CHACHA20POLY1305KEY,
  '__module__' : 'tink.proto.chacha20_poly1305_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.ChaCha20Poly1305Key)
  })
_sym_db.RegisterMessage(ChaCha20Poly1305Key)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)