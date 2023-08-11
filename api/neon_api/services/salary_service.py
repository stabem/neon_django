from neon_api.domain.salary import Salary
from neon_api.repositories.salary_repository import SalaryRepository


class SalaryService:
    def __init__(self):
        self.repository = SalaryRepository()

    def create_salary(self, date, amount, discount, cpf):
        salary_data = {
            'date': date,
            'amount': amount,
            'discount': discount
        }
        return self.repository.create(salary_data, cpf)

    def get_salary(self, salary_id):
        return self.repository.get_salary_by_id(salary_id)

    def get_salary_by_cpf(self, cpf):
        return self.repository.get_salaries_by_cpf(cpf)

    def get_all_salaries(self):
        return self.repository.get_all_salaries()

    def update_salary(self, salary_id, update_data):
        salary_model = self.repository.get_salary_by_id(salary_id)
        if salary_model:
            update_data['amount'] = update_data.get('amount', salary_model.amount)
            update_data['discount'] = update_data.get('discount', salary_model.discount)
            return self.repository.update(salary_model, update_data)
        return None

    def delete_salary(self, salary_id):
        return self.repository.delete(salary_id)

    def get_dashboard_data(self, cpf=None):
        return self.repository.get_dashboard_data(cpf)
