from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from puzzles.models import Puzzle
from django.contrib.auth.models import Group

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
        puzzleslengthlist = []
        for i in Puzzle.objects.filter(level=user_level):
            puzzleslengthlist.append(g.name)
        puzzles_pending = len(puzzleslengthlist)
        return render(request, 'dashboard/dashboard.html', {'puzzle':puzzles_pending, 'groups':groupname})

    else:
        return redirect('login')