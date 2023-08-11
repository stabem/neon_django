from django.views import View
from django.http import JsonResponse
from neon_api.services.salary_service import SalaryService


class DashboardController(View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.salary_service = SalaryService()

    def get(self, request, cpf=None):
        data = self.salary_service.get_dashboard_data(cpf)
        return JsonResponse(data)
