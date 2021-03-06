# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: linear_references.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='linear_references.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x17linear_references.proto\"V\n\x0fLinearReference\x12\x15\n\rstartDistance\x18\x01 \x01(\x04\x12\x15\n\x0b\x65ndDistance\x18\x02 \x01(\x04H\x00\x42\x15\n\x13\x65ndDistance_present\"s\n\x1dSharedStreetsLinearReferences\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x17\n\x0freferenceLength\x18\x02 \x01(\x04\x12$\n\nreferences\x18\x03 \x03(\x0b\x32\x10.LinearReference\"9\n\x07\x44\x61taBin\x12\x10\n\x08\x64\x61taType\x18\x01 \x03(\t\x12\r\n\x05\x63ount\x18\x02 \x03(\x04\x12\r\n\x05value\x18\x03 \x03(\x01\"B\n\x12\x42innedPeriodicData\x12\x14\n\x0cperiodOffset\x18\x01 \x03(\r\x12\x16\n\x04\x62ins\x18\x02 \x03(\x0b\x32\x08.DataBin\"\xac\x01\n#SharedStreetsBinnedLinearReferences\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x14\n\x0cscaledCounts\x18\x02 \x01(\x08\x12\x17\n\x0freferenceLength\x18\x03 \x01(\x04\x12\x14\n\x0cnumberOfBins\x18\x04 \x01(\r\x12\x13\n\x0b\x62inPosition\x18\x05 \x03(\r\x12\x16\n\x04\x62ins\x18\x06 \x03(\x0b\x32\x08.DataBin\"\xec\x01\n)SharedStreetsWeeklyBinnedLinearReferences\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x1f\n\nperiodSize\x18\x02 \x01(\x0e\x32\x0b.PeriodSize\x12\x14\n\x0cscaledCounts\x18\x03 \x01(\x08\x12\x17\n\x0freferenceLength\x18\x04 \x01(\x04\x12\x14\n\x0cnumberOfBins\x18\x05 \x01(\r\x12\x13\n\x0b\x62inPosition\x18\x06 \x03(\r\x12/\n\x12\x62innedPeriodicData\x18\x07 \x03(\x0b\x32\x13.BinnedPeriodicData*\xfb\x01\n\nPeriodSize\x12\r\n\tOneSecond\x10\x00\x12\x0f\n\x0b\x46iveSeconds\x10\x01\x12\x0e\n\nTenSeconds\x10\x02\x12\x12\n\x0e\x46ifteenSeconds\x10\x03\x12\x11\n\rThirtySeconds\x10\x04\x12\r\n\tOneMinute\x10\x05\x12\x0f\n\x0b\x46iveMinutes\x10\x06\x12\x0e\n\nTenMinutes\x10\x07\x12\x12\n\x0e\x46ifteenMinutes\x10\x08\x12\x11\n\rThirtyMinutes\x10\t\x12\x0b\n\x07OneHour\x10\n\x12\n\n\x06OneDay\x10\x0b\x12\x0b\n\x07OneWeek\x10\x0c\x12\x0c\n\x08OneMonth\x10\r\x12\x0b\n\x07OneYear\x10\x0e\x42$B\"SharedStreetsLinearReferencesProtob\x06proto3')
)

_PERIODSIZE = _descriptor.EnumDescriptor(
  name='PeriodSize',
  full_name='PeriodSize',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OneSecond', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FiveSeconds', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TenSeconds', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FifteenSeconds', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ThirtySeconds', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneMinute', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FiveMinutes', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TenMinutes', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FifteenMinutes', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ThirtyMinutes', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneHour', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneDay', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneWeek', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneMonth', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OneYear', index=14, number=14,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=774,
  serialized_end=1025,
)
_sym_db.RegisterEnumDescriptor(_PERIODSIZE)

PeriodSize = enum_type_wrapper.EnumTypeWrapper(_PERIODSIZE)
OneSecond = 0
FiveSeconds = 1
TenSeconds = 2
FifteenSeconds = 3
ThirtySeconds = 4
OneMinute = 5
FiveMinutes = 6
TenMinutes = 7
FifteenMinutes = 8
ThirtyMinutes = 9
OneHour = 10
OneDay = 11
OneWeek = 12
OneMonth = 13
OneYear = 14



_LINEARREFERENCE = _descriptor.Descriptor(
  name='LinearReference',
  full_name='LinearReference',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startDistance', full_name='LinearReference.startDistance', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endDistance', full_name='LinearReference.endDistance', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='endDistance_present', full_name='LinearReference.endDistance_present',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=27,
  serialized_end=113,
)


_SHAREDSTREETSLINEARREFERENCES = _descriptor.Descriptor(
  name='SharedStreetsLinearReferences',
  full_name='SharedStreetsLinearReferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='SharedStreetsLinearReferences.referenceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceLength', full_name='SharedStreetsLinearReferences.referenceLength', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='references', full_name='SharedStreetsLinearReferences.references', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=230,
)


_DATABIN = _descriptor.Descriptor(
  name='DataBin',
  full_name='DataBin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dataType', full_name='DataBin.dataType', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='DataBin.count', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='DataBin.value', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=289,
)


_BINNEDPERIODICDATA = _descriptor.Descriptor(
  name='BinnedPeriodicData',
  full_name='BinnedPeriodicData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='periodOffset', full_name='BinnedPeriodicData.periodOffset', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bins', full_name='BinnedPeriodicData.bins', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=291,
  serialized_end=357,
)


