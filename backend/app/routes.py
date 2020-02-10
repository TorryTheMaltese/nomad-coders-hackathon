from app import app, models
from flask import render_template, request, redirect, url_for, jsonify
import uuid
import dbHelper


def remove_book(book_id):
    for book in models.BOOKS:
        if book['id'] == book_id:
            models.BOOKS.remove(book)
            return True
    return False


@app.route('/', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        models.BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'description': post_data.get('description'),
            'tag': post_data.get('tag')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = models.BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        models.BOOKS.append({
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


@app.route('/join', methods=['GET', 'POST'])
def add_user():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        user = models.USERS(user_email=post_data.get("email"),
                            user_name=post_data.get("username"),
                            user_password=post_data.get("password"))

        try:
            with dbHelper.get_session() as session:
                session.add(user)
        except Exception as e:
            return jsonify(e)
    else:
        response_object = {"status": "failed"}
    return jsonify(response_object)
