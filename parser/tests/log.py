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
import logging
import logging.handlers
import sys

def logger_factory(logtype='syslog', logfile=None, level='WARNING',
                   logid='logg'):
    logger = logging.getLogger(logid)
    logtype = logtype.lower()
    if logtype == 'file':
        hdlr = logging.FileHandler(logfile)
    elif logtype in ['syslog', 'unix']:
        hdlr = logging.handlers.SysLogHandler('/dev/log')
    elif logtype in ['stderr']:
        hdlr = logging.StreamHandler(sys.stderr)
    else:
        print "No worthy LogType Found In the Arguements, pLease Check the Parameter: %s" % logtype
    format = ' [%(module)s] %(levelname)s: %(message)s'
    if logtype in ['file', 'stderr']:
        format = '%(asctime)s ' + format 
    datefmt = ''
    if logtype == 'stderr':
        datefmt = '%X'
    level = level.upper()
    if level in ['ALL']:
        logger.setLevel(logging.DEBUG)
    elif level == 'INFO':
        logger.setLevel(logging.INFO)
    elif level == 'ERROR':
        logger.setLevel(logging.ERROR)
    elif level == 'CRITICAL':
        logger.setLevel(logging.CRITICAL)
    elif level == 'WARNING':
        logger.setLevel(logging.WARNING)
    else:
        logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format,datefmt)
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    return logger
