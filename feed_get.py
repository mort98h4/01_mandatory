from bottle import get, view, redirect, request
import g
import jwt

@get("/feed")
@view("feed")
def _():
    encoded_jwt = request.get_cookie("jwt")

    # If there exists a cookie containing a user
    if encoded_jwt:
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]

        # If user does not exist in the sessions list redirect to the login view
        if user_session_id not in g.SESSIONS:
            return redirect("/login")
        
        # Update specific post 
        update_post = {}
        update_post_id = request.params.get("update")

        # If update_post_id exists
        if update_post_id:
            # Loop through all posts
            for post in g.POSTS:
                # if id of the post matches update_post_id set it as update_post
                if post["id"] == update_post_id:
                    update_post = post

        # Display the view and pass data
        return dict(logged_in=True, posts=g.POSTS, update_post=update_post, user=decoded_jwt)
    
    # Else redirect to Home
    return redirect("/")