from django.shortcuts import render
from django.utils import timezone
from .models import SelectScent


def perfume_list(request):
    posts = SelectScent.objects.filter(select_date__lte=timezone.now()).order_by('select_date')
    return render(request, 'perfume/perfume-list.html', {'posts': posts})
