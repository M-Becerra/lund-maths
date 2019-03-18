import plotly.graph_objs as go
import plotly

#draw a square
x = [0, 1, 0, 1, 0, 1, 0, 1]
y = [0, 1, 1, 0, 0, 1, 1, 0]
z = [0, 0, 0, 0, 1, 1, 1, 1]

#the start and end point for each line
pairs = [(0,0,1), (1,0,0)]

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    name='markers'
)

x_lines = list()
y_lines = list()
z_lines = list()

#create the coordinate list for the lines
for p in pairs:
    for i in range(2):
        x_lines.append(x[p[i]])
        y_lines.append(y[p[i]])
        z_lines.append(z[p[i]])
    x_lines.append(None)
    y_lines.append(None)
    z_lines.append(None)

trace2 = go.Scatter3d(
    x=x_lines,
    y=y_lines,
    z=z_lines,
    mode='lines',
    name='lines'
)

fig = go.Figure(data=[trace1, trace2])
plotly.offline.plot(fig, filename='simple-3d-scatter')