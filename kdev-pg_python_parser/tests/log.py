#!/usr/bin/env python
import logging
import auxillary

# Create Logger with "spam_application"
logger = logging.getLogger("spam_application")
logger.setLevel(logging.DEBUG)

# Create File Handler and set leevl to DEBUG
fh = logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)

# Create Console Handler and set level to DEBUG
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# Create Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

#Add formatter to ch
ch.setFormatter(formatter)

#Add formatter to fh
fh.setFormatter(formatter)

#add fh to logger
logger.addHandler(fh)

#Add ch to logger
logger.addHandler(ch)

logger.info("Creating an Instance of auxillary.Auxillary")
a= auxillary.Auxillary()
logger.info("Created an Instance of auxillary.Auxillary")
logger.info("Calling _add")
a._add()
logger.info("Called _add")
logger.info("Calling function")
auxillary.function()
logger.info("Called function")
