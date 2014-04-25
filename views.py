from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView

from flask.ext.mongoengine.wtf import model_form

home = Blueprint('home', __name__, template_folder='templates')


class HomeView(MethodView):

    def get(self):
        return render_template('index.html')


# Register the urls
home.add_url_rule('/', view_func=HomeView.as_view('home'))
