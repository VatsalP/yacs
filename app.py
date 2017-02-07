"""

"""
import time

import bottle
import valve.source.a2s

app = bottle.Bottle()
bottle.debug(True)
SERVER_ADDRESS = ("yacs.cf", 27015)

def a2s():
    """Retrieves info about the server
    """
    server = valve.source.a2s.ServerQuerier(SERVER_ADDRESS)
    t_send = time.time()
    info = server.info()
    ping = (time.time() - t_send) * 1000.0
    players = server.players()
    return [ping, info, players]


@app.route('/')
def index():
    data = a2s()
    return bottle.template("index", data=data)

if __name__ == "__main__":
    bottle.run(app, host='localhost', port=8080, reloader=True)
