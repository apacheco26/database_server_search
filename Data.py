import pyodbc as sql

class data:
    _connection = None

    @classmethod
    def getData(cls,theName,theGender):
        if cls._connection == None:
            cls._connection = sql.connect(driver="{ODBC Driver 17 for SQL Server}",
                                          server="cisdbss.pcc.edu",
                                          database="NAMES",
                                          user="275student",
                                          password="275student"
                                          )
        if theGender == "null":
            theSQL = "SELECT Name, Year, Gender, NameCount, Total FROM all_data WHERE Name='" + theName.capitalize() + "'"
        else:
            theSQL = "SELECT Name, Year, Gender, NameCount, Total FROM all_data WHERE Name='" + theName.capitalize() + \
                     "' AND Gender='"+ theGender+"'"

        cursor = cls._connection.cursor()
        cursor.execute(theSQL)

        rows = cursor.fetchall()

        cls._connection.close()
        cls._connection = None

        return rows