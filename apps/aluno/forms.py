from django import forms
from apps.aluno.models import aluno

class alunosforms(forms.ModelForm): 
    class meta:
        model = aluno
        exclude = ["",]
        labels = {
            "matricula" : "matricula",
            "status" : "ativo"
        }

        widgets = {
            "nome" : forms.TextInput(attrs={"class": "form-control", "autofocus" : "autofocus"}),
            "matricula" : forms.TextInput(attrs={"class": "form-control"}),
            "email"  : forms.EmailInput(attrs={"class": "form-control"}),
            "telefone" : forms.TextInput(attrs={"class": "form-control"}),
            "status"  :forms.CheckboxInput(attrs={"class": "form-control" "form-check-input"})
        }