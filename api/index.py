from app import app
from gunicorn.app.base import BaseApplication

class StandaloneApplication(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        for key, value in self.options.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

def handler(event, context):
    options = {
        'bind': '0.0.0.0:8080',
        'workers': 1,
        'timeout': 30
    }
    app_instance = StandaloneApplication(app, options)
    return app_instance.application(event)