from flask import Flask, render_template


#Create a flask instance
app = Flask(__name__)

#Create a route decorator
@app.route('/')
# def index():
#     return "<h1> Hello World!</h1>"
def index():
    return render_template('index.html')
    
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/links/')
def links():
    return render_template('links.html')

# Invalid Error Pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404    

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500    
