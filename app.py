from bottle import get, run, static_file, view

##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
import home             # GET
import login            # GET
import signup           # GET

##############################

run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")