from flask import session , abort
from functools import wraps

def admin_only_viwe (func):
    @wraps(func)    # it used when we use a  decorator for several viwe function. without it the name of viwe function set same and flaks give error.
    def decorator(*args,**kwargs):
        if session.get('id') is None:
            abort(401)
        if session.get('role') !=1:
            abort(403)
        return func(*args,**kwargs)
    print (decorator.__name__)
    return decorator