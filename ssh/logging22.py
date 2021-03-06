# Copyright (C) 2011  Jeff Forcier <jeff@bitprophet.org>
#
# This file is part of ssh.
#
# 'ssh' is free software; you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 2.1 of the License, or (at your option)
# any later version.
#
# 'ssh' is distrubuted in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with 'ssh'; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Suite 500, Boston, MA  02110-1335  USA.

"""
Stub out logging on python < 2.3.
"""


DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50


def getLogger(name):
    return _logger


class logger (object):
    def __init__(self):
        self.handlers = [ ]
        self.level = ERROR

    def setLevel(self, level):
        self.level = level

    def addHandler(self, h):
        self.handlers.append(h)

    def addFilter(self, filter):
        pass
        
    def log(self, level, text):
        if level >= self.level:
            for h in self.handlers:
                h.f.write(text + '\n')
                h.f.flush()

class StreamHandler (object):
    def __init__(self, f):
        self.f = f

    def setFormatter(self, f):
        pass

class Formatter (object):
    def __init__(self, x, y):
        pass

_logger = logger()
