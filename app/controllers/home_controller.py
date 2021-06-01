from app import app
from flask import render_template, make_response, request

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/home/index')
def index():
    # ...
    return render_template(
        'home/index.html',
    )

'''@app.route('/about')
def about():
    # ...
    return render_template('home/about.html')'''

@app.route('/cookie/')
def cookie():
    if not request.cookies.get('foo'):
        res = make_response("Setting a cookie")
        res.set_cookie('foo', 'bar', max_age=60*60*24*365*2)
    else:
        res = make_response(
            'Value of cookie fo is {}'.format(request.cookies.get('foo'))
        )
    return res

@app.route('/delete-cookie')
def delete_cookie():
    res = make_response('Cookie Removed')
    res.set_cookie('foo', 'bar', max_age=0)
    return res