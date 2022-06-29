from flask import Flask     # From the flask module import the Flask class


app = Flask(__name__)       # Create an instance of the Flask class into app.
                            # aoo is now an "object"

@app.get("/")               # Flask decorator that allows us to map a route to a view function
def index():                # Our view function
    return "<h1>Hello, world!</h1>" # Return statement.


# x = index() # function call 

@app.get("/about")
def get_about():
    me = {
        "first_name": "Michael",
        "last_name": "Costanza",
        "hobbies": "Learning",
        "active": True
    }
    return me
