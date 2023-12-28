from flask import Flask, request, jsonify
from bd import *
import mysql.connector

db = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    database=database
)

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"

@app.route("/get/<person_id>")
def get(person_id):
    mycursor = db.cursor()
    mycursor.execute("""SELECT * FROM person WHERE id = '%s'""" % person_id)
    myresult = mycursor.fetchall()
    return jsonify(myresult), 200

@app.route("/post", methods=["POST"])
def post():
    mycursor = db.cursor()
    mycursor.execute("""INSERT INTO person (name, gender, maritalstatus) VALUES ('New Person', 'M', 'M')""")
    db.commit()
#    myresult = mycursor.fetchall()
    return jsonify("Person created"), 200

@app.route("/put/<person_id>", methods=["PUT"])
def put(person_id):
    mycursor = db.cursor()
    mycursor.execute("""UPDATE person SET email = 'updated@python.com' WHERE id = '%s'""" % person_id)
    db.commit()
    return jsonify("""Person '%s' updated""" % person_id), 200

@app.route("/delete/<person_id>", methods=["DELETE"])
def delete(person_id):
    mycursor = db.cursor()
    mycursor.execute("""DELETE FROM person WHERE id = '%s'""" % person_id)
    db.commit()
    return jsonify("""Person '%s' deleted""" % person_id), 200

if __name__ == "__main__":
    app.run(debug=True)

