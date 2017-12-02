import plotly.plotly as py
import plotly.graph_objs as go

trace = dict(
    type='scattergeo',
    lon = [42, 39], lat = [12, 22],
    marker = ['Rome', 'Greece'],
    mode = 'markers')
py.iplot([trace])