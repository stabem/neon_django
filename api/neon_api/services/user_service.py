from neon_api.domain.user import User
from neon_api.repositories.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_user(self, cpf, name, birth_date):
        user = User(cpf, name, birth_date)
        return self.repository.create(user)

    def get_user(self, cpf):
        return self.repository.get_user_by_cpf(cpf)

    def update_user(self, cpf, name=None, birth_date=None):
        user = self.get_user(cpf)
        if user is not None:
            if name is not None:
                user.name = name
            if birth_date is not None:
                user.birth_date = birth_date
            return self.repository.update(user)
        return None

    def delete_user(self, cpf):
        return self.repository.delete(cpf)

    def get_all_users(self):
        return self.repository.get_all_users()
