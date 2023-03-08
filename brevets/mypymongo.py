import os
from pymongo import MongoClient

# Set up MongoDB connection
client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
# Use database "brevetsdb"
db = client.brevetsdb
# Use collection "lists" in the databse
collection = db.brevets


def brevet_insert(brevet_dist_km, begin_date, items):
    """
    Inserts a new brevet list into the database "mydb", under the collection "lists".
    
    Inputs a brevet_dist_km (int) and items (list of dictionaries)
    Returns the unique ID assigned to the document by mongo (primary key.)
    """
    output = collection.insert_one({
        "brevet_dist_km": brevet_dist_km,
        "begin_date": begin_date,
        "items": items})
    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)

def brevet_find():
    """
    Obtains the newest brevet document in the "lists" collection in database "mydb".

    Returns title (string) and items (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for brevet_list in lists:
        # We store all of our lists as documents with three fields:
        ## brevet_dist_km: string
        ## begin_date: string
        ## items: list

        ### every item has two fields:
        #### km: int   # km
        #### location: string  # location
        return brevet_list["brevet_dist_km"], brevet_list["begin_date"], brevet_list["items"]
