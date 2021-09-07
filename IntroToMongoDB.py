import pymongo

client = pymongo.MongoClient("mongodb://127.0.0.1:27017/") # Protocol, IP Address, Port number

mydb = client['Employee1']

information = mydb.employeeinformation

records = [{
    'firstname':'Jack',
    'lastname':'Jacobs',
    'department':'Analytics',
}, 
    {
    'firstname':'Nick',
    'lastname':'Jacobs',
    'department':'Mechanics',
    }, 
    {
    'firstname':'James',
    'lastname':'Garner',
    'department':'Athletics',
    }]

information.insert_many(records)