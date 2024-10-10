import pymongo
import certifi


con_string = "mongodb+srv://test:test@fsdi107.9axeg.mongodb.net/?retryWrites=true&w=majority&appName=FSDI107"

client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("organika")