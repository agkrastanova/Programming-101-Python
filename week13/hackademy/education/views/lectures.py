from django.shortcuts import render, get_object_or_404

from education.models import Lecture


def list(request):
    return render(request, 'lectures/list.html', {'lectures': Lecture.objects.all()})


def detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    return render(request, 'lectures/detail.html', {'lecture': lecture})
