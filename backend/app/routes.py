from . import app
from flask import render_template, request, redirect, url_for, jsonify
from .models import BOOKS, USERS
import uuid


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'description': post_data.get('description'),
            'tag': post_data.get('tag')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'description': post_data.get('description'),
            'tag': post_data.get('tag')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


@app.route('/join', methods=['GET','POST'])
def add_user():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        USERS.append({
            'id': uuid.uuid4().hex,
            'email': post_data.get('email'),
            'password': post_data.get('password'),
        })
        response_object['message'] = 'welcome!'
    else:
        response_object['users'] = USERS
    return jsonify(response_object)