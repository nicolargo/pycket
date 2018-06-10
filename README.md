# PyCket

Extract data from packet of bits.

Example:

```
import pycket

packet = [{'description': 'version_number',
           'size': 3},
          {'description': 'type',
           'size': 1},
          {'description': 'data_field_error_flag',
           'size': 1},
          {'description': 'application_process_id',
           'size': 11},
          {'description': 'grouping_flags',
           'size': 2},
          {'description': 'source_sequence_count',
           'size': 14},
          {'description': 'packet_length',
           'size': 16}]
pyc = pycket.Pycket(packet=packet)
raw = pycket.bitstostring('000011000000000010100000000000001000000000000000')
ret = pyc.read(raw)
print(pyc.for_human())
```

Will display:

```
┌ version_number = 0
|   ┌ type = 0
|   | ┌ data_field_error_flag = 1
|   | | ┌ application_process_id = 1024
|   | | |           ┌ grouping_flags = 2
|   | | |           |  ┌ source_sequence_count = 8192
|   | | |           |  |              ┌ packet_length = 32768
|000|0|1|10000000000|10|10000000000000|1000000000000000|
```
