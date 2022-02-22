from bottle import post, redirect, request
import g
import uuid
import jwt
import time

@post("/create-post")
def _():
    # Get user information from cookie
    encoded_jwt = request.get_cookie("jwt")
    decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])

    # Get post_content from the form
    post_content = request.forms.get("post_content")

    # Get date and time of the creation of the post
    post_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(int(time.time())))

    # Create new post
    post = {
        "id": str(uuid.uuid4()),
        "user_id": decoded_jwt["user_id"],
        "user_first_name": decoded_jwt["user_first_name"],
        "user_email": decoded_jwt["user_email"],
        "post_content": post_content,
        "post_date": post_date
    }

    # Add the new post to the posts list
    g.POSTS.append(post)

    return redirect("/feed")
