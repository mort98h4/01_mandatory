from bottle import post, redirect, request
import g

@post("/delete-post")
def _():
    post_id = request.forms.get("post_id")
    if post_id:
        for index, post in enumerate(g.POSTS):
            if post["id"] == post_id:
                g.POSTS.pop(index)

    return redirect("/feed")