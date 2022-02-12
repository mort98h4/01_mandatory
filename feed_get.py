from bottle import get, view, redirect, request
import g
import jwt

@get("/feed")
@view("feed")
def _():
    encoded_jwt = request.get_cookie("jwt")
    if encoded_jwt:
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]
        if user_session_id not in g.SESSIONS:
            return redirect("/login")
        return
    return redirect("/")