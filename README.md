# Django Plot Dash | Examples
In this repository, I'll be working with the package [django-plotly-dash](https://django-plotly-dash.readthedocs.io/en/latest/index.html), exemplifying different types of plots.

Follow the [Usage](https://github.com/ignacio-nava/django_plot_dash_examples/blob/master/README.md#clone) instructions to run it locally. If you want to add examples of your own, read the **Adding Plots** section.


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