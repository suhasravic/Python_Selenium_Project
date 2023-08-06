import pandas
import json
from SeleniumPythonTests import LoggerMS as logger
import openpyxl


# class DataDrivenTest:

def readDataFromExcel(excellPath, sheetName):
    # logger.MyLogger.info("Reading data from excell--" + excellPath)
    # logger.logger.info("Reading data from excell--" + excellPath)
    logger.loggingfunction().info("Reading data from excell--" + excellPath)
    completeData = pandas.read_excel(excellPath, sheet_name=sheetName)
    return completeData


def readRequiredDataFromExcell(excellPath, sheetName, columnNumber, columnName):
    completeData = pandas.read_excel(excellPath, sheet_name=sheetName)
    dataframe = pandas.DataFrame(completeData, index=None)
    requiredData = dataframe.iloc[columnNumber][columnName]
    # requiredData = completeData.iloc[columnNumber], [columnName]
    return requiredData


def readDataFromJSONFile(jsonfilepath):
    jsonfile = open(jsonfilepath)
    jsondataframe = json.load(jsonfile)
    return jsondataframe


def readDataFromJSONFileWithKey(jsonfilepath, key):
    jsonfile = open(jsonfilepath)
    jsondataframe = json.load(jsonfile)
    jsonvalue = jsondataframe[key]
    return jsonvalue
