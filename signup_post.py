from bottle import post, redirect, request
import re # Regex
import uuid # UUID
import g # Globals

@post("/signup")
def _():
    # Validate and grap the first name
    user_first_name = request.forms.get("user_first_name")
    if not user_first_name:
        return redirect(f"/signup?error=user_first_name_missing")
    if len(user_first_name) < 2:
        return redirect(f"/signup?error=user_first_name_invalid&{user_first_name}")

    # Validate and grap the last name
    user_last_name = request.forms.get("user_last_name")
    if not user_last_name:
        return redirect(f"/signup?error=user_last_name_missing&user_first_name={user_first_name}")
    if len(user_last_name) < 2:
        return redirect(f"/signup?error=user_last_name_invalid&user_first_name={user_first_name}&user_last_name={user_last_name}")

    # Validate and grap the e-mail
    user_email = request.forms.get("user_email")
    if not user_email:
        return redirect(f"/signup?error=user_email_missing&user_first_name={user_first_name}&user_last_name={user_last_name}")
    if not re.match(g.REGEX_EMAIL, user_email):
        return redirect(f"/signup?error=user_email_invalid&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    for user in g.USERS:
        if user["user_email"] == user_email:
            return redirect(f"/signup?error=user_email_used&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

    # Validate and grap the password
    user_password = request.forms.get("user_password")
    if not user_password:
        return redirect(f"/signup?error=user_password_missing&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    if not re.match(g.REGEX_PASSWORD, user_password):
        return redirect(f"/signup?error=user_password_invalid&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")

    # Validate and grap the confirm password
    user_confirm_password = request.forms.get("user_confirm_password")
    if not user_confirm_password:
        return redirect(f"/signup?error=user_confirm_password_missing&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    if not user_confirm_password == user_password:
        return redirect(f"/signup?error=user_confirm_password_invalid&user_first_name={user_first_name}&user_last_name={user_last_name}&user_email={user_email}")
    
    # Assign data to the new user
    user_id = str(uuid.uuid4())
    user = {
        "user_first_name": user_first_name,
        "user_last_name": user_last_name,
        "user_email": user_email,
        "user_password": user_password,
        "user_id": user_id
    }

    # Add user to the users list
    g.USERS.append(user)

    return redirect("/login")