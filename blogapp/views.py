from app import app


@app.route('/')
def homepage():
    return '<h1>Home page</h1>'