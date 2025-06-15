from blog.domain.entities.post import Post
from blog.domain.repositories.post_repository import PostRepository


class CreatePostUseCase:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self, post: Post) -> Post:
        return self.repository.create(post)
