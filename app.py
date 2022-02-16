from bottle import get, run, static_file, view

##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
@get("/images/pexels-denise-duplinski-3819818.jpg")
def _():
    return static_file("pexels-denise-duplinski-3819818.jpg", root="./images", mimetype="image/jpg")

##############################
import home_get             # GET
import login_get            # GET
import signup_get           # GET
import feed_get             # GET
import logout_get           # GET

import signup_post          # POST
import login_post           # POST
import delete_post_post     # POST
import update_post_post     # POST
import create_post_post     # POST

##############################

run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")