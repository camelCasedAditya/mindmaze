from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from puzzles.models import Puzzle
from users.models import Submission
from django.contrib.auth.models import Group
from users.models import Submission
import plotly.offline as plot
import pandas as pd

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        # puzzles = Puzzle.objects.all().count()
        query_set = Group.objects.filter(user = request.user)
        for g in query_set:
            groupname = g.name
        if groupname == 'Level_1':
            user_level = 1
        elif groupname == 'Level_2':
            user_level = 2
        elif groupname == 'Level_3':
            user_level = 3
        elif groupname == 'Level_4':
            user_level = 4
        elif groupname == 'Elite_Level':
            user_level = 5
        elif groupname == 'Default':
            user_level = 1
        problem_set = Puzzle.objects.filter(level = user_level)
        completed_set = Submission.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
        for i in completed_set:
            problem_set = problem_set.exclude(pk = i)
        problem_set = list(problem_set)
        puzzles_pending = len(problem_set)

        puzzles_solved = len(list(Submission.objects.filter(user = request.user)))
        puzzles_solved_correctly = len(list(Submission.objects.filter(user = request.user, is_correct = True)))
        puzzles_solved_incorrectly = (puzzles_solved - puzzles_solved_correctly)
        data = [puzzles_solved_correctly, puzzles_solved_incorrectly]
        return render(request, 'dashboard/dashboard.html', {'puzzle':puzzles_pending, 'groups':groupname, "data":data, "puzzles_solved":puzzles_solved})

    else:
        return redirect('login')