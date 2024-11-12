# C:\Users\#####\AppData\Local\Programs\Python\Python313>python -m pip install pillow
# pip install mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html
from connect import mySQLCon

cone = mySQLCon()
print(cone)
cone.createTables()
