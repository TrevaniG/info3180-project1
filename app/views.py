"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, redirect,session, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import Profile_users
import os
import datetime
from forms import LoginForm
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Jonah Ark")

@app.route('/profile', methods=['POST','GET'])
def profile():
    form= LoginForm()
    if request.method=='POST' and form.validate_on_submit():
        count=db.session.query(Profile_users).count()
        firstname=form.firstname.data
        lastname=form.lastname.data
        gender=form.gender.data
        mail=form.email.data
        location=form.location.data
        biography=form.biography.data
        
        date=str(datetime.datetime.now()).split()[0]
      
        photograph=form.photograph.data
        pic_name=secure_filename(photograph.filename)
        photograph.save(os.path.join(app.config['UPLOAD_FOLDER'],pic_name))
       
        user=Profile_users(firstname, lastname, gender, mail,location,biography,pic_name,date)
        
        db.session.add(user)
        db.session.commit()
      
        
        flash('Your profile has created!','success')
        return redirect(url_for('profiles'))
    else:
        return render_template('profile.html',form=form)

def photo_read(filename):
    bytes=" "
    
    with open(filename,"r") as j:
        bytes=j.read()
    
    return data
   
# def upload_images():
#     rootdir=os.getcwd()
#     print rootdir
#     image=[]
#     for subdir.dirs,files in os.walk(rootdir +'/app/static/uploads'):
#         for file in files:
#             image.append(os.path.join(subdir,file).split('/')[-1])
#     return image
    
    
@app.route('/profiles')
def profiles():
    
    users=Profile_users.query.all()
    user_profiles=[]
    
    for user in users:
        user_profiles.append({"profile_picture":user.photograph,"fname":user.firstname,"lname":user.lastname,"gender":user.gender,"location":user.location})
        
    return render_template('profiles.html',user=user)
    
@app.route('/profiles/<id>')
def profiles_byid(userid):
    user=Profile_users().query.filter_by(userid=userid).first()
    
    if user is None:
        return redirect(url_for('home'))
  
    user.userdate= str(datetime.datetime.now()).split()[0]
    
    return render_template('listprofiles.html', user=user)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        #getting the password and the username from the form 
        password=form.password.data
        username=form.username.data
        
        #querying database if user exists based on the username and password submitted
        
        user=Profile_users().query.filter_by(username=username,password=password).first()
        
        if user is not None and check_password_hash(user.password,password):
            remember_me=False
            
        if user is not None:
            login_user(user)
            
            flash("You have logged in successfully.",'success')
            
            next_page= request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash("Login failed- Error",'danger')
            
    
    return render_template("login.html",form=form)
        

@app.route("/logout")
@login_required
def logout():
    
    logout_user()
    flash("You have been logged out.",'danger')
    return redirect(url_for('home'))
    

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
