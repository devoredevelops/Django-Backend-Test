from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Review
from .forms import ReviewForm


class ReviewDetailView(LoginRequiredMixin, DetailView):
    """ Shows Details about a Review """
    model = Review
    slug_field = "title"
    slug_url_kwarg = "title"
    fields = ["company", "rating", "title", "summary"]


review_detail_view = ReviewDetailView.as_view()


class ReviewListView(LoginRequiredMixin, ListView):
    """ Lists Reviews """
    model = Review
    slug_field = "title"
    slug_url_kwarg = "title"


review_list_view = ReviewListView.as_view()


class ReviewCreateView(LoginRequiredMixin, CreateView):
    """ Creates a Review """
    model = Review
    form = ReviewForm
    fields = ["company", "rating", "title", "summary"]

    def get_success_url(self):
        return reverse_lazy("reviews:list")


review_create_view = ReviewCreateView.as_view()


class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """ Edits a Review """
    model = Review
    form = ReviewForm
    fields = ["company", "rating", "title", "summary"]
    slug_field = "title"
    slug_url_kwarg = "title"

    def get_success_url(self):
        return reverse_lazy("reviews:list")


review_update_view = ReviewUpdateView.as_view()


class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """ Deletes a Review """
    model = Review
    slug_field = "title"
    slug_url_kwarg = "title"
    success_url = reverse_lazy("reviews:list")


review_delete_view = ReviewDeleteView.as_view()


class ReviewRedirectView(LoginRequiredMixin, RedirectView):
    """ Redirects to the Review Details View """
    permanent = False

    def get_redirect_url(self):
        return reverse_lazy("reviews:detail")


review_redirect_view = ReviewRedirectView.as_view()
