from flask import session , abort

def admin_only_viwe (func):
    def decorator(*args,**kwargs):
        if session.get('id') is None:
            abort(401)
        if session.get('role') !=1:
            abort(403)
       
    return decorator