from django.http import HttpResponse
from django.views.generic import TemplateView


class MainPageView(TemplateView):
    template_name = 'main.html'


def tokenizer_test(request):
    print(request)
    return HttpResponse(status=201)
