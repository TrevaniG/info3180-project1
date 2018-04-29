from . import db


class Profile_users(db.Model):
    __tablename__='users'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender= db.Column(db.String(80))
    email= db.Column(db.String(80),unique=True)
    location= db.Column(db.String(80))
    userdate=db.Column(db.String(15))
    biography=db.Column(db.String(200))
    photograph=db.Column(db.String(15))
  
    
   
    def __init__(self,firstname,lastname,gender,email,location,biography,photograph,userdate):
        self.firstname=firstname
        self.lastname =lastname
        self.gender=gender
        self.email=email
        self.location=location
        self.biography=biography
        self.photograph=photograph
        self.userdate=userdate
       
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)
