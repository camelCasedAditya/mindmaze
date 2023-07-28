from django.shortcuts import get_object_or_404, render
from .models import Puzzle
from .forms import AnswerForm

def index(request):
    problem_set = Puzzle.objects.all()
    context = {"problem_set": problem_set}
    return render(request, "puzzles/index.html", context)

def detail(request, puzzle_id):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            #correct
            student_answer = form.cleaned_data["student_answer"]
    else:
        form = AnswerForm()
    puzzle = get_object_or_404(Puzzle, pk=puzzle_id)
    return render(request, "puzzles/detail.html", {"puzzle": puzzle, "form": form})