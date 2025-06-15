from blog.domain.value_objects.email_vo import Email
from blog.domain.value_objects.password import Password
from blog.domain.entities.user import User
from blog.domain.repositories.user_repository import UserRepository
from typing import Optional


class LoginUserUseCase:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def execute(self, email: Email, password: Password) -> Optional[User]:
        return self.repository.login(email, password)
