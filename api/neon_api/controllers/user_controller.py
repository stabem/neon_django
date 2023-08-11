from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
from neon_api.services.user_service import UserService
from neon_api.controllers.serializers.user_serializer import UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserController(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        data = JSONParser().parse(request)["data"]
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            user = serializer.save()

            existing_user = self.user_service.get_user(user.cpf)
            if existing_user:
                return JsonResponse({'error': 'Usuário já existe com esse cpf'}, status=409)

            user_created = self.user_service.create_user(user.cpf, user.name, user.birth_date)
            return JsonResponse(UserSerializer(user_created).data)
        return JsonResponse(serializer.errors, status=400)


    def get(self, request, cpf=None):
        if cpf:
            user = self.user_service.get_user(cpf)
            serializer = UserSerializer(user)
        else:
            users = self.user_service.get_all_users()
            serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, cpf):
        user_data = JSONParser().parse(request)["data"]
        existing_user = self.user_service.get_user(cpf)
        serializer = UserSerializer(existing_user, data=user_data)
        if serializer.is_valid():
            updated_user = serializer.save()
            self.user_service.update_user(cpf, updated_user.name, updated_user.birth_date)
            return JsonResponse(UserSerializer(updated_user).data)
        return JsonResponse(serializer.errors, status=400)

    def delete(self, request, cpf):
        self.user_service.delete_user(cpf)
        return HttpResponse(status=204)
