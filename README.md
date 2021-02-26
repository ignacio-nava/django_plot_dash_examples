# Django Plot Dash | Examples
In this repository, I'll be working with the package [django-plotly-dash](https://django-plotly-dash.readthedocs.io/en/latest/index.html), exemplifying different types of plots.

Follow the [Usage](https://github.com/ignacio-nava/django_plot_dash_examples/blob/master/README.md#clone) instructions to run it locally. If you want to add examples of your own, read the [Adding Plots](https://github.com/ignacio-nava/django_plot_dash_examples/blob/master/README.md#adding-plots) section.


## Clone
```bash
git clone https://github.com/ignacio-nava/django_plot_dash_examples.git
cd django_plot_dash_examples/
```

## Usage
1. Create a virtual environment and activate it
```bash
python3 -m venv {venv_name}
source {venv_name}/bin/activate
```

2. Install requirements
```bash
pip install -r requirements.txt
```

3. Migrate
```bash
cd django_plot_dash_examples/
python3 manage.py migrate
```

4. Run server
```bash
python3 manage.py runserver
```

## Adding Plots
1. In the folder [django_plot_dash_examples/django_pd_examples/plots_examples/](https://github.com/ignacio-nava/django_plot_dash_examples/tree/master/django_pd_examples/plots_examples), add a python file-like [example_1.py](https://github.com/ignacio-nava/django_plot_dash_examples/blob/master/django_pd_examples/plots_examples/example_1.py). 

2. Then name the [app](https://github.com/ignacio-nava/django_plot_dash_examples/blob/cf47e74353162a2af3bc326d46bb52e56e09b50f/django_pd_examples/plots_examples/example_1.py#L7) as the python file. For example, if the file is called *my_own_example.py* you must use:
```python
app = DjangoDash('my_own_example')
```

3. Finally, in [examples.py](https://github.com/ignacio-nava/django_plot_dash_examples/tree/master/django_pd_examples/plots_examples/examples.py), import your plot.
```python
from . import example_1.py, my_own_example
```

After this, you will be able to see the link to your plot on the homepage.
