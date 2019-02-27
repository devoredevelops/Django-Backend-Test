from django.contrib import admin

from .forms import CompanyForm
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    form = CompanyForm
