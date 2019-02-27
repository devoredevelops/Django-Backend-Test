from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MaxLengthValidator
from consumeraffairs.companies.models import Company
from django.urls import reverse
from django.utils.timezone import now


class Review(models.Model):
    """ The Review model """
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    RATINGS_CHOICES = [(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")]
    rating = models.IntegerField(
        choices=RATINGS_CHOICES,
        verbose_name="Rating",
        help_text="Must be a number 1 through 5",
        validators=[MaxValueValidator(limit_value=5)],
        default=RATINGS_CHOICES[4])
    title = models.CharField(
        verbose_name="Title",
        max_length=64,
        help_text="No more than 64 chars",
        validators=[MaxLengthValidator(limit_value=64)],
        unique=True)
    summary = models.TextField(
        verbose_name="Summary",
        max_length=10000,
        help_text="No more than 10k chars",
        validators=[MaxLengthValidator(limit_value=10000)])
    date_submitted = models.DateTimeField(
        verbose_name="Date Submitted",
        help_text="The date the review was submitted",
        default=now)

    def get_absolute_url(self):
        return reverse("reviews:detail", kwargs={"title": self.title})

    def __str__(self):
        return self.title
