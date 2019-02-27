from .models import Review
from django.forms import modelform_factory, Textarea

ReviewForm = modelform_factory(
    Review,
    fields=('company', 'rating', 'title', 'summary'),
    widgets={"summary": Textarea()})
