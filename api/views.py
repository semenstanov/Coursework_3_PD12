from flask import Blueprint, jsonify
from feed.dao.feed_dao import FeedDAO
import config
import logging

api_blueprint = Blueprint('api_blueprint', __name__)

feed_dao = FeedDAO(config.POSTS_PATH)
logging_f = "%(asctime)s [%(levelname)s] %(message)s"
time_f = "%d-%b-%y %H:%M:%S"
logging.basicConfig(level=logging.INFO, filename="logs/api.log", filemode="w",
                    format=logging_f, datefmt=time_f, encoding="utf-8")


@api_blueprint.route('/api/posts')
def api_posts():
    """Return all posts"""
    posts: list[dict] = feed_dao.get_posts()
    logging.info("Запрос /api/posts")
    return jsonify(posts), 200


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id):
    """Return single post by id"""
    post: dict | None = feed_dao.get_post_by_pk(post_id)
    logging.info(f"Запрос /api/posts/{post_id}")
    return jsonify(post), 200
