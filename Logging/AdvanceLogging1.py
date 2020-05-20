
"""
Logging works very well but I could missleasd or confuse
if we import one file with logging(file 1) to another
file with logging(file 2) then file 2 also inherit the 
behavious of logging of file 1. We can avoid this situation by
using handlers by assigning logging to a variable and use 
it instead of just logging.

source: https://www.youtube.com/watch?v=jxmzY9soFXg

""" 

import logging
import numpy as np

logger = logging.getLogger(__name__)    # If logger doesn't exists, it creates new one else update
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('AdvanceLogging1.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def add(x,y):
    try:
        z = x+y
    except :
        logger.debug(f'add: {x}+{y} : Got an error')
    else:
        logger.info(f'add: {x}+{y}={z}')
        return z

def div(x,y):
    try:
        z = x/y
    except ZeroDivisionError as e:
        logger.exception(f'div: {x}/{y} = {e}')
    except Exception as e:
        logger.error(e)
    else:
        logger.info(f'div: {x}/{y}={z}')
        return z

num_1 = 3
num_2 = 4
num_3 = 0
num_4 = np.inf

result_add = add(num_1,num_3)
result_div = div(num_2,num_3)
result_div2 = div(num_1,num_2)
result_div3 = div(num_1,num_4)

