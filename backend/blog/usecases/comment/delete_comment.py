from blog.domain.repositories.comment_repository import CommentRepository


class DeleteCommentUseCase:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def execute(self, comment_id: str) -> None:
        self.repository.delete_comment(comment_id)
