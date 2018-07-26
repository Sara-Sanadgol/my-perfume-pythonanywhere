from django.shortcuts import render


def perfume_list(request):
    return render(request, 'perfume/perfume-list.html', {})
