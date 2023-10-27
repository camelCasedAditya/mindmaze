from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from puzzles.models import Puzzle

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE, related_name="puzzles", null=True, blank=True)
    puzzle_id = models.IntegerField()
    user_answer = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    attempts = models.IntegerField(default=0, validators=[MaxValueValidator(3), MinValueValidator(0)], )

    def __str__(self):
        puzzle = Puzzle.objects.filter(id=self.puzzle_id)[0]
        return puzzle.__str__() + " - " + self.user.username