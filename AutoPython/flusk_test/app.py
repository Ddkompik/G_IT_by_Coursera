from flask import Flask

app = Flask(__name__)
#content inside of the home dir
@app.route('/')

def show_user(username):
    return f"Hello, {username}!"
#its not a hack? 
app.add_url_rule('/<username>', 'show_user', show_user) 

if __name__ == "__main__":
    app.run(debug=True)
