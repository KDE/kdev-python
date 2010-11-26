###########################################################################
#    Copyright (C) 2007 by Piyush Verma
#    <piyush@survived>                                                             
#
#-- This program is free software; you can redistribute it and/or
#-- modify it under the terms of the GNU General Public License
#-- as published by the Free Software Foundation; either version 2
#-- of the License, or (at your option) any later version.
#--
#-- This program is distributed in the hope that it will be useful,
#-- but WITHOUT ANY WARRANTY; without even the implied warranty of
#-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#-- GNU General Public License for more details.
#--
#-- You should have received a copy of the GNU General Public License
#-- along with this program; if not, write to the Free Software
#-- Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
#-- 02110-1301, USA.
#
###########################################################################
import os
import sys
import time
from threading import Thread
import logging

from log import logger_factory

class forlist(Thread):
    def __init__ (self):
        Thread.__init__(self)
        if(i < 3):
            y = logger_factory('stderr','','DEBUG','')
            self.run()
        else:
            y = logger_factory('stderr','','WARNING','')
            self.run2()
        logging.debug('Checking')
    def run2(self):
        print i
    def run(self):
        print i
for i in range(10):
   current = forlist()
