from blog.domain.repositories.post_repository import PostRepository
from blog.domain.entities.post import Post
from typing import List, Optional

class InMemoryPostRepository(PostRepository):
    def __init__(self):
        self._posts = {}

    def get_all(self) -> List[Post]:
        return list(self._posts.values())

    def get_by_id(self, post_id: str) -> Optional[Post]:
        return self._posts.get(post_id)

    def create(self, post: Post) -> Post:
        self._posts[post.id] = post
        return post

    def update(self, post: Post) -> Optional[Post]:
        if post.id in self._posts:
            self._posts[post.id] = post
            return post
        return None

    def delete(self, post_id: str) -> None:
        self._posts.pop(post_id, None)
