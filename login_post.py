from bottle import post, redirect, request, response
import re
import g
import uuid
import time
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
            
            session_id = str(uuid.uuid4())
            g.SESSIONS.append(session_id)
            user_session = {
                "user_id": user["user_id"],
                "user_first_name": user["user_first_name"],
                "user_last_name": user["user_last_name"],
                "user_email": user["user_email"],
                "iat": int(time.time()),
                "user_session_id": session_id
            }
            encoded_jwt = jwt.encode(user_session, g.JWT_SECRET, algorithm="HS256")
            response.set_cookie("jwt", encoded_jwt)

            return redirect("/feed")

    return redirect(f"/login?error=non_existing_user&user_email={user_email}")