from django.shortcuts import render
from .models import Term
from django.contrib.auth.models import Group
from puzzles.models import Puzzle
from users.models import Submission

def home(request):
    term_list = Term.objects.all()
    return render(request, "home.html", {"term_list":term_list})

def list(request, year):
    term_list = Term.objects.all()
    return render(request, "home.html", {"term_list":term_list})

def term_view(request, year, season):
    term = Term.objects.all().filter(year=year, season=season)[0]
    problem_set_preview = [[0 for i in range(5)] for j in range(term.length)]
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

    for week in range(term.length):
        puzzles = Puzzle.objects.filter(term=term, week=week, level=user_level)
        #print(week)
        #print(puzzles)
        for i in range(puzzles.count()):
            problem_set_preview[week][i] = puzzles[i]
        #print(problem_set_preview[week])
    weeks = range(1,term.length+1)
    return render(request, "term.html", {"term":term, "preview":problem_set_preview})

def week_view(request, year, season, week):
    term = Term.objects.all().filter(year=year, season=season)[0]
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
    puzzles = Puzzle.objects.filter(term=term, week=week, level=user_level)
    submissions = [0 for _ in range(0,puzzles.count()+1)]
    for puzzle in puzzles:
        submission = Submission.objects.filter(user=request.user, puzzle_id=puzzle.id)
        if submission.exists():
            submissions[puzzle.number] = submission[0]
    

    problems = zip(puzzles, submissions[1:])

    return render(request, "week.html", {"term":term, "week":week, "problem_set":problems})
