def register_routes(api, app):
    from app.auth import register_routes as attach_authRoutes


    attach_authRoutes(api, app)