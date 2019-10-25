from app import app
from app import database
from flask import render_template
from app.forms import LoginForm
from app.forms import RegisterationForm
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from flask_login import current_user,login_user
from flask_login import login_required
from flask_login import logout_user
from app.models import User
from app.models import Posts
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
def index():
    
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))



@app.route('/registeration',methods=['GET','POST'])
def registeration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterationForm(request.form)
    if form.validate_on_submit():
        user = User(username = form.username.data,email = form.email.data)
        user.set_password(form.password.data)
        database.session.add(user)
        database.session.commit()
        flash('congratulations , you are a registered user')
        return redirect(url_for('login'))
    return render_template('registeration.html',title ='Register',form = form)

# user profile
# to create user file we need to write a new view function that maps
# to /user/<username>

# the following url has a dynamic component 
# when a route has a dynamic component flask will accept any 
# text in that portion of the url and will invoke the view function
# and the actual text as the argument 


@app.route('/user/<username>')
@login_required
def user(username):
    # this view function will be accesible only to the 
    user =User.query.filter_by(username=username).first_or_404()
    # in case we dont have the results it will send an 404 error
    posts = [
            {'author':user,'body':'body one'},
            {'author':user,'body':'body two'},
            ]
    return render_template('user.html',user=user,posts=posts)


