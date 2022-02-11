from bottle import get, view

@get("/feed")
@view("feed")
def _():
    return