from flask import Flask, render_template, send_from_directory, request, make_response, url_for, session, flash
from flask_bootstrap import Bootstrap
import os
import datetime
from app.forms import EmailForm
from flask_mail import Mail, Message
key_weather = '34be0019993203b5a55de4637b2cd0e1'
key_ipinfo = '254aabce1a4e9e'

app = Flask(__name__)
app.secret_key = 'ffewjr2ijr30ejfw039efjwefjw0wut0493u0943ti-gjr09t3409jg093jg09rgjoreg03j09rgjg930pojarg34q[po'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = '#'  # введите свой адрес электронной почты здесь
app.config['MAIL_DEFAULT_SENDER'] = '#'  # и здесь
app.config['MAIL_PASSWORD'] = '#'  # введите пароль
bootstrap = Bootstrap(app)
mail = Mail(app)
from app.controllers import home_controller
from app import errors
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.root_path, 'static'),
        'favicon.ico',
        mimetype='image/vnd.microsoft.icon'
    )
@app.route('/contact')
@app.route('/home/contact')
def contact():
    #...
    return render_template('error/404.html'), 404

@app.route('/about')
def about():
    #...
    return render_template('error/500.html'), 500

@app.route('/article/', methods=['POST', 'GET'])
def article():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=365)
    if request.method == 'POST':
        print(request.form)
        res = make_response('')

        session['font'] = request.form.get('font')
        res.headers['location'] = url_for('article')

        session['background'] = request.form.get('background')
        res.headers['location'] = url_for('article')

        session['color'] = request.form.get('color')
        res.headers['location'] = url_for('article')

        return res, 301
    return render_template('home/article.html')

@app.route('/visits-counter/')
def visits():
    session.permanent = True
    app.permanent_session_lifetime = datetime.timedelta(days=365)
    if 'visits' in session:
        session['visits']=session.get('visits')+1
    else:
        session['visits'] = 1
    return 'Всего посещений: {}'.format(session.get('visits'))


@app.route('/session/')
def updating_session():
    res = str(session.items())
    cart_item = {'pineapples':'10', 'apples':'20', 'mangoes':'30'}
    if 'cart_item' in session:
        session['cart_item']['pineapples']= '100'
        session.modified = True
    else:
        session['cart_item'] = cart_item

    return res

@app.route('/delete-visits/')
def delete_visits():
    session.pop('visits', None)
    return 'Посещения очищенны'

@app.route('/ip', methods=["GET", "POST"])
def ip():
    form = EmailForm()
    if form.validate_on_submit():
        email = form.email.data
        flash(f'Ну все погнали; адрес для бомбордировки: {email}', 'success')
        for i in range(0, 15):
            message = Message('Test', sender='#', recipients=[email])
            message.body = 'Andrey'
            mail.send(message)
    return render_template('home/ip.html', form=form)