_SHAREDSTREETSBINNEDLINEARREFERENCES = _descriptor.Descriptor(
  name='SharedStreetsBinnedLinearReferences',
  full_name='SharedStreetsBinnedLinearReferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='SharedStreetsBinnedLinearReferences.referenceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaledCounts', full_name='SharedStreetsBinnedLinearReferences.scaledCounts', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceLength', full_name='SharedStreetsBinnedLinearReferences.referenceLength', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numberOfBins', full_name='SharedStreetsBinnedLinearReferences.numberOfBins', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binPosition', full_name='SharedStreetsBinnedLinearReferences.binPosition', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bins', full_name='SharedStreetsBinnedLinearReferences.bins', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=360,
  serialized_end=532,
)


_SHAREDSTREETSWEEKLYBINNEDLINEARREFERENCES = _descriptor.Descriptor(
  name='SharedStreetsWeeklyBinnedLinearReferences',
  full_name='SharedStreetsWeeklyBinnedLinearReferences',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='SharedStreetsWeeklyBinnedLinearReferences.referenceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='periodSize', full_name='SharedStreetsWeeklyBinnedLinearReferences.periodSize', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaledCounts', full_name='SharedStreetsWeeklyBinnedLinearReferences.scaledCounts', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceLength', full_name='SharedStreetsWeeklyBinnedLinearReferences.referenceLength', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numberOfBins', full_name='SharedStreetsWeeklyBinnedLinearReferences.numberOfBins', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binPosition', full_name='SharedStreetsWeeklyBinnedLinearReferences.binPosition', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binnedPeriodicData', full_name='SharedStreetsWeeklyBinnedLinearReferences.binnedPeriodicData', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=535,
  serialized_end=771,
)

_LINEARREFERENCE.oneofs_by_name['endDistance_present'].fields.append(
  _LINEARREFERENCE.fields_by_name['endDistance'])
_LINEARREFERENCE.fields_by_name['endDistance'].containing_oneof = _LINEARREFERENCE.oneofs_by_name['endDistance_present']
_SHAREDSTREETSLINEARREFERENCES.fields_by_name['references'].message_type = _LINEARREFERENCE
_BINNEDPERIODICDATA.fields_by_name['bins'].message_type = _DATABIN
_SHAREDSTREETSBINNEDLINEARREFERENCES.fields_by_name['bins'].message_type = _DATABIN
_SHAREDSTREETSWEEKLYBINNEDLINEARREFERENCES.fields_by_name['periodSize'].enum_type = _PERIODSIZE
_SHAREDSTREETSWEEKLYBINNEDLINEARREFERENCES.fields_by_name['binnedPeriodicData'].message_type = _BINNEDPERIODICDATA
DESCRIPTOR.message_types_by_name['LinearReference'] = _LINEARREFERENCE
DESCRIPTOR.message_types_by_name['SharedStreetsLinearReferences'] = _SHAREDSTREETSLINEARREFERENCES
DESCRIPTOR.message_types_by_name['DataBin'] = _DATABIN
DESCRIPTOR.message_types_by_name['BinnedPeriodicData'] = _BINNEDPERIODICDATA
DESCRIPTOR.message_types_by_name['SharedStreetsBinnedLinearReferences'] = _SHAREDSTREETSBINNEDLINEARREFERENCES
DESCRIPTOR.message_types_by_name['SharedStreetsWeeklyBinnedLinearReferences'] = _SHAREDSTREETSWEEKLYBINNEDLINEARREFERENCES
DESCRIPTOR.enum_types_by_name['PeriodSize'] = _PERIODSIZE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinearReference = _reflection.GeneratedProtocolMessageType('LinearReference', (_message.Message,), dict(
  DESCRIPTOR = _LINEARREFERENCE,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:LinearReference)
  ))
_sym_db.RegisterMessage(LinearReference)

SharedStreetsLinearReferences = _reflection.GeneratedProtocolMessageType('SharedStreetsLinearReferences', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSLINEARREFERENCES,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsLinearReferences)
  ))
_sym_db.RegisterMessage(SharedStreetsLinearReferences)

DataBin = _reflection.GeneratedProtocolMessageType('DataBin', (_message.Message,), dict(
  DESCRIPTOR = _DATABIN,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:DataBin)
  ))
_sym_db.RegisterMessage(DataBin)

BinnedPeriodicData = _reflection.GeneratedProtocolMessageType('BinnedPeriodicData', (_message.Message,), dict(
  DESCRIPTOR = _BINNEDPERIODICDATA,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:BinnedPeriodicData)
  ))
_sym_db.RegisterMessage(BinnedPeriodicData)

SharedStreetsBinnedLinearReferences = _reflection.GeneratedProtocolMessageType('SharedStreetsBinnedLinearReferences', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSBINNEDLINEARREFERENCES,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsBinnedLinearReferences)
  ))
_sym_db.RegisterMessage(SharedStreetsBinnedLinearReferences)

SharedStreetsWeeklyBinnedLinearReferences = _reflection.GeneratedProtocolMessageType('SharedStreetsWeeklyBinnedLinearReferences', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSWEEKLYBINNEDLINEARREFERENCES,
  __module__ = 'linear_references_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsWeeklyBinnedLinearReferences)
  ))
_sym_db.RegisterMessage(SharedStreetsWeeklyBinnedLinearReferences)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\"SharedStreetsLinearReferencesProto'))
# @@protoc_insertion_point(module_scope)
