from django.shortcuts import render

# Create your views here.

def skill(request):
    context = {'skill':'active'}
    return render(request, 'skill.html', context)

def about(request):
    context = {'about':'active'}
    return render(request, 'about.html', context)