USERS = [
    {
        "user_first_name": "Morten",
        "user_last_name": "Gross",
        "user_email": "a@a.dk",
        "user_password": "123456Qw"
    }
]
SESSIONS = []
POSTS = []
REGEX_EMAIL = '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
REGEX_PASSWORD = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
JWT_SECRET = "4w50m3 k3Y"