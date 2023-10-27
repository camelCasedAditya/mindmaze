from django.db import models

class Term(models.Model):
    year = models.IntegerField()
    season = models.CharField(max_length=10)
    length = models.IntegerField(default=1)
    current_week = models.IntegerField()
    
    def __str__(self):
        return str(self.year)+" "+self.season

    def name(self):
        return self.season+str(self.year)