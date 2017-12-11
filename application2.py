from flask import Flask, render_template, request
from convert_data import find_users, get_user_data, graphs_data
from visualization import text_info, map_scatter,\
    bar_graph_stacked_time, time_by_discipline,\
    bar_graph_stacked_km, km_by_discipline,\
    bar_graph_stacked_controls, controls_by_discipline
from markupsafe import Markup

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return render_template('home.html')


@app.route("/users", methods=['POST'])
def person_id():
    name=request.form['name']
    #regNo=request.form['regNo']
    users = find_users(name)
    length = len(users)
    return render_template('home_users.html', users = users, length = length)


@app.route("/users/<oris_id>", methods=['GET'])
def graphs(oris_id):
    data_frame = graphs_data(oris_id)
    user_data = get_user_data(oris_id)

    text = text_info(data_frame)
    div_map = map_scatter(data_frame)

    div_time = bar_graph_stacked_time(data_frame)
    text_time = time_by_discipline(data_frame)

    div_km = bar_graph_stacked_km(data_frame)
    text_km = km_by_discipline(data_frame)

    div_controls = bar_graph_stacked_controls(data_frame)
    text_controls = controls_by_discipline(data_frame)

    return render_template('graphs.html', user_data = user_data,
                           text_data = text, div_map=Markup(div_map),
                           div_time=Markup(div_time), text_time=text_time,
                           div_km=Markup(div_km), text_km = text_km,
                           div_controls=Markup(div_controls), text_controls=text_controls)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
