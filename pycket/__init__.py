# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 Nicolargo <nicolas@nicolargo.com>
#

__appname__ = "pycket"
__version__ = '0.1'
__author__ = 'Nicolas Hennion <nicolas@nicolargo.com>'
__license__ = 'MIT'

from .pycket import *
from .telemetry_packet import *

__all__ = [
    # Exceptions
    "PycketError",
    # Classes
    "Pycket", "TelemetryPacket"
    ]
