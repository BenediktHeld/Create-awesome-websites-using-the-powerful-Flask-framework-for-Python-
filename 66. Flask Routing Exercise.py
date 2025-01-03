import os

#Import Flask Class
from flask import Flask
'''
Puppy Latin Rules: 
    - If a puppy name does not end in a y add on a y to the name
    - example: Rufus -> Rufusy , Spot -> Spoty

    -If a puppy name does end in a y, replace it with iful instead
    -example: Sparky -> Sparkiful , Spoty -> Spotiful

    -Your web application will have a route: /puppy_latin/<name>
    -This route will take in the name passed and then display the puppy latin version on the page. 
'''
#Create application Object
app = Flask(__name__)

@app.route('/') #127.0.0.1:5000
def index(): 
    return '<h1>Welcome! Go to /puppy_latin/name to see your name in a puppy latin!</h1>'

@app.route("/puppy_latin/<name>")
def puppy(name): 
    if name[-1] == 'y':
        return '<h1>{}iful</h1>'.format(name)
    else:
        return '<h1>{}y</h1>'.format(name)
    
if __name__ == '__main__':
    app.run(debug=True)
