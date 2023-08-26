from django.shortcuts import get_object_or_404, render
from .models import Puzzle
from .forms import AnswerForm
from users.models import Submission
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
    completed_set = Submission.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
    for i in completed_set:
        problem_set = problem_set.exclude(pk = i)
    context = {"problem_set": problem_set}
    return render(request, "puzzles/index.html", context)

@login_required
def detail(request, puzzle_id_detail):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id_detail)
    past_submission = Submission.objects.filter(user = request.user, puzzle_id = puzzle_id_detail)
    answered = past_submission.exists()

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
    completed_set = Submission.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
    for i in completed_set:
        problem_set = problem_set.exclude(pk = i)

    
    problem_set = list(problem_set)
    puzzle_index = problem_set.index(puzzle)
    problem_set_len = len(problem_set)
    if (puzzle_index+1) > (problem_set_len-1):
        next_puzzle = problem_set[0]
    else:
        next_puzzle = problem_set[puzzle_index+1]
    if (puzzle_index-1) < 0:
        prev_puzzle = problem_set[problem_set_len-1]
    else:
        prev_puzzle = problem_set[puzzle_index-1]


    if not answered:
        if request.method == "POST":
            form = AnswerForm(request.POST)
            if form.is_valid():
                answered = True
                student_answer = form.cleaned_data["student_answer"]
                submission = Submission.objects.create(user=request.user, user_answer=student_answer, 
                                                        puzzle_id=puzzle_id_detail, is_correct=(puzzle.solution==student_answer))
                return render(request, "puzzles/detail.html", {"puzzle": puzzle, "submission": submission, "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle})
        else:
            form = AnswerForm()
            return render(request, "puzzles/detail.html", {"puzzle": puzzle, "form": form, "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle})
    else:
        return render(request, "puzzles/detail.html", {"puzzle": puzzle, "submission": past_submission[0], "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle})