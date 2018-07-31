from django.shortcuts import render
from django.utils import timezone
from .models import SelectScent


def post_list(request):
    posts = SelectScent.objects.filter(select_date__lte=timezone.now()).order_by('select_date')
    return render(request, 'perfume/perfume_list.html', {'posts': posts})
