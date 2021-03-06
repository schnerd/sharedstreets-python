# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: speeds.proto

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
  name='speeds.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0cspeeds.proto\"G\n\x0eTemporalPeriod\x12\x1f\n\nperiodSize\x18\x01 \x01(\x0e\x32\x0b.PeriodSize\x12\x14\n\x0cperiodOffset\x18\x02 \x01(\x04\"X\n\x0bWeeklyCycle\x12\x0c\n\x04year\x18\x01 \x01(\r\x12\r\n\x05month\x18\x02 \x01(\r\x12\x0b\n\x03\x64\x61y\x18\x03 \x01(\r\x12\x1f\n\nperiodSize\x18\x04 \x01(\x0e\x32\x0b.PeriodSize\"<\n\x0eSpeedHistogram\x12\x10\n\x08speedBin\x18\x01 \x03(\r\x12\x18\n\x10observationCount\x18\x02 \x03(\r\"R\n\x16SpeedHistogramByPeriod\x12\x14\n\x0cperiodOffset\x18\x01 \x03(\r\x12\"\n\thistogram\x18\x02 \x03(\x0b\x32\x0f.SpeedHistogram\"O\n\x0cSpeedSummary\x12\x11\n\tmeanSpead\x18\x01 \x01(\r\x12\x12\n\npercentile\x18\x02 \x03(\r\x12\x18\n\x10observationCount\x18\x03 \x03(\r\"Q\n\x14SpeedSummaryByPeriod\x12\x14\n\x0cperiodOffset\x18\x01 \x03(\r\x12#\n\x0cspeedSummary\x18\x03 \x03(\x0b\x32\r.SpeedSummary\"\x91\x02\n\x19SharedStreetsWeeklySpeeds\x12\x13\n\x0breferenceId\x18\x01 \x01(\t\x12\x1f\n\nperiodSize\x18\x02 \x01(\x0e\x32\x0b.PeriodSize\x12\x14\n\x0cscaledCounts\x18\x03 \x01(\x08\x12\x17\n\x0freferenceLength\x18\x04 \x01(\x04\x12\x14\n\x0cnumberOfBins\x18\x05 \x01(\r\x12\x13\n\x0b\x62inPosition\x18\x06 \x03(\r\x12/\n\x0espeedsByPeriod\x18\x07 \x03(\x0b\x32\x17.SpeedHistogramByPeriod\x12\x33\n\x14speedSummaryByPeriod\x18\x08 \x03(\x0b\x32\x15.SpeedSummaryByPeriod*\xfb\x01\n\nPeriodSize\x12\r\n\tOneSecond\x10\x00\x12\x0f\n\x0b\x46iveSeconds\x10\x01\x12\x0e\n\nTenSeconds\x10\x02\x12\x12\n\x0e\x46ifteenSeconds\x10\x03\x12\x11\n\rThirtySeconds\x10\x04\x12\r\n\tOneMinute\x10\x05\x12\x0f\n\x0b\x46iveMinutes\x10\x06\x12\x0e\n\nTenMinutes\x10\x07\x12\x12\n\x0e\x46ifteenMinutes\x10\x08\x12\x11\n\rThirtyMinutes\x10\t\x12\x0b\n\x07OneHour\x10\n\x12\n\n\x06OneDay\x10\x0b\x12\x0b\n\x07OneWeek\x10\x0c\x12\x0c\n\x08OneMonth\x10\r\x12\x0b\n\x07OneYear\x10\x0e\x42\x1a\x42\x18SharedStreetsSpeedsProtob\x06proto3')
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
  serialized_start=766,
  serialized_end=1017,
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



_TEMPORALPERIOD = _descriptor.Descriptor(
  name='TemporalPeriod',
  full_name='TemporalPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='periodSize', full_name='TemporalPeriod.periodSize', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='periodOffset', full_name='TemporalPeriod.periodOffset', index=1,
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
  ],
  serialized_start=16,
  serialized_end=87,
)


_WEEKLYCYCLE = _descriptor.Descriptor(
  name='WeeklyCycle',
  full_name='WeeklyCycle',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='year', full_name='WeeklyCycle.year', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='month', full_name='WeeklyCycle.month', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='day', full_name='WeeklyCycle.day', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='periodSize', full_name='WeeklyCycle.periodSize', index=3,
      number=4, type=14, cpp_type=8, label=1,
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
  ],
  serialized_start=89,
  serialized_end=177,
)


_SPEEDHISTOGRAM = _descriptor.Descriptor(
  name='SpeedHistogram',
  full_name='SpeedHistogram',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='speedBin', full_name='SpeedHistogram.speedBin', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='observationCount', full_name='SpeedHistogram.observationCount', index=1,
      number=2, type=13, cpp_type=3, label=3,
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
  serialized_start=179,
  serialized_end=239,
)


_SPEEDHISTOGRAMBYPERIOD = _descriptor.Descriptor(
  name='SpeedHistogramByPeriod',
  full_name='SpeedHistogramByPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='periodOffset', full_name='SpeedHistogramByPeriod.periodOffset', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='histogram', full_name='SpeedHistogramByPeriod.histogram', index=1,
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
  serialized_start=241,
  serialized_end=323,
)


_SPEEDSUMMARY = _descriptor.Descriptor(
  name='SpeedSummary',
  full_name='SpeedSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meanSpead', full_name='SpeedSummary.meanSpead', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='percentile', full_name='SpeedSummary.percentile', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='observationCount', full_name='SpeedSummary.observationCount', index=2,
      number=3, type=13, cpp_type=3, label=3,
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
  serialized_start=325,
  serialized_end=404,
)


