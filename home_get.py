from bottle import get, redirect, request, view
import g
import jwt

##############################
@get("/")
@view("index")
def _():
    encoded_jwt = request.get_cookie("jwt")
    if encoded_jwt:
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]
        if user_session_id in g.SESSIONS: 
            return redirect("/feed")
    return dict(logged_in=False)