from bottle import get, run, view

##############################
@get("/")
@view("index")
def _():
    return
##############################

run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")