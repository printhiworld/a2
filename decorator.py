from flask import request, abort
import jwt

algo = 'HS256'
secret = '1wsx34%'
def auth_required(func):
    """

    :rtype: object
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split('Bearer ')[-1]

        try:
            jwt.decode(token, secret, algorithms=[algo])
        except Exception as e:
            abort(401)
        return func
    return wrapper