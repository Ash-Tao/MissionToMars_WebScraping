# flask app to render html on local machines.
# also will load data to mongo

import os
from flask import Flask, render_template, redirect
import scrape_mars
from flask_pymongo import PyMongo


# Create an instance of Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = ('mongodb://localhost:27017/mars_db')
mongo = PyMongo(app)

@app.route('/')
def index():
    # find one document from our mongo db and return it.
    mars = mongo.db.images.find_one()
    # pass that listing to render_template
    return render_template("index.html",mars = mars)

# set our path to /scrape
@app.route('/scrape')
def scrape():
    # Run the scrape function
    mission_to_mars = scrape_mars.scrape_info()
    # Update the Mongo database using update and upsert=True
    mongo.db.images.update_one({}, {"$set": mission_to_mars}, upsert=True)
    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
