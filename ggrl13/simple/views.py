from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from .models import FormDataModel


class ResultsView(ListView):
    model = FormDataModel
    template_name = 'simple/results.html'


class InputFormView(View):
    template_name = 'simple/dynamic_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        payload = request.POST.dict()
        payload.pop('csrfmiddlewaretoken', None)
        FormDataModel.objects.create(inputs=payload)

        return redirect("simple:results")


