from django.db import models


class User(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    class Meta:
        db_table = 'user'


class Salary(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    user = models.ForeignKey(User, related_name='salaries', on_delete=models.CASCADE)

    class Meta:
        db_table = 'salary'

