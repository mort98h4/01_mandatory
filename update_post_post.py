from bottle import post, redirect, request
import g

@post("/update-post")
def _():
    post_id = request.forms.get("post_id")
    if post_id:
        for index, post in enumerate(g.POSTS):
            if post["id"] == post_id:
                post["post_content"] = request.forms.get("post_content")
    
    return redirect("/feed")