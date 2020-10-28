from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email



# DataREquired == Making sure the field is filled in
# EqualTo == Making sure the field(s) are the same (I.E Password and Confirm Password)
# Email == Making sure the field has a proper email given to it

class UserInfoForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField()

    #were gonna take the value from line 11 and import it into routes.