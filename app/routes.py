from flask import render_template, redirect, flash, url_for
from app import App
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import user



@App.route('/')
@App.route('/index')
def index():
    words = ['привет', 'пока', 'я очень буду ждать звонка', 'полетели', 'hello']
    '''
        я связываю МЕТКУ words на странице index.html
        со своим массивом words, в котором лежат слова
    '''
    return render_template('index.html', words=words)


@App.route('/sign_in', methods=['GET', 'POST'])
def signIn():
    form = LoginForm()
    return render_template('login.html', form=form)
