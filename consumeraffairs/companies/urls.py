from django.urls import path

from consumeraffairs.companies.views import (
    company_list_view, company_redirect_view, company_create_view,
    company_detail_view, company_update_view, company_delete_view)

app_name = "companies"
urlpatterns = [
    path("", view=company_list_view, name="list"),
    path("~redirect/", view=company_redirect_view, name="redirect"),
    path("create/", view=company_create_view, name="create"),
    path("<slug:name>", view=company_detail_view, name="detail"),
    path("<slug:name>/update/", view=company_update_view, name="update"),
    path("<slug:name>/delete/", view=company_delete_view, name="delete")
]
