from django.shortcuts import get_object_or_404, render
from django.db.models import Q
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
    completed_set = Submission.objects.filter(Q(attempts=3) | Q(is_correct=True), user = request.user).values_list('puzzle_id', flat=True)
    for i in completed_set:
        problem_set = problem_set.exclude(pk = i)
    no_puzzles = False
    puzzles_left = list(problem_set)
    if (len(puzzles_left) == 0):
        no_puzzles = True
    context = {"problem_set": problem_set, "no_puzzles":no_puzzles}
    return render(request, "puzzles/index.html", context)

@login_required
def detail(request, puzzle_id_detail):
    answered = False
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id_detail)
    past_submission = Submission.objects.filter(user = request.user, puzzle_id = puzzle_id_detail)
    try:
        past_attempts = Submission.objects.filter(puzzle_id = puzzle_id_detail).values_list("attempts", flat=True)
        past_attempts = list(past_attempts)
        past_attempts = int(past_attempts[0])
    except:
        past_attempts = 0

    attempts_left = 3 - int(past_attempts)
    if (past_attempts == 0):
        attempts_left = 3

    if past_attempts == 3:
        answered = True

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
    completed_set = Submission.objects.filter(Q(attempts=3) | Q(is_correct=True), user = request.user).values_list('puzzle_id', flat=True)
    for i in completed_set:
        problem_set = problem_set.exclude(pk = i)

    next_puzzle_exists = True
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


    if (past_attempts < 3):
        if request.method == "POST":
            form = AnswerForm(request.POST or None)
            if form.is_valid():
                
                if past_attempts > 0:
                    past_attempts += 1
                    student_answer = form.cleaned_data["student_answer"]
                    submission = Submission.objects.filter(user=request.user, puzzle_id=puzzle_id_detail).update(user_answer=student_answer, is_correct=(puzzle.solution==student_answer), attempts=past_attempts)
                    if (student_answer == puzzle.solution):
                        past_attempts = 3
                    if past_attempts == 3:
                        answered = True
                    else:
                        answered = False

                    if (len(problem_set) == 0):
                        next_puzzle_exists = False
                    form = AnswerForm(request.POST)
                    attempts_left = 3 - int(past_attempts)
                    return render(request, "puzzles/detail.html", {"puzzle": puzzle, "submission": submission, "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle, "button_enabled":next_puzzle_exists, "form":form, "student_answer":student_answer, "attempts_left":attempts_left})

                else:
                    past_attempts += 1
                    student_answer = form.cleaned_data["student_answer"]
                    if (student_answer == puzzle.solution):
                        past_attempts = 3
                    submission = Submission.objects.create(user=request.user, user_answer=student_answer, 
                                                            puzzle_id=puzzle_id_detail, is_correct=(puzzle.solution==student_answer), attempts=past_attempts)
                    if past_attempts == 3:
                        answered = True
                    else:
                        answered = False

                    if (len(problem_set) == 0):
                        next_puzzle_exists = False
                    attempts_left = 3 - int(past_attempts)
                    if (past_attempts == 0):
                        attempts_left = 3
                    return render(request, "puzzles/detail.html", {"puzzle": puzzle, "submission": submission, "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle, "button_enabled":next_puzzle_exists, "form":form, "student_answer":student_answer, "attempts_left":attempts_left})
        else:
            form = AnswerForm()
            return render(request, "puzzles/detail.html", {"puzzle": puzzle, "form": form, "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle, "button_enabled":next_puzzle_exists, "attempts_left":attempts_left})
    else:
        return render(request, "puzzles/detail.html", {"puzzle": puzzle, "submission": past_submission[0], "answered": answered, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle, "button_enabled":next_puzzle_exists, "attempts_left":attempts_left})
    
