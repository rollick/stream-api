import datetime
from pymongo import MongoClient

MONGO_URL = 'mongodb://localhost:27017/'
DATABASE_NAME = 'stream'

#connection = MongoClient(MONGO_URL)
#db = connection[DATABASE_NAME]

"""
Typical message Structure

{"created": datetime.datetime.utcnow(),
 "text": "The message we want to deliver",
 "tags": ["PULL REQUEST", "FAIL"],
 "source": "Github" 
}

"""

# this internal function return the database connection
def __get_db():
    connection = MongoClient(MONGO_URL)
    db = connection[DATABASE_NAME]
    return db

# this function returns the messages collection
def get_messages_collection():
    db = __get_db()
    return db.messages

# This function store a message into the collection messages
def put_message(message):
   
    message['created'] = datetime.datetime.utcnow() 
    messages = get_messages_collection()
    message_id = messages.insert(message)
    return message_id

def to_string(message):
    #return "- source: {0} \n- created: {1} \n- text: {2} \n- tags: {3}".format(message["source"], message["created"], message["text"], message["tags"])
    result = "- Source: %s <br />" %message['source']
    result += "- Text: %s <br />" %message['text']
    result += "- Tags: %s <br />" "".join(message["tags"])
    return result
    #return "- source: {0} \n- text: {2} \n- tags: {3}".format(message["source"], message["text"], message["tags"])
