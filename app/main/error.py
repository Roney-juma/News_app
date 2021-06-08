from flask import render_template
from . import main

@main.app_errorhandler(403)
def forbidden_access(error):
    '''
    Function to handles 403 error ie forbidden access
    '''
    
    return render_template('error.html',error ='page')


@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to handles 404 error ie page not found
    '''
    return render_template('error.html',error='page')


@main.app_errorhandler(500)
def server_error(error):
    '''
    Function to handles 500 error ie server error
    '''
    return render_template('error.html',error='page')