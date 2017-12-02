from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('my_template.html', map=url_for('static', filename='map.html'), stacked=url_for('static', filename='stacked-bar.html'), stacked_km=url_for('static', filename='km_months_stacked.html'), controls=url_for('static', filename='controls_months_stacked.html'))

if __name__ == '__main__':
    app.run(debug=True)