from avengers_form_app import app, db

# Import all of the Werkzeug Security methods
from werkzeug.security import generate_password_hash, check_password_hash

# Import for DateTime Module (This comes from Python)
from datetime import datetime

# The User class will have
# An id, username, email
#password, post

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique =True)
    # the encryption key is 256 characters
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship ('Post', backref = 'author', lazy = True)

                    # LAZY means we only ask for it when we need it, other than that
                    # We would not ask for it 

# Creation of an Init method for our Class 
    def __init__(self, username, email,password):
        self.username = username
        self.email = email
        self.password = self.set_pasword(password)

    def set_password(self,password):
        """
        
            Grab the password that is passed into the method
            Return the hashed version of the password
            Which will be stored inside of the database
        
        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with the following email: {self.email}'


# Creation of the Post Model 
# The Post model will have an
# id, title, content, date_created
# user_id
class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, title, content, user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the post is {self.title} \n and the content is {self.content}'