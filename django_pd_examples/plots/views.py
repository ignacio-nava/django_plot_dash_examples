from django.shortcuts import render

from plots_examples import examples

def exampleDetailView(request, example):
    template_name = 'plots/plot_detail.html'
    reference = getattr(examples, example).reference
    ctx = {
        'example': example,
        'reference': reference
        }
    return render(request, template_name, ctx)