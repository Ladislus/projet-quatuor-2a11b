from .app import app
from flask import render_template, redirect, request, url_for
import os
from .forms import *
from .views_quatuor import *
from .views_clarinette import *
from .views_contact import *
from .views_stages import *
from .views_other import *
from .views_administration import *
