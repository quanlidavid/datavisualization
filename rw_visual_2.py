import plotly.graph_objs as go

from random_walk import RandomWalk

while True:
    rw = RandomWalk(5_000)
    rw.fill_walk()

