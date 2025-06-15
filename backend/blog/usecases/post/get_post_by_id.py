from blog.domain.repositories.post_repository import PostRepository
from blog.domain.entities.post import Post
from typing import Optional


class GetPostByIdUseCase:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self, post_id: str) -> Optional[Post]:
        return self.repository.get_by_id(post_id)
