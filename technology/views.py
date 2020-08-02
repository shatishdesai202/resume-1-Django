from django.shortcuts import render

# Create your views here.

def tech(request):
    context = {'tech':'active'}
    return render(request, 'tech.html', context)