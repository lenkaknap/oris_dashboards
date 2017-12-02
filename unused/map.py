from convert_data import map_data
import plotly
plotly.tools.set_credentials_file(username='x408491', api_key='j6WIzt7o4nEKNY8MmRHS')

import plotly.plotly as py
from plotly.graph_objs import *

mapbox_access_token = 'pk.eyJ1IjoieDQwODQ5MSIsImEiOiJjamFjZXBxd2cwOTB0MzNxdTJsZDEybzNxIn0.bEA4K56yPb7ckl1npZgEEA'

df = map_data(2837)
latitude_ls = df["latitude"].tolist()
longitude_ls = df["longitude"].tolist()
name_ls = df["name"].tolist()

data = Data([
    Scattermapbox(
        lat=latitude_ls,
        lon=longitude_ls,
        mode='markers',
        marker=Marker(
            size=9
        ),
        text=name_ls,
    )
])
layout = Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(lat=49.7745131, lon=15.4786125),
        pitch=0,
        zoom=6
    ),
)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='MapLenda')