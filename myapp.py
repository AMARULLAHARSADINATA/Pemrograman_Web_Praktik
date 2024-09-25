#import flask
from flask import Flask

# main app
app = Flask(__name__)

# set route untuk/
@app.route("/")
# function index
def index():
    # print text
    return "Hello, World!"

# debug, untuk update server dev otomatis
if __name__ == "__main__":
    app.run(debug=True)