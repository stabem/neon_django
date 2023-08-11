from neon_api.domain.user import User
from neon_api.models import User as UserModel


class UserRepository:
    def __init__(self):
        pass

    def _get_user_model(self, cpf):
        return UserModel.objects.get(cpf=cpf)

    def create(self, user):
        user_model = UserModel.objects.create(cpf=user.cpf, name=user.name, birth_date=user.birth_date)
        return self._model_to_domain(user_model)

    def get_all_users(self):
        return UserModel.objects.all()

    def get_user_by_cpf(self, cpf):
        return UserModel.objects.filter(cpf=cpf).first()

    def update(self, user):
        user_model = self._get_user_model(user.cpf)
        user_model.name = user.name
        user_model.birth_date = user.birth_date
        user_model.save()
        return self._model_to_domain(user_model)

    def delete(self, cpf):
        UserModel.objects.filter(cpf=cpf).delete()
        return True

    def _model_to_domain(self, user_model):
        return User(user_model.cpf, user_model.name, user_model.birth_date)
