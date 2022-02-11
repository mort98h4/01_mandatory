from bottle import post, redirect, request
import re
import g
import jwt

@post("/login")
def _():
    # VALIDATION
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect(f"/login?error=user_email_missing")
    if not re.match(g.REGEX_EMAIL, user_email):
        return redirect(f"/login?error=user_email_invalid&user_email={user_email}")
    
    user_password = request.forms.get("user_password")
    if not user_password:
        return redirect(f"/login?error=user_password_missing&user_email={user_email}")
    if not re.match(g.REGEX_PASSWORD, user_password):
        return redirect(f"/login?error=user_password_invalid&user_email={user_email}")

    for user in g.USERS:
        if user["user_email"] == user_email:
            if not user["user_password"] == user_password:
                return redirect(f"/login?error=user_password_incorrect&user_email={user_email}")
            return redirect("/feed")

    return redirect(f"/login?error=non_existing_user&user_email={user_email}")