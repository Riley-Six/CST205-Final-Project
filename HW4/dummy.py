from flask import Flask 
from flask_bootstrap import Bootstrap
from flask import render_template
from image_info import image_info
from PIL import Image
import random
import requests
import flask

# create an instance of the Flask class
app = Flask(__name__)
boostrap = Bootstrap(app)

# route() decorator binds a function to a URL
@app.route('/', methods = ['GET'])
def hello():
    return render_template('homeDummy.html')

@app.route('/second', methods = ['POST'])
def page2func():
  # Get the searchedName
  searchedName = flask.request.form['searchedName']

  # call imageFunction
  image = searchedName + '.jpg'

  # call ratingsFunction
  ratings = []

  # pass on image, ratings list and name to result page
  return render_template('resultDummy.html', searchedName=searchedName, image=image, ratings=ratings)

if __name__ == '__main__':
    app.run()