from config import COMMENTS_PATH
import pytest
from feed.dao.comments_dao import CommentsDAO


class TestCommentsDAO:

    @pytest.fixture
    def comments_dao(self):
        comments_dao_instance = CommentsDAO(COMMENTS_PATH)
        return comments_dao_instance

    @pytest.fixture
    def correct_keys(self):
        keys: set = {"post_id", "commenter_name", "comment", "pk"}
        return keys

    # TEST ALL COMMENTS
    def test_get_comments_all_type(self, comments_dao):
        """Testing all comments correct type"""
        comments: list[dict] | list = comments_dao.get_comments()
        assert type(comments) == list, "Not a list"

    def test_get_comments_all_keys(self, comments_dao, correct_keys: dict):
        """Testing all comments valid keys"""
        comments: list[dict] | list = comments_dao.get_comments()
        for comment in comments:
            comment_keys = set(comment.keys())
            assert correct_keys == comment_keys, "Keys not valid"

    # TEST USER POST COMMENTS
    def test_get_comments_by_post_id_type(self, comments_dao):
        """Testing comments in user post correct type"""
        post_comments: list[dict] | list = comments_dao.get_comments_by_post_id(
            1)
        assert type(post_comments) == list, "Not a list"

    def test_get_comments_by_post_id_keys(self, comments_dao,
                                          correct_keys: dict):
        """Testing comments in user post valid keys"""
        post_comments: list[dict] | list = comments_dao.get_comments_by_post_id(
            1)
        for comment in post_comments:
            comment_keys = set(comment.keys())
            assert correct_keys == comment_keys, "Keys not valid"

    def test_get_comments_by_post_id_error(self, comments_dao):
        """Testing wrong post id raises error"""
        with pytest.raises(ValueError):
            comments_dao.get_comments_by_post_id(9)
