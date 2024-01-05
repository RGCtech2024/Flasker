from flask import Flask, render_template


#Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
#   return "<h1>Hello World!</h1>"

def index():
   first_action = "python"
   stuff = "This is <strong>Bold</strong> text"
   favorite_color= [ "red", "blue", "lavender", 41]
   return render_template("index.html", 
                          first_action=first_action, 
                          stuff=stuff,
                          favorite_color=favorite_color)

    
# localhost:5000/object/action
@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name=name)


#custom error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == '__main__':
    app.run(debug=True)