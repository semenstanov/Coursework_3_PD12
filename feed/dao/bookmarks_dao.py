import json


class BookmarksDAO:
    def __init__(self, path: str):
        self.path = path

    def get_bookmarks(self) -> list[dict] | list:
        """Load JSON with all bookmarks"""
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_bookmarks(self, data: list[dict]) -> None:
        """Save bookmarks to the file"""
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_bookmark(self, post: dict) -> None:
        """Add a bookmark to the file"""
        data: list[dict] | list = self.get_bookmarks()
        founded_posts: int = 0
        for post_data in data:
            if post_data.get('pk') == post.get('pk'):
                founded_posts += 1
        if founded_posts == 0:
            data.append(post)
            self.save_bookmarks(data)

    def delete_bookmark(self, pk: int) -> None:
        """Delete bookmark from the file"""
        data: list[dict] | list = self.get_bookmarks()
        for index, bookmark in enumerate(data):
            if bookmark["pk"] == pk:
                del data[index]
                break
        self.save_bookmarks(data)
