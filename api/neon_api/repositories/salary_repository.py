from django.db.models import Avg, Max, Min, F

from neon_api.models import User as UserModel, User
from neon_api.models import Salary as SalaryModel
from neon_api.domain.salary import Salary


class SalaryRepository:
    def __init__(self):
        pass

    def _get_user_model(self, cpf):
        return UserModel.objects.get(cpf=cpf)

    def _get_salary_model(self, date, user_model):
        return SalaryModel.objects.get(date=date, user=user_model)

    def create(self, salary_data, cpf):
        user_model = UserModel.objects.get(cpf=cpf)
        salary_model = SalaryModel.objects.create(user=user_model, **salary_data)
        return salary_model

    def get_all_salaries(self):
        return SalaryModel.objects.all()

    def get_salaries_by_cpf(self, cpf):
        return SalaryModel.objects.filter(user__cpf=cpf)

    def update(self, salary_model, update_data):
        salary_model.amount = update_data['amount']
        salary_model.discount = update_data['discount']
        salary_model.save()
        return self._model_to_domain(salary_model)

    def get_salary_by_id(self, salary_id):
        return SalaryModel.objects.filter(id=salary_id).first()

    def delete(self, salary_id):
        SalaryModel.objects.filter(id=salary_id).delete()
        return True

    def _model_to_domain(self, salary_model):
        return Salary(salary_model.date, salary_model.amount, salary_model.discount, salary_model.user.cpf, salary_model.id)

    def get_dashboard_data(self, cpf=None):
        salaries = self.get_all_salaries() if cpf is None else self.get_salaries_by_cpf(cpf)
        salaries = salaries.annotate(net_salary=F('amount') - F('discount'))

        return {
            "averageSalary": salaries.aggregate(Avg('net_salary'))['net_salary__avg'],
            "averageDiscount": salaries.aggregate(Avg('discount'))['discount__avg'],
            "highestSalary": salaries.aggregate(Max('net_salary'))['net_salary__max'],
            "lowestSalary": salaries.aggregate(Min('net_salary'))['net_salary__min'],
        }
