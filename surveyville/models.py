from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager


# Create your models here.
class Account(AbstractBaseUser):
    USERNAME_FIELD = 'username'
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length = 254)
    password = models.CharField(("password"), max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

class Survey(models.Model):
    s_title = models.CharField(max_length=255)
    s_text = models.CharField(max_length=255)
    create_date = models.DateField()
    expire_date = models.DateField()
    user_FK = models.ForeignKey(Account, on_delete=models.CASCADE)

class Question(models.Model):
    q_text = models.CharField(max_length=255)
    survey_FK = models.ForeignKey(Survey, on_delete=models.CASCADE)

class Answer(models.Model):
    a_text = models.CharField(max_length=255)
    question_FK = models.ForeignKey(Question, on_delete=models.CASCADE)

class Vote(models.Model):
    answer_FK = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user_FK = models.ForeignKey(Account, on_delete=models.CASCADE)