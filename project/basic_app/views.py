from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)
from . import models
from basic_app.forms import form

class IndexView(TemplateView):
    # Just set this Class Object Attribute to the template page.
    # template_name = 'app_name/site.html'
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class SchoolListView(ListView):
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ("name","principal","location","pics")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal","pics")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class StudentCreateView(CreateView):
    fields = ("name","age","school","Student_Report")
    model = models.Student

class StudentUpdateView(UpdateView):
    fields = ("name","age")
    model = models.Student


class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:list")
