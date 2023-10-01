from django.db import models
from django.contrib.auth.models import User
from puzzles.models import Puzzle

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name="puzzles", null=True, blank=True)
    user_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.puzzle.__str__() + " - " + self.user.username