from flask import current_app, redirect
from flask_login import current_user




class RoleManager(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        app.teardown_appcontext(self.teardown)
    
    def teardown(self):
        pass
