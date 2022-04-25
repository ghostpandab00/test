from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Version-2"
    
if __name__ == "__main__":
     app_port = os.getenv('APP_PORT',"8080")
    app.run(debug=True)
