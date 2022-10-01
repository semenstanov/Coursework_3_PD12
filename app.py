from flask import Flask

from api.views import api_blueprint
from feed.views import feed_blueprint

app = Flask(__name__)
app.config.from_pyfile("config.py")

app.register_blueprint(feed_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def error_404(error):
    """Page 404 error"""
    return f"OOPS! Page not found", 404


@app.errorhandler(500)
def error_500(error):
    """Internal server error"""
    return f"OOPS! Server have a problem", 500


if __name__ == '__main__':
    app.run()
