from blog.domain.repositories.comment_repository import CommentRepository
from blog.domain.entities.comment import Comment
from typing import List


class InMemoryCommentRepository(CommentRepository):
    def __init__(self):
        self._comments = {}

    def get_comments_by_post(self, post_id: str) -> List[Comment]:
        return [c for c in self._comments.values() if c.post_id == post_id]

    def get_comments_by_user(self, user_id: str) -> List[Comment]:
        return [c for c in self._comments.values() if c.user_id == user_id]

    def add_comment(self, comment: Comment) -> Comment:
        self._comments[comment.id] = comment
        return comment

    def delete_comment(self, comment_id: str) -> None:
        self._comments.pop(comment_id, None)
