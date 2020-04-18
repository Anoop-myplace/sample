import pymongo

#Connection str: mongodb+srv://sample:15375928@cluster0-zqovh.mongodb.net/test?retryWrites=true&w=majority

client = pymongo.MongoClient("mongodb+srv://sample:<password>@cluster0-zqovh.mongodb.net/test?retryWrites=true&w=majority")
mydb = client.my_base

def add_employee(idd, first, last, pay):
    unique_employee = mydb.my_coll.find_one({"id":idd})
    if unique_employee:
        return "Employee already exists"
    else:
        mydb.my_coll.insert_one(
                {
                "id" : idd,
                "first" : first,
                "last" : last,
                "pay" : pay
                })
        return "Employee added successfully"

def fetch_all_employee():
    user = mydb.my_coll.find()
    for i in user:
        print (i)

#Insert data in collection
add_employee(1,'Anoop', 'Ramji', 50000)
add_employee(2,'Manish', 'Kumar', 70000)
add_employee(3,'Arjit', 'Singh', 30000)
add_employee(4,'Divyanshu', 'Srivastava', 30000)

fetch_all_employee()

#Drop a collection in Mongo, deletes the database as well
#mydb.my_coll.drop()