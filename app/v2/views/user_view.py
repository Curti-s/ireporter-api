from flask import Blueprint, render_template
from flask_login import login_user, login_required

user = Blueprint('user',__name__)

@user.route('/signup',methods=['GET','POST'])
def signup():
    form = SignupForm()
    return render_template('signup.html', title='Signup', form=form)

