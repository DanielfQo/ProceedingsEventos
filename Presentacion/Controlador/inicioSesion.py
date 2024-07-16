from flask import Blueprint, render_template, redirect, url_for
from . import registrarse

inicioSesion = Blueprint('inicioSesion', __name__,template_folder='../Vista/Assets/HTML')

@inicioSesion.route('/')
def home():
    return render_template('inicioSesion.html')
