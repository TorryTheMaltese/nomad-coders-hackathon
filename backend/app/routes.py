from app import app, models
from flask import render_template, request, redirect, url_for, jsonify
from config import Config
from werkzeug.security import safe_str_cmp
import datetime
from pytz import timezone, utc
import jwt
import uuid
import dbHelper

now = datetime.datetime.utcnow()
KST = timezone("Asia/Seoul")
real_now = utc.localize(now).astimezone(KST)


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


@app.route('/join', methods=['GET', 'POST'])
def join():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()

        invalid_user = models.USERS.query.filter_by(user_email=post_data.get("email")).first()
        if invalid_user:
            return jsonify({"error": "이미 사용 중인 이메일입니다."})
        else:
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


def authenticate(email, password):
    user = models.USERS.query.filter_by(user_email=email).first()
    if user and safe_str_cmp(user.user_password.encode("utf-8"), password.encode("utf-8")):
        return user


def identity(payload):
    user_id = payload["userId"]
    return models.USERS.query.filter_by(user_id=user_id).first()


def give_access_token(user_id, user_name):
    exp = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * 60 * 24)
    real_exp = utc.localize(exp).astimezone(KST)

    payload = {
        "userId": user_id,
        "username": user_name,
        "exp": real_exp
    }

    access_token = jwt.encode(payload, Config.SECRET_KEY, "HS256")

    return access_token


def give_refresh_token(user):
    payload = {
        "userId": user.id
    }

    refresh_token = jwt.encode(payload, Config.SECRET_KEY, "HS256")
    token = models.TOKEN(token_refresh=refresh_token)
    token.user = user

    try:
        with dbHelper.get_session() as session:
            session.add(token)
    except Exception as e:
        return jsonify(e)

    return refresh_token


@app.route("/login", methods=["GET", "POST"])
def login():
    response_object = {"status": "success"}
    if request.method == "POST":
        post_data = request.get_json()
        user_exist = authenticate(post_data.get("email"), post_data.get("password"))

        if user_exist:
            give_refresh_token(user_exist)

            return jsonify({
                "accessToken": give_access_token(user_exist.id, user_exist.user_name).decode("UTF-8")
            })
        else:
            return "", 401

    return jsonify(response_object)
