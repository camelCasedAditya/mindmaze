from django.db import models
from django.contrib.auth.models import User

class Puzzles_Solved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    puzzle_id=models.IntegerField()
    puzzle_correctness=models.BooleanField()

    def __int__(self):
        return self.puzzle_id