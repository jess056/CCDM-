import mySQLdb
conn = mySQLdb.connection(host="localhost", user = "root", passwd = "ceit")
mycurse = conn.cursor()

