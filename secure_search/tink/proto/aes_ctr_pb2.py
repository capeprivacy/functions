# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tink/proto/aes_ctr.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tink/proto/aes_ctr.proto',
  package='google.crypto.tink',
  syntax='proto3',
  serialized_options=b'\n\034com.google.crypto.tink.protoP\001Z-github.com/google/tink/proto/aes_ctr_go_proto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18tink/proto/aes_ctr.proto\x12\x12google.crypto.tink\"\x1f\n\x0c\x41\x65sCtrParams\x12\x0f\n\x07iv_size\x18\x01 \x01(\r\"U\n\x0f\x41\x65sCtrKeyFormat\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32 .google.crypto.tink.AesCtrParams\x12\x10\n\x08key_size\x18\x02 \x01(\r\"a\n\tAesCtrKey\x12\x0f\n\x07version\x18\x01 \x01(\r\x12\x30\n\x06params\x18\x02 \x01(\x0b\x32 .google.crypto.tink.AesCtrParams\x12\x11\n\tkey_value\x18\x03 \x01(\x0c\x42O\n\x1c\x63om.google.crypto.tink.protoP\x01Z-github.com/google/tink/proto/aes_ctr_go_protob\x06proto3'
)




_AESCTRPARAMS = _descriptor.Descriptor(
  name='AesCtrParams',
  full_name='google.crypto.tink.AesCtrParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='iv_size', full_name='google.crypto.tink.AesCtrParams.iv_size', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=48,
  serialized_end=79,
)


_AESCTRKEYFORMAT = _descriptor.Descriptor(
  name='AesCtrKeyFormat',
  full_name='google.crypto.tink.AesCtrKeyFormat',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='params', full_name='google.crypto.tink.AesCtrKeyFormat.params', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_size', full_name='google.crypto.tink.AesCtrKeyFormat.key_size', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=81,
  serialized_end=166,
)


_AESCTRKEY = _descriptor.Descriptor(
  name='AesCtrKey',
  full_name='google.crypto.tink.AesCtrKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='google.crypto.tink.AesCtrKey.version', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='google.crypto.tink.AesCtrKey.params', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key_value', full_name='google.crypto.tink.AesCtrKey.key_value', index=2,
      number=3, type=12, cpp_type=9, label=1,
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
  serialized_start=168,
  serialized_end=265,
)

_AESCTRKEYFORMAT.fields_by_name['params'].message_type = _AESCTRPARAMS
_AESCTRKEY.fields_by_name['params'].message_type = _AESCTRPARAMS
DESCRIPTOR.message_types_by_name['AesCtrParams'] = _AESCTRPARAMS
DESCRIPTOR.message_types_by_name['AesCtrKeyFormat'] = _AESCTRKEYFORMAT
DESCRIPTOR.message_types_by_name['AesCtrKey'] = _AESCTRKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AesCtrParams = _reflection.GeneratedProtocolMessageType('AesCtrParams', (_message.Message,), {
  'DESCRIPTOR' : _AESCTRPARAMS,
  '__module__' : 'tink.proto.aes_ctr_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.AesCtrParams)
  })
_sym_db.RegisterMessage(AesCtrParams)

AesCtrKeyFormat = _reflection.GeneratedProtocolMessageType('AesCtrKeyFormat', (_message.Message,), {
  'DESCRIPTOR' : _AESCTRKEYFORMAT,
  '__module__' : 'tink.proto.aes_ctr_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.AesCtrKeyFormat)
  })
_sym_db.RegisterMessage(AesCtrKeyFormat)

AesCtrKey = _reflection.GeneratedProtocolMessageType('AesCtrKey', (_message.Message,), {
  'DESCRIPTOR' : _AESCTRKEY,
  '__module__' : 'tink.proto.aes_ctr_pb2'
  # @@protoc_insertion_point(class_scope:google.crypto.tink.AesCtrKey)
  })
_sym_db.RegisterMessage(AesCtrKey)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
