from django.db import models
import chess
import chess.svg

class Puzzle(models.Model):
    position_fen = models.CharField(max_length=200)
    level = models.IntegerField(default=0)
    label = models.CharField(max_length=200)
    instruction = models.CharField(max_length=200)
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.label
    
    def position_diagram(self):
        return chess.svg.board(chess.Board(self.position_fen), size=400)
