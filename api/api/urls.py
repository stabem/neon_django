from django.urls import path

from neon_api.controllers.dashboard_controller import DashboardController
from neon_api.controllers.user_controller import UserController
from neon_api.controllers.salary_controller import SalaryController

salary_controller = SalaryController()

urlpatterns = [
    path('users/', UserController.as_view()),
    path('users/<str:cpf>/', UserController.as_view()),
    path('dashboard/<str:cpf>/', DashboardController.as_view()),
    path('dashboard/', DashboardController.as_view()),
    path('salaries/', SalaryController.as_view()),
    path('salaries/user/<str:cpf>/', SalaryController.as_view()),
    path('salaries/<int:salary_id>/', SalaryController.as_view()),
]

