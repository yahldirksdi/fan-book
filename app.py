import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("mongodb://test:sparta@ac-6fty83g-shard-00-00.1q65sre.mongodb.net:27017,ac-6fty83g-shard-00-01.1q65sre.mongodb.net:27017,ac-6fty83g-shard-00-02.1q65sre.mongodb.net:27017/?ssl=true&replicaSet=atlas-10zzql-shard-0&authSource=admin&retryWrites=true&w=majority")
DB_NAME =  os.environ.get("fanbook")

client = MongoClient("mongodb://test:sparta@ac-6fty83g-shard-00-00.1q65sre.mongodb.net:27017,ac-6fty83g-shard-00-01.1q65sre.mongodb.net:27017,ac-6fty83g-shard-00-02.1q65sre.mongodb.net:27017/?ssl=true&replicaSet=atlas-10zzql-shard-0&authSource=admin&retryWrites=true&w=majority")

db = client["fanbook"]

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive,
    }
    db.fanbook.insert_one(doc)
    return jsonify({'msg':'Comment Posted!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    message_list = list(db.fanbook.find({}, {'_id': False}))
    return jsonify({'messages': message_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)