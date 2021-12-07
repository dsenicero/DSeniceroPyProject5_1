import pyodbc

server = 'cstnt.tstc.edu'
database = 'itse2359sp21'
username = 'dsenicerosp212359'
password = '1733724'

con = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

cursor = con.cursor()
#Initial Query
#query = cursor.execute("SELECT * FROM teachsp212359.terminology")

#First Query ->Show only terms and definitions whose term starts with the letter m.
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term like 'm%'")

#Second Query ->Show only terms and definitions whose term matches hardware.
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term = 'hardware'")

#Third Query ->Show only terms and definitions that have the letter s in the term.
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term like '%s%'")

#Fourth Query ->Show only terms and definitions whose terms contains ware.
#query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term like '%ware%'")

#Fifth Query ->Show only terms and definitions whose term ends with the letter t.
query = cursor.execute("SELECT * FROM teachsp212359.terminology WHERE term like '%t'")

results = cursor.fetchall()

for result in results:
    print(result);
    print();