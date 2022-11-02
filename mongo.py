from pymongo import MongoClient
import json
import requests

cluster = MongoClient("mongodb+srv://Luis:admin@cluster0.nccxbu2.mongodb.net/?retryWrites=true&w=majority")
db = cluster["db_name"]
collection = db["collection_name"]

def add_suggestion(suggestion):
    print(suggestion)
    collection.insert_one(suggestion)
    print("*******************  Artigo adicionado com sucesso!  *******************")

# edita um artigo.
def vote(suggestion_id, suggestion):
    print(suggestion)
    collection.update_one({"_id":suggestion_id}, {"$set": {"v": 1}})
    print("*******************  Sugestao editada com sucesso!  *******************")
