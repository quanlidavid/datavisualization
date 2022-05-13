import plotly.graph_objs as go
import numpy as np

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

    fig = go.Figure(data=go.Scatter(
        x=rw.x_values,
        y=rw.y_values,
        mode='markers',
        name='Random Walk',
        marker=dict(
            color=np.arange(rw.num_points),
            size=8,
            colorscale='Greens',
            showscale=True
        )
    ))

    fig.show()

    keep_running = input('Make another walk?(y/n): ')
    if keep_running == 'n':
        break
