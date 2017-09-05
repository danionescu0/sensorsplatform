import jwt

from security.JwtTokenFactory import JwtTokenFactory

def secure(handler_class):
    def wrap_execute(handler_execute):
        def _execute(self, transforms, *args, **kwargs):
            try:
                require_auth(self, kwargs)
            except Exception:
                return False

            return handler_execute(self, transforms, *args, **kwargs)

        return _execute

    def require_auth(handler, kwargs):
        auth = handler.request.headers.get('Authorization')
        if not auth:
            return missing_authorization(handler)

        auth_header = auth.split()

        if auth_header[0].lower() != 'bearer' or len(auth_header) == 1:
            return invalid_header(handler)
        token = auth_header[1]
        try:
            jwt.decode(token, JwtTokenFactory.SECRET)
        except Exception:
            handler._transforms = []
            handler.set_status(401)
            handler.write("Invalid token")
            handler.finish()
        return True

    def missing_authorization(handler):
        handler._transforms = []
        handler.write("Missing authorization")
        handler.finish()

    def invalid_header(handler):
        handler._transforms = []
        handler.set_status(401)
        handler.write("invalid header authorization")
        handler.finish()

    handler_class._execute = wrap_execute(handler_class._execute)

    return handler_class