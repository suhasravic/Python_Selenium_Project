import logging
import sys
import time

from loguru import logger


# class Logger():
def loggingfunction():
    logger = logging.getLogger(__name__)

    timestr = time.strftime("%Y-%m-%d-%H-%M-%S")
    filelocation = logging.FileHandler(
        'C:/Users/USER/PycharmProjects/pythonProject1/SeleniumPythonTests/Logs/Test_logs -' + str(timestr) + str(
            ".txt"))
    formater = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filelocation.setFormatter(formater)
    logger.addHandler(filelocation)
    logger.setLevel(logging.INFO)
    # logger.propagate = False
    # logger.parent=True
    logger.propagate = True
    print("---"+str(logger.hasHandlers()))
    # if not logger.hasHandlers():
    return logger
# def loggingfunction():
#     log = logger.add("log_{time}.txt", level="INFO")
#     print("from logger ms")
#     return log
