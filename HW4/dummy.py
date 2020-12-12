from flask import Flask 
from flask_bootstrap import Bootstrap
from flask import render_template
from image_info import image_info
from PIL import Image
from google_images_search import GoogleImagesSearch
from io import BytesIO
import json 
import pathlib
pathlib.Path().absolute()
import random
import requests
import flask


from bs4 import BeautifulSoup
# create an instance of the Flask class
def resultFinder(nameLooker):
    result = requests.get("https://www.behindthename.com/name/"+nameLooker+"/rating")

    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    lookFor = "td"
    links = soup.find_all(lookFor)
    allJunk = []

    for i in links:
            allJunk.append([str(i.text)])
    
    temp2Dlist = [[] for i in range(14)]
    spotsAgain = 0
    switchAgain = 0

    for i in range(len(allJunk)):
        if ("%" in str(allJunk[i]) or "xa0" in str(allJunk[i])) and ("\\n" not in str(allJunk[i])):
            s = str(allJunk[i])
            s = s.replace('\\xa0','').replace("'","").replace("[",'').replace("]","")
            #print(s)
            temp2Dlist[spotsAgain].append(s)
            switchAgain += 1
            if switchAgain == 4:
                switchAgain = 0
                spotsAgain += 1

    if not temp2Dlist[0]:
        return("Unfortunatly, the popularity data for "+ nameLooker +" could not be found.")

    outPutCombine = "According to a popular vote, many people thought the name '" + nameLooker +"' was:"
    #print(outPutCombine)
    for i in range(len(temp2Dlist)):
        if (i == (0)):
            outPutCombine = outPutCombine + " " 
        elif(i == (len(temp2Dlist)-1)):
            outPutCombine = outPutCombine + ", and " 
        else:
            outPutCombine = outPutCombine + ", "

        if temp2Dlist[i][1] > temp2Dlist[i][2]:
            outPutCombine = outPutCombine + temp2Dlist[i][0]
        else:
            outPutCombine = outPutCombine + temp2Dlist[i][0]

        if i == (len(temp2Dlist)-1):
            outPutCombine = outPutCombine + "."


    return(outPutCombine)

def imageFinder(nameLooker):
    gis = GoogleImagesSearch('AIzaSyALNghCvPMwTXWwrXorvOUvy9ydUCdlcvU', 'aa5bd644ce5a37202')
    name = nameLooker

    response = requests.get('https://www.behindthename.com/api/lookup.json?name=' + name + '&key=er829146479').json()

    try:
        usage = response[0]['usages'][0]['usage_full']

        if usage == 'English':
            usage = 'UK'
        
        if usage == 'Italian':
            usage = 'Italy'

        searchTerm = usage +' Flag'
    except KeyError:
        searchTerm = 'IDK'

    gis.search({'q': searchTerm, 'num': 1,'fileType': 'jpg'}, custom_image_name = name)

    my_bytes_io = BytesIO()
    
    for image in gis.results():
        # here we tell the BytesIO object to go back to address 0
        my_bytes_io.seek(0)

        # take raw image data
        raw_image_data = image.get_raw_data()

        # this function writes the raw image data to the object
        image.copy_to(my_bytes_io, raw_image_data)

        # or without the raw data which will be automatically taken
        # inside the copy_to() method
        image.copy_to(my_bytes_io)

        # we go back to address 0 again so PIL can read it from start to finish
        my_bytes_io.seek(0)

        # create a temporary image object
        temp_img = Image.open(my_bytes_io)

        # show it in the default system photo viewer
        temp_img.show()

        outputImage = temp_img

    return outputImage


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
  image = imageFinder(searchedName)

  # call ratingsFunction
  ratings = resultFinder(searchedName)

  # pass on image, ratings list and name to result page
  return render_template('resultDummy.html', searchedName=searchedName, image=image, ratings=ratings)

if __name__ == '__main__':
    app.run()