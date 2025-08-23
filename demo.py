import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging

logging.info("Hello, World!")


try:
    a = 2/0

except Exception as e:
    raise USvisaException(e, sys)

