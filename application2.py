from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('home.html', map=url_for('static', filename='map.html'), stacked=url_for('static', filename='stacked-bar.html'), stacked_km=url_for('static', filename='km_months_stacked.html'), controls=url_for('static', filename='controls_months_stacked.html'))

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
