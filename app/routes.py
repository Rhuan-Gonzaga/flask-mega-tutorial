from app import instancia_flask

@instancia_flask.route('/')
@instancia_flask.route('/index')
def index():
    return "Hello world"