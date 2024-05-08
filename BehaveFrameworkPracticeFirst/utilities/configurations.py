import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\BehaveFrameworkPracticeFirst\\utilities\\properties.ini")
    return config