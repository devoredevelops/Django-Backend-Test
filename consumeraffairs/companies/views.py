from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Company
from .forms import CompanyForm


class CompanyDetailView(LoginRequiredMixin, DetailView):
    """ Shows Details about a Company """
    model = Company
    slug_field = "name"
    slug_url_kwarg = "name"
    fields = ["name"]


company_detail_view = CompanyDetailView.as_view()


class CompanyListView(LoginRequiredMixin, ListView):
    """ Lists Companies """
    model = Company
    slug_field = "name"
    slug_url_kwarg = "name"


company_list_view = CompanyListView.as_view()


class CompanyCreateView(LoginRequiredMixin, CreateView):
    """ Creates a Company """
    model = Company
    form = CompanyForm
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy("companies:list")


company_create_view = CompanyCreateView.as_view()


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    """ Edits a Company """
    model = Company
    form = CompanyForm
    fields = ["name"]
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_success_url(self):
        return reverse_lazy("companies:list")


company_update_view = CompanyUpdateView.as_view()


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    """ Deletes a Company """
    model = Company
    slug_field = "name"
    slug_url_kwarg = "name"
    success_url = reverse_lazy("companies:list")


company_delete_view = CompanyDeleteView.as_view()


class CompanyRedirectView(LoginRequiredMixin, RedirectView):
    """ Redirects to the Company Details View """
    permanent = False

    def get_redirect_url(self):
        return reverse_lazy("companies:detail")


company_redirect_view = CompanyRedirectView.as_view()
