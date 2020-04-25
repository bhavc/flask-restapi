# from .model import Auth

def register_routes(api, app):
    from .controller import api as auth_api

    api.add_namespace(auth_api, path="/auth")
