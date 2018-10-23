from flask import Flask, request
import json
import pymongo
from faker import Faker

fake = Faker()

mongoClient = pymongo.MongoClient('mongodb://localhost:27017')
db = mongoClient.scratch
peopleCollection = db.people

def create_person():
    person = { 'name': fake.name(), 'address': fake.address() }
    id = peopleCollection.insert(person)
    return id

def list_people():
    cursor = peopleCollection.find({})
    elements = [ dict(name=d['name'], address=d['address']) for d in cursor ]
    return elements

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/people', methods=['GET', 'POST'])
def people():
    if request.method == 'POST':
        res = json.dumps({ 'results': str(create_person()) })
        return res
    else:
        res = json.dumps({ 'results': list_people() })
        return res

if __name__ == '__main__':
app.run(host="0.0.0.0", debug=True)
