import config

from flask import Blueprint, render_template, request, redirect

from feed.dao.comments_dao import CommentsDAO
from feed.dao.feed_dao import FeedDAO
from feed.dao.bookmarks_dao import BookmarksDAO
from feed.utils import word_for_comments_count

feed_blueprint = Blueprint('feed_blueprint', __name__,
                           template_folder='templates')

feed_dao = FeedDAO(config.POSTS_PATH)
comments_dao = CommentsDAO(config.COMMENTS_PATH)
bookmarks_dao = BookmarksDAO(config.BOOKMARKS_PATH)


@feed_blueprint.route('/')
def feed_page():
    """Main feed page with posts"""
    feed: list[dict] = feed_dao.make_hashtags_from_text()
    bookmarks: list[dict] | list = bookmarks_dao.get_bookmarks()
    return render_template('index.html', feed=feed, bookmarks=bookmarks), 200


@feed_blueprint.route('/post/<int:post_id>')
def post_page(post_id: int):
    """Single post page"""
    post: dict | None = feed_dao.get_post_by_pk(post_id)
    comments: list[dict] | list = comments_dao.get_comments_by_post_id(post_id)
    comments_count: str = word_for_comments_count(comments)
    return render_template('post.html', post=post, comments=comments,
                           comments_count=comments_count), 200


@feed_blueprint.route('/search')
def search_posts():
    """Page with search by word results"""
    query: str = request.args.get('s')
    posts: list[dict] | list = feed_dao.search_for_posts(query)
    return render_template('search.html', posts=posts), 200


@feed_blueprint.route('/user/<username>')
def user_feed(username: str):
    """Page with user posts"""
    feed: list[dict] | list = feed_dao.get_posts_by_user(username)
    return render_template('user-feed.html', feed=feed, username=username), 200


@feed_blueprint.route('/tag/<tagname>')
def tag_feed(tagname: str):
    """Page with search by hashtag results"""
    posts: list[dict] | list = feed_dao.search_for_posts(tagname)
    return render_template('tag.html', posts=posts, tagname=tagname), 200


@feed_blueprint.route('/bookmarks')
def feed_bookmarks():
    """Page with saved bookmarks"""
    all_bookmarks: list[dict] = bookmarks_dao.get_bookmarks()
    return render_template("bookmarks.html", bookmarks=all_bookmarks), 200


@feed_blueprint.route('/bookmarks/add/<int:post_id>', methods=['GET'])
def bookmarks_add(post_id: int):
    """View for add bookmark by id"""
    post: dict = feed_dao.get_post_by_pk(post_id)
    bookmarks_dao.add_bookmark(post)
    return redirect("/", code=302)


@feed_blueprint.route('/bookmarks/remove/<int:post_id>', methods=['GET'])
def delete_bookmarks(post_id: int):
    """View for delete bookmark by id"""
    bookmarks_dao.delete_bookmark(post_id)
    return redirect("/", code=302)
