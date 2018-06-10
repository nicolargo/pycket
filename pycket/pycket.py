# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Nicolargo <nicolas@nicolargo.com>
#

from pprint import pformat


class PycketError(Exception):
    pass


class Pycket(object):
    """A packet of bits"""

    def __init__(self, packet):
        """ Init a packet

        packet: Packet definition (list of dicts)
        """
        self._packet = packet

    def __str__(self):
        return pformat(self._packet)

    def for_human(self, header=True, value=True):
        """Return a human representatio of the current packet

        header: True ==> return the header
        value: True ==> add value in the header"""
        ret = ''
        if header:
            ret += self._for_human_header(value=value)
        ret += self._for_human_data()
        return ret

    def _for_human_header(self, value=True):
        head = ret = ''
        first = True
        for i in self._packet:
            if first:
                head += '|'
                first = False
            ret += head[:-1] + '┌ ' + i['description']
            if value:
                ret += ' = {}'.format(i['value'])
            ret += '\n'
            head += ' ' * i['size'] + '|'
        return ret

    def _for_human_data(self):
        ret = ''
        first = True
        for i in self._packet:
            if first:
                ret += '|'
                first = False
            ret += i['raw_value']
            ret += '|'
        return ret

    def read(self, raw):
        """Read a raw buffer (string) and return a packet description"""
        # Convert the buffer to a string of bits
        bits = stringtobits(raw)
        # Add the raw_value and value to the packet
        self._add_raw_value(bits)
        self._raw_to_value()
        return self._packet

    def _add_raw_value(self, bits):
        """Take bits buffer (string of bits) & add raw_value to the packet"""
        begin = end = 0
        for i in self._packet:
            end += i['size']
            i['raw_value'] = bits[begin:end]
            begin = end
        if end != len(bits):
            err = 'Bad packet size'
            err += ' (buffer is to {}).'.format('short' if end > len(bits) else 'long')
            err += ' Buffer size is {} bits, expected {}.'.format(len(bits), end)
            raise PycketError(err)

    def _raw_to_value(self):
        """Convert raw_value to value (human readable)"""
        for i in self._packet:
            i['value'] = int(i['raw_value'], 2)


def bitstostring(b):
    # Source: https://stackoverflow.com/questions/9916334/bits-to-string-python
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)] * 8))


def stringtobits(s):
    # Source:https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa
    result = ''
    for c in s:
        bits = bin(ord(c))[2:]
        result += '00000000'[len(bits):] + bits
    return result
