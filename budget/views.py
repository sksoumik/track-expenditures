from django.shortcuts import render


def project_list(request):
    return render(request, 'budget/project_list.html')


def project_detail(request, project_slug):
    return render(request, 'budget/project_detail.html')
