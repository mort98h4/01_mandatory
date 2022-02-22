from bottle import get, run, static_file, view

##############################
@get("/app.css")
def _():
    return static_file("app.css", root=".")

##############################
# Allow to use this static file
@get("/images/pexels-denise-duplinski-3819818.jpg")
def _():
    return static_file("pexels-denise-duplinski-3819818.jpg", root="./images", mimetype="image/jpg")

##############################
# Import functions of web application
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

# Run localhost with specific port, allow debug, reload on save and use the Paste server
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")