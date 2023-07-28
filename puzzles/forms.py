from django import forms

class AnswerForm(forms.Form):
    student_answer = forms.CharField(label="Answer", max_length=100)