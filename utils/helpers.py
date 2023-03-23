from dotenv import load_dotenv
import os
from utils.sessions import reqres


def authorization():
    load_dotenv()
    LOGIN = os.getenv('email')
    PASSWORD = os.getenv('password')
    authorization = reqres().post('/api/login', data={
        "email": LOGIN,
        "password": PASSWORD
    })
    cookie_value = authorization.cookies.get('token')
    token = {}
    if cookie_value is not None:
        token.update({"token": cookie_value})
    return token
