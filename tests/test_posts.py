from config import POSTS_PATH
import pytest
from feed.dao.feed_dao import FeedDAO


class TestFeedDAO:

    @pytest.fixture
    def feed_dao(self):
        feed_dao_instance = FeedDAO(POSTS_PATH)
        return feed_dao_instance

    @pytest.fixture
    def correct_keys(self):
        keys: set = {"poster_name", "poster_avatar", "pic", "content",
                     "views_count", "likes_count", "pk"}
        return keys

    # TEST ALL POSTS
    def test_posts_all_type(self, feed_dao):
        """Testing all posts correct type"""
        posts: list[dict] = feed_dao.get_posts()
        assert type(posts) == list, "Not a list"

    def test_posts_all_keys(self, feed_dao, correct_keys: set):
        """Testing all posts valid keys"""
        posts: list[dict] = feed_dao.get_posts()
        for post in posts:
            post_keys = set(post.keys())
            assert correct_keys == post_keys, "Keys not valid"

    # TEST USER POSTS
    def test_get_posts_by_user_type(self, feed_dao):
        """Testing user posts correct type"""
        user_posts: list[dict] | list = feed_dao.get_posts_by_user("leo")
        assert type(user_posts) == list, "Not a list"

    def test_get_posts_by_user_keys(self, feed_dao, correct_keys: set):
        """Testing user posts valid keys"""
        user_posts: list[dict] | list = feed_dao.get_posts_by_user("leo")
        for post in user_posts:
            post_keys = set(post.keys())
            assert correct_keys == post_keys, "Keys not valid"

    def test_get_posts_by_user_value_error(self, feed_dao):
        """Testing wrong user raises error"""
        with pytest.raises(ValueError):
            feed_dao.get_posts_by_user("TestName")

    # TEST SINGLE POST
    def test_get_post_by_pk_type(self, feed_dao):
        """Testing single post correct type"""
        post_pk: dict = feed_dao.get_post_by_pk(1)
        assert type(post_pk) == dict, "Not a dict"

    def test_get_post_by_pk_keys(self, feed_dao, correct_keys: set):
        """Testing single post correct keys"""
        post_pk: dict = feed_dao.get_post_by_pk(1)
        assert correct_keys == set(post_pk.keys()), "Keys not valid"
