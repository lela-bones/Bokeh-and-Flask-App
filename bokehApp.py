# bokehApp.py

import holoviews as hv
from bokeh.server.server import Server
from tornado.ioloop import IOLoop
import numpy as np

renderer = hv.renderer('bokeh')
renderer = renderer.instance(mode='server')

def sine(frequency, phase, amplitude):
    xs = np.linspace(0, np.pi*4)
    return hv.Curve((xs, np.sin(frequency*xs+phase)*amplitude)).options(width=800)

if __name__ == '__main__':
    ranges = dict(frequency=(1, 5), phase=(-np.pi, np.pi), amplitude=(-2, 2), y=(-2, 2))
    dmap = hv.DynamicMap(sine, kdims=['frequency', 'phase', 'amplitude']).redim.range(**ranges)
    app = renderer.app(dmap)
    server = Server({'/': app}, port=5006, allow_websocket_origin=["localhost:5000"])
    server.start()
    loop = IOLoop.current()
    loop.start()
   