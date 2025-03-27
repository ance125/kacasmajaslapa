from flask import Blueprint, render_template, send_file
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/sun')
@login_required
def sun():
    return render_template("sun.html", user=current_user)

@views.route('/mercury')
@login_required
def mercury():
    return render_template("mercury.html", user=current_user)

@views.route('/venus')
@login_required
def venus():
    return render_template("venus.html", user=current_user)

@views.route('/mars')
@login_required
def mars():
    return render_template("mars.html", user=current_user)

@views.route('/jupiter')
@login_required
def jupiter():
    return render_template("jupiter.html", user=current_user)

@views.route('/saturn')
@login_required
def saturn():
    return render_template("saturn.html", user=current_user)

@views.route('/uranus')
@login_required
def uranus():
    return render_template("uranus.html", user=current_user)

@views.route('/neptune')
@login_required
def neptune():
    return render_template("neptune.html", user=current_user)
    


    
    
