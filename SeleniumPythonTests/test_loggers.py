import datetime
import logging
# import time
from loguru import logger


def test_basiclogging():
    # logger=logging.getLogger(__name__)
    # timestr = time.strftime("%Y-%m-%d-%H%M%S")
    # filelocation=logging.FileHandler('C:/Users/USER/PycharmProjects/pythonProject/logs/Execution_logs'+str(timestr)+str(".log"))
    # formater=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    # filelocation.setFormatter(formater)
    #
    # logger.addHandler(filelocation)
    # logger.setLevel(logging.DEBUG)
    # # logger hierarchy is as follows
    #
    # logger.debug("logger level is debug")
    # logger.info("logger level is info")
    # logger.warning("logger level is warning")
    # logger.error("logger level is error")
    # logger.critical("logger level is critical")
    logger.info("hey")
    logger.add("log_{time}.txt", level="INFO")
    logger.info("hai")
