from django.conf import settings as django_settings
from plots.plots_examples import examples

def settings(request):
    examples_list = [example for example in examples.__dir__() if not example.startswith('__')]
    return {
        'settings': django_settings,
        'examples': examples_list,
    }
