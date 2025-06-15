from blog.domain.repositories.post_repository import PostRepository
from blog.domain.entities.post import Post
from typing import List


class GetAllPostsUseCase:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self) -> List[Post]:
        return self.repository.get_all()
