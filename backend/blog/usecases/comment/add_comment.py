from blog.domain.entities.comment import Comment
from blog.domain.repositories.comment_repository import CommentRepository


class AddCommentUseCase:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def execute(self, comment: Comment) -> Comment:
        return self.repository.add_comment(comment)
