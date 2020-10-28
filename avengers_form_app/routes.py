# Import the app variable from the init
from avengers_form_app import app

# Import specific packages from flask
from flask import render_template, request

# Import Our Form(s)
from avengers_form_app.forms import UserInfoForm

# Default Home Route - in order to use a route, u need a decorator = line 8
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/test')
def testRoute():
    names = ['Joel','Gabby','Terrell','Keith']
    return render_template('test.html', list_names = names)

#GET == Gathering Info
#Post == Sending Info
@app.route('/register', methods = ['GET','POST'])

def register():
    # Init our form 
    form = UserInfoForm()
    # Validation of our form
    if request.method == 'POST' and form.validate():
        # Get Information from the form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        #print the data to the server that comes from the form
        print(username,email,password)

    return render_template('register.html',user_form = form)