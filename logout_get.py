from bottle import get, redirect, request, response
import jwt
import g

@get("/logout")
def _():
    encoded_jwt = request.get_cookie("jwt")

    # If there exists a cookie containing a user
    if encoded_jwt:    
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])

        # Loop through sessions
        user_session_id = decoded_jwt["user_session_id"]
        for session in g.SESSIONS:
            # If user exists in the sessions list, remove the user and destroy the cookie
            if session == user_session_id:
                g.SESSIONS.remove(user_session_id)  
                response.set_cookie("jwt", encoded_jwt, expires=0)
    
    # Else redirect to Home
    return redirect("/")