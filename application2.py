from flask import Flask, render_template, request, url_for
from convert_data import find_users

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')

@app.route("/users", methods=['POST'])
def person_id():
    name=request.form['name']
    users = find_users(name)
    return render_template('home_users.html', users = users)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
