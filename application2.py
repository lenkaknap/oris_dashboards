from flask import Flask, render_template, request, url_for
from convert_data import find_users, get_user_data, graphs_data
from visualization import text_info, map_scatter, bar_graph_stacked_km, bar_graph_stacked_controls, bar_graph_stacked_time
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
    dataFrame = graphs_data(oris_id)
    user_data = get_user_data(oris_id) # tady bych si to mohla predat z predchoziho kroku?? how?
    div_map = map_scatter(oris_id)
    div_time = bar_graph_stacked_time(oris_id)
    div_km = bar_graph_stacked_km(oris_id)
    div_controls = bar_graph_stacked_controls(oris_id)
    text = text_info(dataFrame)
    return render_template('graphs.html', div_map=Markup(div_map), div_time=Markup(div_time), div_km=Markup(div_km), div_controls=Markup(div_controls), user_data = user_data, text_data = text)


@app.route("/about", methods=['GET'])
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
