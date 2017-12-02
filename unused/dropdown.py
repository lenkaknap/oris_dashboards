import pandas as pd
import plotly.plotly as py

from ipywidgets import widgets
from IPython.display import display, clear_output, Image
from plotly.graph_objs import *
from plotly.widgets import GraphWidget

# define our widgets
g = GraphWidget('https://plot.ly/~kevintest/1149/')
w = widgets.Dropdown(
    options=['red', 'blue', 'green'],
    value='blue',
    description='Colour:',
)


# generate a function to handle changes in the widget
def update_on_change(change):
    g.restyle({'marker.color': change['new']})


# set a listener for changes to the dropdown widget
w.observe(update_on_change, names="selected_label")

display(w)
display(g)