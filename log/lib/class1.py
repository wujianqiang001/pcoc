#!/usr/bin/env python
# coding=utf-8
import time
from functools import partial
from config import logger,message
def log(a,b,c):
    logger.info(message,a,b,c)

tp = partial(log,"A","B")
tp("C")
time.sleep(10)
logger.info("test-----c")