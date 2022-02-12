from bottle import post, redirect, request
import g
import uuid
import jwt

@post("/create-post")
def _():
    encoded_jwt = request.get_cookie("jwt")
    decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
    post_content = request.forms.get("post_content")

    post = {
        "id": str(uuid.uuid4()),
        "user_first_name": decoded_jwt["user_first_name"],
        "user_email": decoded_jwt["user_email"],
        "post_content": post_content
    }
    g.POSTS.append(post)

    return redirect("/feed")