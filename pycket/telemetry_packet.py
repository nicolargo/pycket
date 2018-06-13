# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Nicolargo <nicolas@nicolargo.com>
#

from pycket import Pycket


class TelemetryPacket(Pycket):
    """A CCSDS 203.0-B-2 packet"""

    _packet = [{'description': 'version_number',
                'size': 3},
               {'description': 'type',
                'size': 1},
               {'description': 'data_field_error_flag',
                'size': 1},
               {'description': 'application_process_id',
                'size': 11,
                'display': 'dec'},
               {'description': 'grouping_flags',
                'size': 2},
               {'description': 'source_sequence_count',
                'size': 14},
               {'description': 'packet_length',
                'size': 16}]
