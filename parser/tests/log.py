###########################################################################
#    Copyright (C) 2007 by Piyush Verma,Sapphire Mobile Systems,0091-11-41553035,0091-981261908                                      
#    <piyush@survived>                                                             
#
# Copyright: See COPYING file that comes with this distribution
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
