# Create a sample Flask application
# ---------------------------------
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, agusjuli!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
    
# host='0.0.0.0' makes Flask listen on all interfaces inside the container
# port=8080, this is the port inside the container where Flask will run.
# It needs to match the container port that you expose when running Docker