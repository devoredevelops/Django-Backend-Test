from django.contrib import admin

from .forms import ReviewForm
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    form = ReviewForm
