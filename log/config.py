#!/usr/bin/env python
# coding=utf-8
import logging
import logging.config

logging.config.fileConfig("logger.ini")
logger = logging.getLogger("access")
message = """
a = %s
b = %s
c = %s
"""