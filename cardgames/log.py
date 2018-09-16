#!/usr/bin/python3

import logging

# instead of setting this level here, we can grab it from the command line.
loglevel = 'DEBUG'

logging.basicConfig(level=getattr(logging, loglevel.upper()))
logger = logging.getLogger(__name__)
