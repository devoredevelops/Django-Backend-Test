from django.db import models
from django.core.validators import RegexValidator, MaxValueValidator, MaxLengthValidator
from consumeraffairs.users.models import User
from consumeraffairs.companies.models import Company


# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    RATINGS_CHOICES = [(1, 'one'),
                       (2, 'two'),
                       (3, 'three'),
                       (4, 'four'),
                       (5, 'five')]
    rating = models.Field(choices=RATINGS_CHOICES, verbose_name='Rating', help_text='Must be between 1 - 5',
                                 validators=[MaxValueValidator(limit_value=5)])
    title = models.CharField(verbose_name='Title', max_length=64, help_text='No more than 64 chars',
                             validators=[MaxLengthValidator(limit_value=64)])
    summary = models.TextField(verbose_name='Summary', max_length=10000, help_text='No more than 10k chars',
                               validators=[MaxLengthValidator(limit_value=10000)])
    ip_addr = models.IPAddressField(verbose_name='IP Address', help_text='IP of the review submitter')
    date_submitted = models.DateTimeField(verbose_name='Date Submitted', help_text='The date the review was submitted')

    @property
    def ip_addr(self):
        return self.user.ip_addr
