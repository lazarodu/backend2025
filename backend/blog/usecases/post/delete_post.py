from blog.domain.repositories.post_repository import PostRepository


class DeletePostUseCase:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def execute(self, post_id: str) -> None:
        self.repository.delete(post_id)
