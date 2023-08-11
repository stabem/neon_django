from typing import List

from neon_api.domain.salary import Salary


class User:
    def __init__(self, cpf: str, name: str, birth_date: str):
        self.cpf = cpf
        self.name = name
        self.birth_date = birth_date
        self.salaries: List[Salary] = []

    def add_salary(self, salary: Salary):
        if salary.user_cpf != self.cpf:
            raise ValueError("Salary does not belong to this user")
        self.salaries.append(salary)
