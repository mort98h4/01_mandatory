from bottle import get, redirect, request, view
import jwt
import g

##############################
@get("/signup")
@view("signup")
def _():
    encoded_jwt = request.get_cookie("jwt")
    if encoded_jwt:
        decoded_jwt = jwt.decode(encoded_jwt, g.JWT_SECRET, algorithms=["HS256"])
        user_session_id = decoded_jwt["user_session_id"]
        if user_session_id in g.SESSIONS:
            return redirect("/feed")

    form_error = request.params.get("error")
    
    if form_error == "user_first_name_missing":
        error = {"error_type": "user_first_name", "error_message": "Please enter your first name."}
    elif form_error == "user_first_name_invalid":
        error = {"error_type": "user_first_name", "error_message": "Your first name must be at least 2 characters."}
    elif form_error == "user_last_name_missing":
        error = {"error_type": "user_last_name", "error_message": "Please enter your last name."}
    elif form_error == "user_last_name_invalid":
        error = {"error_type": "user_last_name", "error_message": "Your last name must be at least 2 characters."}
    elif form_error == "user_email_missing":
        error = {"error_type": "user_email", "error_message": "Please enter your e-mail"}
    elif form_error == "user_email_invalid":
        error = {"error_type": "user_email", "error_message": "Please enter a valid e-mail"}
    elif form_error == "user_email_used":
        error = {"error_type": "user_email", "error_message": "Your e-mail is already registered to an account."}
    elif form_error == "user_password_missing":
        error = {"error_type": "user_password", "error_message": "Please enter a password of at least 8 characters, containing at least 1 uppercase letter, 1 lowercase letter and 1 number."}
    elif form_error == "user_password_invalid":
        error = {"error_type": "user_password", "error_message": "Please enter a valid password of at least 8 characters, containing at least 1 uppercase letter, 1 lowercase letter and 1 number."}
    elif form_error == "user_confirm_password_missing":
        error = {"error_type": "user_confirm_password", "error_message": "Please confirm your password."}
    elif form_error == "user_confirm_password_invalid":
        error = {"error_type": "user_confirm_password", "error_message": "Passwords are not identical."}
    else:
        error = {}

    user_first_name = request.params.get("user_first_name")
    user_last_name = request.params.get("user_last_name")
    user_email = request.params.get("user_email")

    return dict(error=error, user_first_name=user_first_name, user_last_name=user_last_name, user_email=user_email)