from django.shortcuts import render
from regex.services import RegexMatchService


def index_view(request):
    context = {}

    if request.method == 'POST':
        data = request.POST
        pattern = data['pattern']
        string = data['string']

        context['response'] = RegexMatchService.check_regex_and_get_response(
            pattern=pattern,
            string=string
        )
        context['pattern'] = pattern
        context['string'] = string

    return render(
        request=request,
        template_name='index.html',
        context=context
    )