_SPEEDSUMMARYBYPERIOD = _descriptor.Descriptor(
  name='SpeedSummaryByPeriod',
  full_name='SpeedSummaryByPeriod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='periodOffset', full_name='SpeedSummaryByPeriod.periodOffset', index=0,
      number=1, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speedSummary', full_name='SpeedSummaryByPeriod.speedSummary', index=1,
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
  serialized_start=406,
  serialized_end=487,
)


_SHAREDSTREETSWEEKLYSPEEDS = _descriptor.Descriptor(
  name='SharedStreetsWeeklySpeeds',
  full_name='SharedStreetsWeeklySpeeds',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='SharedStreetsWeeklySpeeds.referenceId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='periodSize', full_name='SharedStreetsWeeklySpeeds.periodSize', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scaledCounts', full_name='SharedStreetsWeeklySpeeds.scaledCounts', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceLength', full_name='SharedStreetsWeeklySpeeds.referenceLength', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numberOfBins', full_name='SharedStreetsWeeklySpeeds.numberOfBins', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binPosition', full_name='SharedStreetsWeeklySpeeds.binPosition', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speedsByPeriod', full_name='SharedStreetsWeeklySpeeds.speedsByPeriod', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speedSummaryByPeriod', full_name='SharedStreetsWeeklySpeeds.speedSummaryByPeriod', index=7,
      number=8, type=11, cpp_type=10, label=3,
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
  serialized_start=490,
  serialized_end=763,
)

_TEMPORALPERIOD.fields_by_name['periodSize'].enum_type = _PERIODSIZE
_WEEKLYCYCLE.fields_by_name['periodSize'].enum_type = _PERIODSIZE
_SPEEDHISTOGRAMBYPERIOD.fields_by_name['histogram'].message_type = _SPEEDHISTOGRAM
_SPEEDSUMMARYBYPERIOD.fields_by_name['speedSummary'].message_type = _SPEEDSUMMARY
_SHAREDSTREETSWEEKLYSPEEDS.fields_by_name['periodSize'].enum_type = _PERIODSIZE
_SHAREDSTREETSWEEKLYSPEEDS.fields_by_name['speedsByPeriod'].message_type = _SPEEDHISTOGRAMBYPERIOD
_SHAREDSTREETSWEEKLYSPEEDS.fields_by_name['speedSummaryByPeriod'].message_type = _SPEEDSUMMARYBYPERIOD
DESCRIPTOR.message_types_by_name['TemporalPeriod'] = _TEMPORALPERIOD
DESCRIPTOR.message_types_by_name['WeeklyCycle'] = _WEEKLYCYCLE
DESCRIPTOR.message_types_by_name['SpeedHistogram'] = _SPEEDHISTOGRAM
DESCRIPTOR.message_types_by_name['SpeedHistogramByPeriod'] = _SPEEDHISTOGRAMBYPERIOD
DESCRIPTOR.message_types_by_name['SpeedSummary'] = _SPEEDSUMMARY
DESCRIPTOR.message_types_by_name['SpeedSummaryByPeriod'] = _SPEEDSUMMARYBYPERIOD
DESCRIPTOR.message_types_by_name['SharedStreetsWeeklySpeeds'] = _SHAREDSTREETSWEEKLYSPEEDS
DESCRIPTOR.enum_types_by_name['PeriodSize'] = _PERIODSIZE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TemporalPeriod = _reflection.GeneratedProtocolMessageType('TemporalPeriod', (_message.Message,), dict(
  DESCRIPTOR = _TEMPORALPERIOD,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:TemporalPeriod)
  ))
_sym_db.RegisterMessage(TemporalPeriod)

WeeklyCycle = _reflection.GeneratedProtocolMessageType('WeeklyCycle', (_message.Message,), dict(
  DESCRIPTOR = _WEEKLYCYCLE,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:WeeklyCycle)
  ))
_sym_db.RegisterMessage(WeeklyCycle)

SpeedHistogram = _reflection.GeneratedProtocolMessageType('SpeedHistogram', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDHISTOGRAM,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:SpeedHistogram)
  ))
_sym_db.RegisterMessage(SpeedHistogram)

SpeedHistogramByPeriod = _reflection.GeneratedProtocolMessageType('SpeedHistogramByPeriod', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDHISTOGRAMBYPERIOD,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:SpeedHistogramByPeriod)
  ))
_sym_db.RegisterMessage(SpeedHistogramByPeriod)

SpeedSummary = _reflection.GeneratedProtocolMessageType('SpeedSummary', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDSUMMARY,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:SpeedSummary)
  ))
_sym_db.RegisterMessage(SpeedSummary)

SpeedSummaryByPeriod = _reflection.GeneratedProtocolMessageType('SpeedSummaryByPeriod', (_message.Message,), dict(
  DESCRIPTOR = _SPEEDSUMMARYBYPERIOD,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:SpeedSummaryByPeriod)
  ))
_sym_db.RegisterMessage(SpeedSummaryByPeriod)

SharedStreetsWeeklySpeeds = _reflection.GeneratedProtocolMessageType('SharedStreetsWeeklySpeeds', (_message.Message,), dict(
  DESCRIPTOR = _SHAREDSTREETSWEEKLYSPEEDS,
  __module__ = 'speeds_pb2'
  # @@protoc_insertion_point(class_scope:SharedStreetsWeeklySpeeds)
  ))
_sym_db.RegisterMessage(SharedStreetsWeeklySpeeds)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('B\030SharedStreetsSpeedsProto'))
# @@protoc_insertion_point(module_scope)
