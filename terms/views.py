from django.shortcuts import get_object_or_404, render
from .models import Term
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from puzzles.models import Puzzle
from users.models import Submission

def home(request):
    is_admin = request.user.is_staff
    term_list = Term.objects.all()
    current_term = term_list.last()
    return render(request, "home.html", {"is_admin":is_admin, "current_term":current_term, "term_list":term_list})

def term_view(request, year, season):
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

    solved = [0]*(term.length+1)
    incorrect = [0]*(term.length+1)
    total = [0]*(term.length+1)
    weeks = [0]*(term.length+1)
    weeks_progress = []

    for week in range(1, term.length+1):
        puzzles = Puzzle.objects.filter(term=term, week=week, level=user_level)
        for puzzle in puzzles:
            submission = Submission.objects.filter(user=request.user, puzzle_id=puzzle.id)
            if submission.exists():
                if submission[0].is_correct:
                    solved[week] += 1
                else:
                    incorrect[week] += 1
            total[week] += 1

        if puzzles.exists():
            solved[week] /= total[week]
            solved[week] *= 100
            incorrect[week] /= total[week]
            incorrect[week] *= 100
            weeks[week] = week
            weeks_progress.append((weeks[week], solved[week], incorrect[week]))

    return render(request, "term.html", {"term":term, "weeks":weeks_progress})


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
    solved = 0
    incorrect = 0
    unanswered = 0

    for puzzle in puzzles:
        submission = Submission.objects.filter(user=request.user, puzzle_id=puzzle.id)
        if submission.exists():
            submissions[puzzle.number] = submission[0]
            if submission[0].is_correct:
                solved += 1
            else:
                incorrect += 1
        else:
            unanswered += 1

    problems = zip(puzzles, submissions[1:])

    return render(request, "week.html", {"term":term, "week":week, "problem_set":problems,
                                         "solved":solved, "incorrect":incorrect, "unanswered":unanswered})

def class_view(request):
    if not request.user.is_staff: #user does not have permission to see
        return render(request, "profile.html", {"access":False})
    else:
        level_set = Group.objects.filter(user = request.user)
        for g in level_set:
            groupname = g.name
        student_list = User.objects.filter(groups__name=groupname)
        student_names = []
        student_submissions = []
        for student in student_list:
            student_names.append(student.get_full_name)
            student_submissions.append(Submission.objects.filter(user=student))

        class_details = zip(student_list, student_submissions)

        return render(request, "class.html", {"class":class_details})

def my_stats(request):
    user = request.user
    user_submissions = Submission.objects.filter(user=user)
    puzzle_set = []
    for submission in user_submissions:
        puzzle = get_object_or_404(Puzzle, pk=submission.puzzle_id)
        puzzle_set.append(puzzle)
    
    problems = zip(puzzle_set, user_submissions)
    return render(request, "profile.html", {"access":True, "problem_set":problems})

def user_stats(request, username):
    user = User.objects.get(username=username)
    if user != request.user and not request.user.is_staff: #user does not have permission to see
        return render(request, "profile.html", {"access":False})
    else:
        user_submissions = Submission.objects.filter(user=user)
        puzzle_set = []
        for submission in user_submissions:
            puzzle = get_object_or_404(Puzzle, pk=submission.puzzle_id)
            puzzle_set.append(puzzle)
        
        problems = zip(puzzle_set, user_submissions)
        return render(request, "profile.html", {"access":True, "problem_set":problems})