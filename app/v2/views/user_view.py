from flask import Blueprint, render_template, request
from flask_login import login_user, login_required

user = Blueprint('user',__name__)