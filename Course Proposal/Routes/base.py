from flask import Blueprint, request, jsonify


base_bp = Blueprint('base', __name__)


@base_bp.route('/')
def home():
    '''
    Home route for the Course Proposal Tool.
    '''
    return 'Welcome to the Course Proposal Tool!'
