from bottle import post, redirect, request, response
import re
import g
import uuid
import time
import jwt

@post("/login")
def _():
    # Validate and get the e-mail
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect(f"/login?error=user_email_missing")
    if not re.match(g.REGEX_EMAIL, user_email):
        return redirect(f"/login?error=user_email_invalid&user_email={user_email}")
    
    # Validate and get the password
    user_password = request.forms.get("user_password")
    if not user_password:
        return redirect(f"/login?error=user_password_missing&user_email={user_email}")
    if not re.match(g.REGEX_PASSWORD, user_password):
        return redirect(f"/login?error=user_password_invalid&user_email={user_email}")

    # Loop through all users
    for user in g.USERS:
        # Check if a user email matches the email from the form
        if user["user_email"] == user_email:
            # Check if the password matches the password from the form
            if not user["user_password"] == user_password:
                return redirect(f"/login?error=user_password_incorrect&user_email={user_email}")
            
            # Create a temporarily session id and add it to the sessions list
            session_id = str(uuid.uuid4())
            g.SESSIONS.append(session_id)

            # Create user session dictionary, encode it as a JWT and set as cookie
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

            # SUCCES
            return redirect("/feed")

    # If validation is cool but user email does not exist
    return redirect(f"/login?error=non_existing_user&user_email={user_email}")