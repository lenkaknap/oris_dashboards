from convert_data import map_data
import plotly
from plotly.graph_objs import *

# map is not showing correctly, it is showing a different map than what I selected on mapbox
def map_scatter(person_id):
    mapbox_access_token = 'pk.eyJ1IjoieDQwODQ5MSIsImEiOiJjamFjZXBxd2cwOTB0MzNxdTJsZDEybzNxIn0.bEA4K56yPb7ckl1npZgEEA'

    df = map_data(person_id)
    rows = len(df.index)

    latitude_ls = df["latitude"].tolist()
    longitude_ls = df["longitude"].tolist()
    name_date = []

    for i in range (rows):
        name_date.append(df['date'][i] + '<br>' + df['classTxt'][i] + '<br>' + df['name'][i])

    data = Data([
        Scattermapbox(
            lat=latitude_ls,
            lon=longitude_ls,
            mode='markers',
            marker=Marker(
                size=12
            ),
            text= name_date,
        )
    ])
    layout = Layout(
        title='Mapa závodů za rok 2017',
        # autosize=False,
        width = 800,
        height = 600,
        showlegend=False,
        hovermode='y',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(lat=49.7745131, lon=15.4786125),
            pitch=0,
            zoom=6,
        ),
        font=dict(family='sans-serif'),
    )
    fig = dict(data=data, layout=layout)
    fig_map = plotly.offline.plot(fig, output_type='div')
    return fig_map