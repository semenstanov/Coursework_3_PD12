from config import POSTS_PATH
from feed.dao.feed_dao import FeedDAO

feed_dao_instance = FeedDAO(POSTS_PATH)


def test_search_for_posts_type():
    """Testing search result correct type"""
    posts: list[dict] = feed_dao_instance.search_for_posts("кот")
    assert type(posts) == list, "Not a list"


def test_search_for_posts_keys():
    """Testing search result valid keys"""
    posts: list[dict] = feed_dao_instance.search_for_posts("кот")
    correct_keys: set = {"poster_name", "poster_avatar", "pic", "content",
                         "views_count", "likes_count", "pk"}
    for post in posts:
        post_keys = set(post.keys())
        assert correct_keys == post_keys, "Keys not valid"


def test_search_for_posts_word():
    """Testing search have a result"""
    word: str = "кот"
    posts: list[dict] = feed_dao_instance.search_for_posts(word)
    assert len(posts) != 0
    for post in posts:
        assert word in post["content"]
