from .models import Company
from django.forms import modelform_factory

CompanyForm = modelform_factory(Company, fields=('name', ))
