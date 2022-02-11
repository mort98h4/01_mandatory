from bottle import get, request, view
import g

##############################
@get("/login")
@view("login")
def _():
    form_error = request.params.get("error")
    user_email = request.params.get("user_email")

    if form_error == "user_email_missing":
        error = {"error_type": "user_email", "error_message": "Please enter your e-mail"}
    elif form_error == "user_email_invalid":
        error = {"error_type": "user_email", "error_message": "Please enter a valid e-mail"}
    elif form_error == "user_password_missing":
        error = {"error_type": "user_password", "error_message": "Please enter a password of at least 8 characters, containing at least 1 uppercase letter, 1 lowercase letter and 1 number."}
    elif form_error == "user_password_invalid":
        error = {"error_type": "user_password", "error_message": "Please enter a valid password of at least 8 characters, containing at least 1 uppercase letter, 1 lowercase letter and 1 number."}
    elif form_error == "user_password_incorrect":
        error = {"error_type": "user_password", "error_message": "Password is incorrect."}
    elif form_error == "non_existing_user":
        error = {"error_type": "non_existing_user", "error_message": f"The email {user_email} is not an user."}
    else:
        error = {}

    

    return dict(error=error, user_email=user_email, users=g.USERS)