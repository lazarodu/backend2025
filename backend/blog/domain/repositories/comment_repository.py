from abc import ABC, abstractmethod
from blog.domain.entities.comment import Comment

class CommentRepository(ABC):
    @abstractmethod
    def get_comments_by_post(self, post_id: str) -> list[Comment]: ...

    @abstractmethod
    def get_comments_by_user(self, user_id: str) -> list[Comment]: ...

    @abstractmethod
    def add_comment(self, comment: Comment) -> None: ...

    @abstractmethod
    def delete_comment(self, comment_id: str) -> None: ...