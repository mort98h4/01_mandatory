from bottle import post, redirect, request
import g

@post("/update-post")
def _():
    # Grab post["id"] from the form
    post_id = request.forms.get("post_id")
    if post_id:
        # Loop through posts
        for index, post in enumerate(g.POSTS):
            # If post["id"] matches post_id update the value of post_content with data from the form
            if post["id"] == post_id:
                post["post_content"] = request.forms.get("post_content")
    
    return redirect("/feed")