import pymongo


# Here iam coping the client code which is in my cluster0 database , so this code helps us connect with cluster0 which is my database for my mongodb
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Mahendra:JTx5FZA7parBernO@cluster0.klmitxd.mongodb.net/?retryWrites=true&w=majority" # just mention the password of the cluster0 database which we must save at somewhere while creating the database

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)



# By the above output i successfully connected to my database of MongoDB and i have defined database 

### Steps to work with MongoDB database
    
# first create database in MongoDB
# create collection
# create a file for storing collection
# create Document
# insert document inside the file 





# Now iam creating database in my MongoDB
database_name='student1'
student_database=client[database_name]

# creating a collection
collection='student_database'

# storing the created database which is student_database in 1 file which 
students_details_collection=student_database[collection]



# Creating a document which it consist of data in Key:value pair because mongodb takes data in Json formate with Key:value pair dictionary form
student_data={"name":"Mahendra",
              "college":"LPU",
              "Address":"Punjab"}

# By the above code we just created a document which is suits for MongoDB , adn we didnot insert this document yet
    

# lets create another document 
student_data={"name":"Max-payn",
              "college":"IIT",
              "Address":"Chennai"}


# inserting the created document in MongoDB
students_details_collection.insert_one(student_data) # for inserting 1 document we need to use insert_one()



### Steps to Know the Inserted docuement in MongoDB
# Open MongoDB Atlas ->click on Databases-> click on collection-> there check the created data with Key:value pair

# Fetching the inserted data in the mongodb database
student_corner=students_details_collection.find() # here by using the find() iam going to find the document which i saved inside the collection and which it got saved in 1 file which is students_details_collection thats why iam finding that file
student_corner.next()  # by using the next() i can fetch the inserted document in MongoDB

student_corner.next() # as you can see here first i have created the 2nd document , and then i have inserted in the database, and then fetched the inserted document thorugh the next function , so its depends on how many times we are running the call next fucntion based on the that run time number that particular document will get fetched , so here i have created 2 documents in my MongoDB so inorder to fetch my second document i need to run the next() for 2 time then i could get the 2nd document in my output

# so rather than calling the document manually which is in database by using next() , it would be better to use For Loop
for student_details in students_details_collection.find():
    print(student_details)

# Lets Try to insert many list of documents in single go 
student_data_list=[{"name":"Sbhubham", "last_name":"KumaP", "Course": "Cyber Security"},
{"City": "bangalore", "name":"Sima", "Collage": "Mumbai University"},
{"name": "Rahul", "Books": "machine Learning", "job": "Data Science"}]


# inserting the created list of documents in MongoDB
students_details_collection.insert_many(student_data_list) # for inserting many documents we need to use insert_one()


# fetching the list of documents which are inserted in MongoDB by using For Loop
for student_details in students_details_collection.find():
    print(student_details)





# Filtering Operations

# searching for the specific name throughout the list of document 
query={"name":"Max-payn"} 

for student_details in students_details_collection.find(query): # here we just need to pass the query variable inside the find() that searches for the assgined dictionary
    print(student_details)



# Regular Expression = it helps us to search for specfic starting letter words 
myquery={"name":{"$regex":"^R"}} # here i would to search for the data of the specific column which is name and which starts with data letter R

doc=students_details_collection.find(myquery)

for x in doc:
    print(x)


# Sort = it helps us to sort the document in different forms
doc=students_details_collection.find().sort("name") # here i sorting the document based on the name column 
for x in doc:
    print(x)



# Whichever the operations that we are performing here thats all get reflected or made changes in the MongoDB database based on the operation that we are performing 

# deleting the single record
myquery={"name":"sanju"}

students_details_collection.delete_one(myquery) # here by using the delete_one fucntion iam deleting the specific column name which is sanju

for x in students_details_collection.find(): # by this we could check that we succesfully deleted the sanju in our mongodb database
    print(x)


# deleting the multiple records 
myquery={"name":{"$regex":"^S"}} # here iam trying to delete the records which starts with letter S 

students_details_collection.delete_many(myquery)

for x in students_details_collection.find(): # by this we could check that we succesfully deleted the sanju in our mongodb database
    print(x)