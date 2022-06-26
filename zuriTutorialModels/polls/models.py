from typing import Optional
from django.db import models

# Create your models here.


class Question(models.Model):
    question_text: Optional[str] = models.CharField(max_length=200)
    question_description = models.CharField(
        max_length=200, default="basic description")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.question} ---> {self.choice_answer}"
