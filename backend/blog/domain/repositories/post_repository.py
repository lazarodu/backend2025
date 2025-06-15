from abc import ABC, abstractmethod
from blog.domain.entities.post import Post

class PostRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Post]:
        pass

    @abstractmethod
    def get_by_id(self, post_id: str) -> Post:
        pass

    @abstractmethod
    def create(self, post: Post) -> None:
        pass

    @abstractmethod
    def update(self, post: Post) -> None:
        pass

    @abstractmethod
    def delete(self, post_id: str) -> None: 
        pass
    