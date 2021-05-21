# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Nicolargo <nicolas@nicolargo.com>
#

from pycket import Pycket


class TelemetryFrame(Pycket):
    """Packet Telemetry Encoder (PTME)"""

    # Frame size in bytes (with header)
    _size = 1024

    # Size are in bits
    _packet = [{'description': 'synchro_marker',
                'size': 32},
               {'description': 'version',
                'size': 2},
               {'description': 'space_craft_id',
                'size': 10},
               {'description': 'virtual_channel_id',
                'size': 3},
               {'description': 'opcf_flag',
                'size': 1,
                'display': 'dec'},
               {'description': 'master_channel_frame_count',
                'size': 8},
               {'description': 'virtual_channel_frame_count',
                'size': 8},
               {'description': 'frame_data_field_status',
                'size': 16},

               {'description': 'secondary_header_flag',
                'size': 1},
               {'description': 'sync_flag',
                'size': 1},
               {'description': 'packet_order_flag',
                'size': 1},
               {'description': 'segment_length_id',
                'size': 2},
               {'description': 'first_header_pointer',
                'size': 11},

               {'description': 'secondary_header_version',
                'size': 2},
               {'description': 'secondary_header_length',
                'size': 6},
               {'description': 'virtual_channel_frame_counter',
                'size': 24},

               {'description': 'data',
                # A size of None go to te end of the frame (need the _size variable to be defined)
                'size': None,
                # Do not display the data
                'display': None}]



class TelemetryFrameList(object):
    """A list of TelemetryFrame"""

    def __init__(self):
        """ Init a list of TelemetryFrame
        """
        self._frame_list = []

    def for_human(self, header=True, value=True):
        """Return a human representation of the current list of telemetry

        header: True ==> return the header
        value: True ==> add value in the header"""
        ret = ''
        if header:
            ret += self._frame_list[0]._for_human_header(value=value)
        for i in range(0, 10):
            ret += self._frame_list[i]._for_human_data()
            ret += '\n'

        return ret

    def read_from_file(self, file_name, display_while_reading=False, number=10):
        """Read a raw buffer from a file"""
        counter = 0
        with open(file_name, "rb") as file_descriptor:
            while counter < number:
                new_frame = TelemetryFrame()
                raw = file_descriptor.read(TelemetryFrame._size)
                if not raw:
                    break
                new_frame.read(raw)
                self._frame_list.append(new_frame)
                if display_while_reading:
                    print(new_frame.for_human(header=(counter==0), value=True))
                    counter += 1

        return self._frame_list
