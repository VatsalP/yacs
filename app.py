"""

"""
import bottle

app = bottle.Bottle()
bottle.debug(True)

@app.route('/')
def index():
    return bottle.template("index")

if __name__ == "__main__":
    bottle.run(app, host='localhost', port=8080, reloader=True)
