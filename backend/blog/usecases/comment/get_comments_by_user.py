from blog.domain.repositories.comment_repository import CommentRepository
from blog.domain.entities.comment import Comment
from typing import List


class GetCommentsByUserUseCase:
    def __init__(self, repository: CommentRepository):
        self.repository = repository

    def execute(self, user_id: str) -> List[Comment]:
        return self.repository.get_comments_by_user(user_id)
