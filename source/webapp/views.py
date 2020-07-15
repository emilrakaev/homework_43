from django.shortcuts import render


def calculation(request):
    if request.method == 'GET':
        return render(request, 'calculate_form.html')
    elif request.method == 'POST':
        res = 0
        if request.POST.get('sign') == '+':
            res = int(request.POST.get('first')) + int(request.POST.get('second'))
        elif request.POST.get('sign') == '-':
            res = int(request.POST.get('first')) - int(request.POST.get('second'))
        elif request.POST.get('sign') == '*':
            res = int(request.POST.get('first')) * int(request.POST.get('second'))
        elif request.POST.get('sign') == '/':
            res = int(request.POST.get('first')) / int(request.POST.get('second'))
        context = {
            'first': request.POST.get('first'),
            'second': request.POST.get('second'),
            'sign': request.POST.get('sign'),
            'result': res
        }
        return render(request, 'result.html', context)

