from django.shortcuts import render
from .forms import RegexForm
import re


def index_view(request):
    context = {}
    if request.method == 'POST':
        form = RegexForm(request.POST)
        if form.is_valid():
            pattern = form.cleaned_data['pattern']
            string = form.cleaned_data['string']

            response = 'Текст не найден'
            match = None

            try:
                valid_pattern = re.compile(pattern)
            except re.error:
                response = 'Регулярное выражение неверно'
            else:
                match = valid_pattern.match(string=string)

            if match is not None:
                response = 'Найдено совпадение'

            context['response'] = response

    else:
        form = RegexForm()

    context['form'] = form

    return render(
        request=request,
        template_name='index.html',
        context=context
    )
