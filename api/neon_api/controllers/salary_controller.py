from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from neon_api.services.salary_service import SalaryService
from neon_api.controllers.serializers.salary_serializer import SalarySerializer


@method_decorator(csrf_exempt, name='dispatch')
class SalaryController(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.salary_service = SalaryService()

    def post(self, request):
        data = JSONParser().parse(request)["data"]
        serializer = SalarySerializer(data=data)
        if serializer.is_valid():
            salary_data = serializer.validated_data
            cpf = data['cpf']
            salary = self.salary_service.create_salary(
                salary_data['date'],
                salary_data['amount'],
                salary_data['discount'],
                cpf
            )
            return JsonResponse(SalarySerializer(salary).data)

        return JsonResponse(serializer.errors, status=400)

    def get(self, request, cpf=None):
        if cpf:
            salary = self.salary_service.get_salary_by_cpf(cpf)
            serializer = SalarySerializer(salary, many=True)
        else:
            salaries = self.salary_service.get_all_salaries()
            serializer = SalarySerializer(salaries, many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, salary_id):
        data = JSONParser().parse(request)['data']
        salary_model = self.salary_service.get_salary(salary_id)
        if salary_model:
            serializer = SalarySerializer(salary_model, data=data, partial=True)

            if serializer.is_valid():
                updated_salary = self.salary_service.update_salary(salary_id, serializer.validated_data)
                return JsonResponse(SalarySerializer(updated_salary).data)

            return JsonResponse(serializer.errors, status=400)

        return JsonResponse({'error': 'Salary not found'}, status=404)

    def delete(self, request, salary_id):
        self.salary_service.delete_salary(salary_id)
        return HttpResponse(status=204)

