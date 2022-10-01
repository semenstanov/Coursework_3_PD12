import re
import json


class FeedDAO:
    def __init__(self, path: str):
        self.path = path

    def get_posts(self) -> list[dict]:
        """Load JSON with all posts"""
        with open(self.path, "r", encoding="UTF-8") as file:
            return json.load(file)

    def make_hashtags_from_text(self) -> list[dict]:
        """Convert hashtags in post text to links"""
        posts: list[dict] = self.get_posts()
        for post in posts:
            phrase_split: list = post.get("content").split()
            for index in range(len(phrase_split)):
                if phrase_split[index].startswith("#"):
                    tag_word_start_re = re.compile("#\w+")
                    tag_word_end_re = re.compile("[^# \w]+")
                    tag_word_start: str = \
                        re.search(tag_word_start_re, phrase_split[index])[0]
                    if re.search(tag_word_end_re,
                                 phrase_split[index]) is not None:
                        tag_word_end: str = \
                            re.search(tag_word_end_re, phrase_split[index])[0]
                        phrase_split[index]: str = \
                            f"<a href='/tag/{tag_word_start.split('#')[-1]}'>" \
                            f"{tag_word_start}</a>{tag_word_end}"
                    else:
                        phrase_split[index]: str = \
                            f"<a href='/tag/{tag_word_start.split('#')[-1]}'>" \
                            f"{tag_word_start}</a>"
            converter_post: str = " ".join(phrase_split)
            post["content"] = converter_post
        return posts

    def get_posts_by_user(self, user_name: str) -> list[dict] | list:
        """Return all posts by user"""
        user_posts: list = []
        user_name_found: bool = False
        for post in self.make_hashtags_from_text():
            if user_name == post["poster_name"]:
                user_name_found = True
                user_posts.append(post)
        if user_name_found:
            return user_posts
        else:
            raise ValueError("User not found")

    def get_post_by_pk(self, pk: int) -> dict | None:
        """Return single post by pk"""
        for post in self.make_hashtags_from_text():
            if pk == post["pk"]:
                return post

    def search_for_posts(self, query: str) -> list[dict] | list:
        """Return all posts by word"""
        founded_posts: list = []
        for post in self.make_hashtags_from_text():
            if query.lower() in post["content"].lower():
                founded_posts.append(post)
        return founded_posts
