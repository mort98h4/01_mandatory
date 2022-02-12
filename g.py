import time

USERS = [
    {
        "user_first_name": "Morten",
        "user_last_name": "Gross",
        "user_email": "a@a.dk",
        "user_password": "123456Qw"
    }
]
SESSIONS = []
POSTS = [
    {"id": "a", "user_first_name": "a", "user_email": "a@a.dk", "post_content": "xxx", "post_date": time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(1644672386))},
    {"id": "b", "user_first_name": "b", "user_email": "b@b.dk", "post_content": "xxx", "post_date": time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(1643677386))},
    {"id": "c", "user_first_name": "c", "user_email": "c@c.dk", "post_content": "xxx", "post_date": time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(1643672386))}
]
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
REGEX_PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
JWT_SECRET = "4w50m3 k3Y"