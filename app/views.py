from django.shortcuts import render
from .forms import IndexForm
from knn_model.utils import preprocessing, predict

# Create your views here.
def index(req):
    return render(req, 'index.jinja', {'form': IndexForm()})

def result(req):
    if req.method == 'POST':
        print(1 if req.POST['gender'][0] == 'M' else 0)
        high_bp = 0 if req.POST['high_bp'][0] == 'N' else 1
        high_chol = 0 if req.POST['high_chol'][0] == 'N' else 1
        chol_check = 0 if req.POST['chol_check'][0] == 'N' else 1
        gender = 1 if req.POST['gender'][0] == 'M' else 0
        content = preprocessing({
            "outcome": [0],
            "HighBP": [high_bp],
            "HighChol": [high_chol],
            "CholCheck": [chol_check],
            "BMI": [int(req.POST['bmi'])],
            "Sex": [gender],
            "Age": [int(req.POST['age'])],
        })
        return render(req, 'result.jinja', {'status': predict(content)[0]})
    return render(req, 'result.jinja', {'status': False})