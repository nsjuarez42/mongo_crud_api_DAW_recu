from flask import Flask,jsonify,request
from config import Development,Build
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config.from_object(Development)
mongo = PyMongo(app)


@app.route("/todos",methods=["GET","POST"])
def todos():
    if request.method == "GET":
        return jsonify(list(mongo.db.todos.find({})))

    elif request.method == "POST":

        mongo.db.todos.insert_one(request.json)
        print(dir(mongo.db.todos))
        return jsonify({"msg":"Todo added successfully"})

@app.route("/todo/<id>",methods=["PUT","DELETE","GET"])
def todo(id):
    if request.method == "GET":
        return jsonify({"todo":mongo.db.todos.find_one({"_id":ObjectId(id)})})
    
    if request.method == "PUT":
        mongo.db.todos.update_one({"_id":ObjectId(id)},{"$set":request.json})
        todo = mongo.db.todos.find_one({"_id":ObjectId(id)})
        return jsonify({"msg":"Updated successfully","todo":todo})

    elif request.method == "DELETE":
        todo = mongo.db.todos.find_one({"_id":ObjectId(id)})
        mongo.db.todos.delete_one({"_id":ObjectId(id)})
        return jsonify({"msg":"Deleted successfully","todo":todo})


if __name__ == "__main__":
    app.run(debug=True)
