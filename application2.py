from flask import Flask, render_template, request, url_for
from convert_data import find_users
from graphs_months import bar_graph_stacked_km_div
from map_offline import map_scatter
from markupsafe import Markup

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/users", methods=['POST'])
def person_id():
    name=request.form['name']
    users = find_users(name)
    return render_template('home_users.html', users = users)


@app.route("/users/<oris_id>", methods=['GET'])
def graphs(oris_id):
    plot_div = bar_graph_stacked_km_div(oris_id)
    map_div = map_scatter(oris_id)
    return render_template('graphs.html', div_placeholder=Markup(plot_div), div_map=Markup(map_div))


@app.route("/about", methods=['GET'])
def about():
    plot_div = bar_graph_stacked_km_div(3483)
    return render_template('about.html', div_placeholder = Markup(plot_div))


@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
