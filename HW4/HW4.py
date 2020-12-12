# Eric Guerra
# 11/20/2020
# CST 205
# Driver code that includes a home route and a route for the 2nd page

from flask import Flask 
from flask_bootstrap import Bootstrap
from flask import render_template
from image_info import image_info
from PIL import Image
import random
# create an instance of the Flask class
app = Flask(__name__)
boostrap = Bootstrap(app)

# store all image values 
rand = random.choice(image_info)

# route() decorator binds a function to a URL
@app.route('/')
def hello():
    random3 = []
    i = 0
    while i < 3:
        # check if image is already in the array 
        placeholder = random.choice(image_info)
        if placeholder not in random3:
            random3.append(placeholder)
            i += 1
    return render_template('home.html', my_list=random3)

@app.route('/picture/<imageID>')
def page2func(imageID):
    # get the pillow data for the image
    print (imageID)
    imgPath = 'static/images/' + imageID + '.jpg'
    im = Image.open(imgPath)
    return render_template('page2.html', imageID=imageID, my_list=image_info, 
                            imageSize=im.size, imageFormat=im.format, imageMode=im.mode)

if __name__ == '__main__':
    app.run()