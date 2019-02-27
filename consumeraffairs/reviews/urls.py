from django.urls import path

from consumeraffairs.reviews.views import (
    review_list_view, review_redirect_view, review_create_view,
    review_detail_view, review_update_view, review_delete_view)

app_name = "reviews"
urlpatterns = [
    path("", view=review_list_view, name="list"),
    path("~redirect/", view=review_redirect_view, name="redirect"),
    path("create/", view=review_create_view, name="create"),
    path("<slug:title>", view=review_detail_view, name="detail"),
    path("<slug:title>/update/", view=review_update_view, name="update"),
    path("<slug:title>/delete/", view=review_delete_view, name="delete")
]
