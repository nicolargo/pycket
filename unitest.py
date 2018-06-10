#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Nicolargo <nicolas@nicolargo.com>
#

import unittest
import pycket


class TestPycket(unittest.TestCase):
    """Test Glances class."""

    def test_001_ok(self):
        print('=' * 80)
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
        self.assertEqual(ret[0]['raw_value'], '000')
        self.assertEqual(ret[2]['value'], 1)

    def test_002_packet_too_short(self):
        print('=' * 80)
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
        raw = pycket.bitstostring('0000110000000000101000000000000010000000000')
        try:
            pyc.read(raw)
        except pycket.PycketError as e:
            print(e)
            self.assertTrue('Bad packet size' in e.message)
        raw = pycket.bitstostring('000011000000000010100000000000001000000000000000000000000000000000000000')
        try:
            pyc.read(raw)
        except pycket.PycketError as e:
            print(e)
            self.assertTrue('Bad packet size' in e.message)


if __name__ == '__main__':
    unittest.main()
