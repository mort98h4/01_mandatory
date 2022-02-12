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
        
        update_post = {}
        update_post_id = request.params.get("update")
        if update_post_id:
            for post in g.POSTS:
                if post["id"] == update_post_id:
                    update_post = post

        return dict(logged_in=True, posts=g.POSTS, update_post=update_post)
    return redirect("/")