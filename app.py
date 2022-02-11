from bottle import get, run, static_file, view

##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
import home_get             # GET
import login_get            # GET
import signup_get           # GET

import signup_post          # POST

##############################

run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")