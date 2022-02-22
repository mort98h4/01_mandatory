from bottle import get, redirect, request, response
import jwt
import g

@get("/logout")
def _():
    encoded_jwt = request.get_cookie("jwt")
    if encoded_jwt:    
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]
        for session in g.SESSIONS:
            if session == user_session_id:
                g.SESSIONS.remove(user_session_id)  
                response.set_cookie("jwt", encoded_jwt, expires=0)
    return redirect("/")