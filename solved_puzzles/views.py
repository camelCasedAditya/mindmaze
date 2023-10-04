from django.shortcuts import render, get_object_or_404
from puzzles.models import Puzzle
from users.models import Submission
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
@login_required
def index(request):
    completed_set = Submission.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
    solved = Puzzle.objects.filter(pk__in=completed_set)
    context = {"solved": solved}
    return render(request, "solved_puzzles/index.html", context)

@login_required
def detail(request, puzzle_id):
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    past_submission = Submission.objects.filter(user = request.user, puzzle_id = puzzle_id)
    answered = True

    user_answer = Submission.objects.filter(user = request.user, puzzle_id = puzzle_id).values_list('user_answer', flat=True)
    user_answer = user_answer[0]
    # solved = Puzzle.objects.filter(pk__in=completed_set)
    # submissions = Submission.objects.filter(user = request.user)
    completed_set = Submission.objects.filter(user = request.user).values_list('puzzle_id', flat=True)
    problem_set = Puzzle.objects.filter(pk__in=completed_set)
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

    context = {"puzzle": puzzle, "submission": past_submission, "answered": answered, "answer":user_answer, "next_puzzle": next_puzzle, "prev_puzzle": prev_puzzle}
    return render(request, "solved_puzzles/detail.html", context)