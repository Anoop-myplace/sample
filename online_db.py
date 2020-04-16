import mysql.connector 
from pandas import DataFrame
# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='ram_ar', password='mySelf@08',
                              host='db4free.net', database = 'workplace_ar')

c = conn.cursor()

c.execute ("""CREATE TABLE employees(
          id INTEGER,
          first  TEXT,
          last TEXT,
          pay INTEGER
          )""")

conn.commit()

# STEP 4
c.execute("INSERT INTO employees VALUES(01,'ANOOP','RAMJI',6500)")
c.execute("INSERT INTO employees VALUES(02,'ARJIT','Singh',5500)")
c.execute("INSERT INTO employees VALUES(03,'Gautam','Manish',7000)")
c.execute("INSERT INTO employees VALUES(04,'Divyanshu','Srivastava',6000)")
conn.commit()

n = int(input("Enter the number of entries: "))
while (n>0):
    n-=1    
    idd = int(input("Enter the ID : "))
    first = input("Enter First Name : ")
    last = input("Enter Last Name : ")
    pay = int(input("Enter the Pay : "))
    c.execute("INSERT INTO employees VALUES ({},'{}', '{}', {})".format(idd, first,last,pay))
    conn.commit()


c.execute("SELECT * FROM employees")

# STEP 5

print ( c.fetchone()) 

print ( c.fetchmany(2)) 

print ( c.fetchall() )

c.execute("SELECT * FROM employees")

# STEP 6
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["id","first","last","pay"]

conn.close()
