import MySQLdb 

#create a connection
myconnection = MySQLdb.connection(host = "localhost", user= "root", passwd= "ciet")
#create the cursor object to hold connection
mycursor = myconnection.cursor()

mycursor.execute('CREATE DATABASE CEIT_library')
mycursor.execute('USE CIET_library')


#now let's create table--> Books
tablebooks = """CREATE table book(book_ID int primary key,bookname varchar(20)),Author varchar(20),Grnre varchar(20))"""
tablereaders = """CREATE TABLE Readers (ReadID int primary key, ReaderFName varchar(10), Readersurname varchar(20), course varchar(6),BkID int)"""

#now execute tablebooks
mycursor.execute(tablebooks)
mycursor.execute(tablereaders)
#now insert values
insertbokkvalue =""" INSERT INTO Book values (101,"Intro to python","Jack","sam","programming")"""
insertreader = """Insert INTO Readers Values(201,"Jonny","walker","CCDM",101)"""
mycursor.EXECUTE(insertbokkvalue)
mycursor.excute(insertreader)

#Thurday code
file = open('book.csv')
contents = csv.reader(file)
insertVal = "INSERT INTO book (BookID, Title, Author,Genre) VALUES (?,?,?,?)""
mycursor.executemany(insertVal,contents)
selectall = "SELECT * FROM book"
rows = cursor.execute(selectall).fetchall()
for row in rows:
    print(row)
#To fetch data and display output
#result = mycursor.fatchall()
    
#commit changes
myconnection.commit()
myconnection.close()

#To view
mycursor.execute('SHOW books')
result = mycursor.fetchall()
myconnection.commit()

for row in result:
    print(row)
    print("\n")