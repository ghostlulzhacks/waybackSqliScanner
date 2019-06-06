import requests
import json
import re

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class sqliScannerClass():

    def __init__(self):
        #SQL Error Messages
        self.MySQL = ["SQL syntax.*MySQL", "Warning.*mysql_.*", "valid MySQL result", "MySqlClient\."]
        self.PostgreSQL = ["PostgreSQL.*ERROR", "Warning.*\Wpg_.*", "valid PostgreSQL result", "Npgsql\."]
        self.MicrosoftSQLServer = ["Driver.* SQL[\-\_\ ]*Server", "OLE DB.* SQL Server", "(\W|\A)SQL Server.*Driver", "Warning.*mssql_.*", "(\W|\A)SQL Server.*[0-9a-fA-F]{8}", "(?s)Exception.*\WSystem\.Data\.SqlClient\.", "(?s)Exception.*\WRoadhouse\.Cms\."]
        self.MicrosoftAccess = ["Microsoft Access Driver", "JET Database Engine", "Access Database Engine"]
        self.Oracle = ["\bORA-[0-9][0-9][0-9][0-9]", "Oracle error", "Oracle.*Driver", "Warning.*\Woci_.*", "Warning.*\Wora_.*"]
        self.IBMDB2 = ["CLI Driver.*DB2", "DB2 SQL error", "\bdb2_\w+\("]
        self.SQLite = ["SQLite/JDBCDriver", "SQLite.Exception", "System.Data.SQLite.SQLiteException", "Warning.*sqlite_.*", "Warning.*SQLite3::", "\[SQLITE_ERROR\]"]
        self.Sybase = ["(?i)Warning.*sybase.*", "Sybase message", "Sybase.*Server message.*"]


    def createSqliUrl(self,url):
        try:
            urlParams = url.split("?")[1] 
        except:
            return

        urlParams = urlParams.split("&")
        for param in urlParams:
            try:
                param = param.split("=")
                paramStr = str(param[0]+"="+param[1])

                #Check for sqli using '
                paramExploitStr = paramStr+"'"
                newUrl = url.replace(paramStr,paramExploitStr)
                self.checkSqli(newUrl)

                #Check for sql using "
                paramExploitStr = paramStr+'"'
                newUrl = url.replace(paramStr,paramExploitStr)
                self.checkSqli(newUrl)
            except:
                pass

    def checkSqli(self,url):
        r = requests.get(url,verify=False,timeout=10)
        html = r.content
        for regg in self.MySQL:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.PostgreSQL: 
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.MicrosoftSQLServer:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.MicrosoftAccess:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.Oracle:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.IBMDB2:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.SQLite:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return
        for regg in self.Sybase:
            if(re.search(regg, html)):
                print("Vulnerable\t"+url)
                return

