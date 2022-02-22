from bottle import get, redirect, request, view
import g # Globals
import jwt # JSON Web Token

##############################
@get("/")
@view("index")
def _():
    encoded_jwt = request.get_cookie("jwt")

    # If there exists a cookie containing a user
    if encoded_jwt:
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]

        # If user exists in the sessions list redirect to the feed view
        if user_session_id in g.SESSIONS: 
            return redirect("/feed")
    
    # Else pass logged_in false and display the view
    return dict(logged_in=False)