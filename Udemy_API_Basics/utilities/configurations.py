import configparser

import mysql.connector
from mysql.connector import *

def getConfig():
    config = configparser.ConfigParser()
    config.read("D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\Udemy_API_Basics\\utilities\\properties.ini")
    return config

connect_config = {
    "host": getConfig()["SQL"]["host"],
    "user": getConfig()["SQL"]["user"],
    "password": getConfig()["SQL"]["password"],
    "database": getConfig()["SQL"]["database"]
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(e)