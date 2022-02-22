from bottle import post, redirect, request
import g

@post("/delete-post")
def _():
    # Grab post["id"] from the form
    post_id = request.forms.get("post_id")
    if post_id:
        # Loop through posts
        for index, post in enumerate(g.POSTS):
            # If post["id"] matches post_id remove it from the posts list
            if post["id"] == post_id:
                g.POSTS.pop(index)

    return redirect("/feed")