# -*- coding: utf-8 -*-
import os
import pymongo
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():

    # Docker will set the address and the port of the linked MongoDB container
    # in the following environmental variables.
    db_host = str(os.environ["DB_HOST"])
    db_port = int(os.environ["DB_PORT"])

    # Get a connection to MongoDB, then get the collection 'webStats' from the
    # database 'app2Db'.
    client = pymongo.MongoClient(db_host, db_port)
    collection = client["app2Db"]["webStats"]

    # Increment the hit count for the page 'home' by one.
    collection.update({"_id": "home"}, {"$inc": {"hit_count": 1}}, True)

    # Read the value of the hit counter
    hit_count = collection.find_one({"_id": "home"})["hit_count"]

    return """<h1>This is the app!</h1>
              <p>Hit Count: {count} </p>""".format(count=hit_count)


if __name__ == '__main__':
    app.run() 