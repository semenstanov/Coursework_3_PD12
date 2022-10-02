import json


class CommentsDAO:
    def __init__(self, path: str):
        self.path = path

    def get_comments(self) -> list[dict] | list:
        """Load JSON with all comments"""
        with open(self.path, "r", encoding='UTF-8') as file:
            return json.load(file)

    def get_comments_by_post_id(self, post_id: int) -> list[dict] | list:
        """Return all comments in a single post"""
        comments: list = []
        if post_id not in range(1, 9):
            raise ValueError("Post not found")
        else:
            for comment in self.get_comments():
                if post_id == comment['post_id']:
                    comments.append(comment)
            return comments
