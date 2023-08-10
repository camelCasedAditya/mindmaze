from django.shortcuts import get_object_or_404, render
from .models import Puzzle
from .forms import AnswerForm
from users.models import Puzzles_Solved
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def index(request):
    level_set = Group.objects.filter(user = request.user)
    for g in level_set:
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
    completed_set = Puzzles_Solved.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
    for i in completed_set:
            problem_set = Puzzle.objects.filter(level = user_level).exclude(pk=i)

    # completed_set = Puzzles_Solved.objects.filter(user = request.user.username)

    # for

    context = {"problem_set": problem_set}
    return render(request, "puzzles/index.html", context)

@login_required
def detail(request, puzzle_id_detail):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            #correct
            student_answer = form.cleaned_data["student_answer"]
    else:
        form = AnswerForm()
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id_detail)
    return render(request, "puzzles/detail.html", {"puzzle": puzzle, "form": form})