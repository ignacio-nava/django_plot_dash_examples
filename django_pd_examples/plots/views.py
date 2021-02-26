from django.shortcuts import render

from plots_examples import examples

def exampleDetailView(request, example):
    template_name = 'plots/plot_detail.html'
    plot_example = getattr(examples, example)
    ctx = {
        'example': example,
        'reference': plot_example.reference,
        'ratio': plot_example.ratio
        }
    return render(request, template_name, ctx)