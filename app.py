"""
Ayy lmao
"""
import time

import bottle
import valve.source.a2s

from bottle.ext import sqlite

APP = bottle.Bottle()
PLUGIN = sqlite.Plugin(dbfile='sourcemod.sq3')
APP.install(PLUGIN)
SERVER_ADDRESS = ("139.59.23.194", 27015)

def a2s():
    """Retrieves info about the server
    """
    try:
        server = valve.source.a2s.ServerQuerier(SERVER_ADDRESS)
        t_send = time.time()
        info = server.info()
        ping = (time.time() - t_send) * 1000.0
        #players = server.players()
        return [True, ping, info] #, players]
    except Exception:
        return [False]

@APP.route('/')
def index(db):
    data = a2s()
    ipinfo = db.execute(
        "SELECT ccode, Count(*) as countrycode from ipinfo group by ccode order by countrycode desc"
        ).fetchall()
    return bottle.template("index", data=data, ipinfo=ipinfo)

if __name__ == "__main__":
    bottle.debug(True)
    bottle.run(APP, host='localhost', port=8080, reloader=True)
