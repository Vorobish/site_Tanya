from django.db import models


class SignUp(models.Model):
    '''
        Запись
    '''
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    comment = models.TextField(max_length=300)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# python manage.py migrate
# python manage.py makemigrations
