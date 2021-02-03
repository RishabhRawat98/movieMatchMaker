# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/swipe')
@login_required
def swipe():
    return render_template('swipe.html', name=current_user.name, movieId="97889" , movieImageURL="https://lumiere-a.akamaihd.net/v1/images/ct_aladdin2019_aladdin_17975_53d203c9.jpeg" , movieTitle="Aladdin", movieBrief="Aladdin, a kind thief, woos Jasmine, the princess of Agrabah, with the help of Genie. When Jafar, the grand vizier, tries to usurp the king, Jasmine, Aladdin and Genie must stop him from succeeding.")

@main.route('/movielist')
@login_required
def movielist():
    return render_template('movielist.html')