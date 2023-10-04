from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_answer = models.CharField(max_length=200)
    puzzle_id = models.IntegerField()
    is_correct = models.BooleanField()
    attempts = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)], )

    def __int__(self):
        return self.puzzle_id