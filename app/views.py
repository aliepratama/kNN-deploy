from django.shortcuts import render
from .forms import IndexForm

# Create your views here.
def index(req):
    return render(req, 'index.jinja', {'form': IndexForm()})

def result(req):
    if req.method == 'POST':
        return render(req, 'result.jinja', {'status': True})
    return render(req, 'result.jinja', {'status': False})