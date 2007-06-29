###########################################################################
#    Copyright (C) 2007 by Piyush Verma,Sapphire Mobile Systems,0091-11-41553035,0091-981261908                                      
#    <piyush@survived>                                                             
#
# Copyright: See COPYING file that comes with this distribution
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
