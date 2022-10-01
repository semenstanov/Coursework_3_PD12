import app
import pytest


class TestApi:

    @pytest.fixture
    def correct_keys(self):
        keys = {"poster_name", "poster_avatar", "pic", "content", "views_count",
                "likes_count", "pk"}
        return keys

    # TEST ALL POSTS
    def test_api_posts_status(self):
        """Testing API status code and response type"""
        response = app.app.test_client().get("/api/posts")
        assert response.status_code == 200, "Response error"
        assert response.mimetype == "application/json", "Not a JSON"

    def test_api_posts_type(self):
        """Testing API JSON correct type"""
        response = app.app.test_client().get("/api/posts")
        assert type(response.json) == list, "Not a list"

    def test_api_posts_keys(self, correct_keys: dict):
        """Testing API valid keys"""
        response = app.app.test_client().get("/api/posts")
        for result in response.json:
            response_keys = set(result.keys())
            assert correct_keys == response_keys, "Keys not valid"

    # TEST SINGLE POST
    def test_api_single_post_status(self):
        """Testing API single post status code and response type"""
        response = app.app.test_client().get("/api/posts/1")
        assert response.status_code == 200, "Response error"
        assert response.mimetype == "application/json", "Not a JSON"

    def test_api_single_post_type(self):
        """Testing API single post JSON correct type"""
        response = app.app.test_client().get("/api/posts/1")
        assert type(response.json) == dict, "Not a dict"

    def test_api_single_post_keys(self, correct_keys: dict):
        """Testing API single post valid keys"""
        response = app.app.test_client().get("/api/posts/1")
        response_keys = set(response.json.keys())
        assert correct_keys == response_keys, "Keys not valid"
