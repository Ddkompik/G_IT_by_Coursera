from flask import Flask

app = Flask(__name__)
#content inside of the home dir
@app.route("/")

def home():
    return "Hello Flusk!"

if __name__ == "__main__":
    app.run(debug=True)
